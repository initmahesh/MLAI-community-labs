import imaplib
import email
from email.header import decode_header
import time
import os
import sys
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("email_monitor.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class EmailMonitor:
    def __init__(self, email_address, password, imap_server="imap.gmail.com", target_subject=None):
        """
        Initialize the email monitor with credentials and target subject
        
        Args:
            email_address: Your email address
            password: Your email password or app password
            imap_server: IMAP server address (default: Gmail)
            target_subject: The specific subject to monitor for
        """
        self.email_address = email_address
        self.password = password
        self.imap_server = imap_server
        self.target_subject = target_subject
        self.last_checked_ids = set()
        self.mail = None
        self.max_retries = 5
        self.retry_delay = 30  # seconds
        
    def connect(self):
        """Establish connection to the IMAP server with retry logic"""
        retries = 0
        while retries < self.max_retries:
            try:
                if self.mail:
                    try:
                        self.mail.close()
                        self.mail.logout()
                    except:
                        pass
                
                logger.info(f"Connecting to {self.imap_server}...")
                self.mail = imaplib.IMAP4_SSL(self.imap_server)
                self.mail.login(self.email_address, self.password)
                logger.info("Connection established successfully")
                return True
            except imaplib.IMAP4.error as e:
                retries += 1
                logger.error(f"IMAP error during connection (attempt {retries}/{self.max_retries}): {str(e)}")
                time.sleep(self.retry_delay)
            except Exception as e:
                retries += 1
                logger.error(f"Unexpected error during connection (attempt {retries}/{self.max_retries}): {str(e)}")
                time.sleep(self.retry_delay)
        
        logger.critical(f"Failed to connect after {self.max_retries} attempts")
        return False
        
    def disconnect(self):
        """Close the connection to the IMAP server"""
        if hasattr(self, 'mail') and self.mail:
            try:
                self.mail.close()
                self.mail.logout()
                logger.info("Disconnected from IMAP server")
            except Exception as e:
                logger.warning(f"Error during disconnect: {str(e)}")
            
    def fetch_email_content(self, email_id):
        """Fetch and parse the content of an email by its ID"""
        try:
            res, msg_data = self.mail.fetch(email_id, "(RFC822)")
            
            if res != 'OK':
                logger.error(f"Error fetching email ID {email_id}")
                return None
                
            raw_email = msg_data[0][1]
            email_message = email.message_from_bytes(raw_email)
            
            # Get subject
            subject = decode_header(email_message["Subject"])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode()
                
            # Get sender
            from_ = decode_header(email_message.get("From", ""))[0][0]
            if isinstance(from_, bytes):
                from_ = from_.decode()
                
            # Get date
            date_str = email_message.get("Date", "")
            
            # Get body
            body = ""
            if email_message.is_multipart():
                for part in email_message.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    
                    # Skip attachments
                    if "attachment" in content_disposition:
                        continue
                        
                    if content_type == "text/plain":
                        body = part.get_payload(decode=True).decode()
                        break
                    elif content_type == "text/html" and not body:
                        body = part.get_payload(decode=True).decode()
            else:
                body = email_message.get_payload(decode=True).decode()
                
            return {
                "id": email_id.decode(),
                "subject": subject,
                "from": from_,
                "date": date_str,
                "body": body
            }
        except Exception as e:
            logger.error(f"Error parsing email: {str(e)}")
            return None
            
    def check_connection(self):
        """Check if connection is still alive and reconnect if needed"""
        try:
            status, response = self.mail.noop()
            return status == 'OK'
        except:
            logger.warning("Connection lost, attempting to reconnect...")
            return self.connect()
            
    def monitor_for_new_emails(self, check_interval=60, callback=None):
        """
        Continuously monitor for new emails with the target subject
        
        Args:
            check_interval: Time in seconds between email checks
            callback: Function to call when matching email is found, 
                      receives email content as parameter
        """
        run_forever = True
        
        while run_forever:
            try:
                if not self.connect():
                    logger.error("Could not establish connection. Retrying in 60 seconds...")
                    time.sleep(60)
                    continue
                    
                logger.info(f"Started monitoring for emails with subject: '{self.target_subject}'")
                logger.info(f"Checking every {check_interval} seconds...")
                
                connection_check_counter = 0
                
                while True:
                    # Periodically check connection (every 10 iterations)
                    connection_check_counter += 1
                    if connection_check_counter >= 10:
                        if not self.check_connection():
                            logger.warning("Connection check failed, restarting monitoring loop")
                            break
                        connection_check_counter = 0
                    
                    try:
                        self.mail.select("INBOX")
                        
                        # Search for all unread emails
                        search_criteria = '(UNSEEN)'
                        if self.target_subject:
                            # If target subject is specified, refine search
                            search_criteria = f'(UNSEEN SUBJECT "{self.target_subject}")'
                            
                        result, data = self.mail.search(None, search_criteria)
                        
                        if result != 'OK':
                            logger.error("Error searching for emails")
                            time.sleep(check_interval)
                            continue
                            
                        email_ids = data[0].split()
                        
                        for email_id in email_ids:
                            email_id_str = email_id.decode()
                            if email_id_str not in self.last_checked_ids:
                                # New matching email found
                                email_content = self.fetch_email_content(email_id)
                                
                                if email_content:
                                    logger.info(f"New email detected: From {email_content['from']}, Subject: {email_content['subject']}")
                                    
                                    # Process the email content
                                    if callback and callable(callback):
                                        try:
                                            callback(email_content)
                                        except Exception as e:
                                            logger.error(f"Error in callback function: {str(e)}")
                                    
                                    # Add to checked IDs
                                    self.last_checked_ids.add(email_id_str)
                                    
                                    # Limit the size of last_checked_ids to prevent memory growth
                                    if len(self.last_checked_ids) > 1000:
                                        # Keep the 500 most recent IDs
                                        self.last_checked_ids = set(list(self.last_checked_ids)[-500:])
                    except imaplib.IMAP4.abort:
                        logger.error("IMAP connection aborted. Reconnecting...")
                        if not self.connect():
                            break
                    except imaplib.IMAP4.error as e:
                        logger.error(f"IMAP error: {str(e)}. Reconnecting...")
                        if not self.connect():
                            break
                    except Exception as e:
                        logger.error(f"Error during email check: {str(e)}")
                        
                    # Sleep before next check
                    time.sleep(check_interval)
                    
            except KeyboardInterrupt:
                logger.info("Monitoring stopped by user.")
                run_forever = False
            except Exception as e:
                logger.error(f"Critical error occurred: {str(e)}")
                logger.info("Restarting monitoring in 60 seconds...")
                time.sleep(60)
            finally:
                self.disconnect()

# Example callback function to process matching emails
def process_email(email_content):
    """
    Example callback function to process matching emails
    You can implement your own logic here
    """
    logger.info("Processing new email...")
    
    # Add your custom processing logic here
    # For example, save to database, trigger another process, etc.
    
    # Example: Save email content to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"email_{timestamp}.txt"
    
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"From: {email_content['from']}\n")
            f.write(f"Subject: {email_content['subject']}\n")
            f.write(f"Date: {email_content['date']}\n\n")
            f.write(f"Body:\n{email_content['body']}")
        
        logger.info(f"Email content saved to {filename}")
    except Exception as e:
        logger.error(f"Error saving email to file: {str(e)}")

if __name__ == "__main__":
    try:
        # Replace these with your actual email credentials
        EMAIL_ADDRESS = "sachinparmar0246@gmail.com"
        PASSWORD = "ayfv qlil eyaq guny"
        
        # Define the specific subject to monitor for
        TARGET_SUBJECT = "Important Notification"
        
        # Create the email monitor
        monitor = EmailMonitor(
            email_address=EMAIL_ADDRESS,
            password=PASSWORD,
            target_subject=TARGET_SUBJECT
        )
        
        # Start monitoring with a callback function
        monitor.monitor_for_new_emails(
            check_interval=30,  # Check every 30 seconds
            callback=process_email
        )
    except Exception as e:
        logger.critical(f"Fatal error in main thread: {str(e)}")