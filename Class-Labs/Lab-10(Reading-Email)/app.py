import imaplib
import email
import time
import os
from email.header import decode_header
import io

class EmailAttachmentFetcher:
    def __init__(self, email_address, password, imap_server="imap.gmail.com", 
                 target_subject=None, check_interval=60):
        """
        Initialize the Email Attachment Fetcher.
        
        Args:
            email_address (str): Your email address
            password (str): Your email password or app password
            imap_server (str): IMAP server address (default: Gmail)
            target_subject (str): Subject text to match (None matches all)
            check_interval (int): How often to check for new emails in seconds
        """
        self.email_address = email_address
        self.password = password
        self.imap_server = imap_server
        self.target_subject = target_subject
        self.check_interval = check_interval
        self.processed_emails = set()
        self.attachments_in_memory = {}
        
    def connect(self):
        """Establish connection to the IMAP server."""
        self.mail = imaplib.IMAP4_SSL(self.imap_server)
        self.mail.login(self.email_address, self.password)
        print(f"Successfully connected to {self.imap_server}")
        
    def disconnect(self):
        """Close the connection to the IMAP server."""
        if hasattr(self, 'mail'):
            self.mail.close()
            self.mail.logout()
            print("Disconnected from the server")
            
    def get_decoded_header(self, header_text):
        """Decode email header text."""
        decoded_parts = decode_header(header_text)
        decoded_text = ""
        
        for text, encoding in decoded_parts:
            if isinstance(text, bytes):
                if encoding:
                    decoded_text += text.decode(encoding)
                else:
                    decoded_text += text.decode('utf-8', errors='replace')
            else:
                decoded_text += text
                
        return decoded_text
            
    def fetch_attachments(self):
        """Check for new emails and fetch attachments from matching ones."""
        self.mail.select("INBOX")
        
        # Search for all unseen emails
        status, messages = self.mail.search(None, "UNSEEN")
        
        if status != "OK":
            print("No new messages found or error occurred")
            return
            
        for message_id in messages[0].split():
            # Fetch the email
            status, msg_data = self.mail.fetch(message_id, "(RFC822)")
            
            if status != "OK":
                print(f"Error fetching message {message_id}")
                continue
                
            raw_email = msg_data[0][1]
            email_message = email.message_from_bytes(raw_email)
            
            # Get email ID for tracking processed emails
            email_id = email_message.get("Message-ID", message_id.decode())
            
            # Skip if we've processed this email already
            if email_id in self.processed_emails:
                continue
                
            # Check subject
            subject = self.get_decoded_header(email_message["Subject"])
            
            if self.target_subject is None or self.target_subject in subject:
                sender = self.get_decoded_header(email_message["From"])
                print(f"Found matching email from {sender} with subject: {subject}")
                
                # Process attachments
                self._process_attachments(email_message, email_id)
            
            # Mark as processed
            self.processed_emails.add(email_id)
    
    def _process_attachments(self, email_message, email_id):
        """Extract and store attachments from the email."""
        for part in email_message.walk():
            if part.get_content_maintype() == "multipart":
                continue
                
            if part.get("Content-Disposition") is None:
                continue
                
            filename = part.get_filename()
            
            if filename:
                filename = self.get_decoded_header(filename)
                content = part.get_payload(decode=True)
                
                # Store the attachment in memory
                memory_file = io.BytesIO(content)
                self.attachments_in_memory[filename] = memory_file
                
                print(f"Attachment '{filename}' saved to memory")
                
                # Example of how to access the attachment
                print(f"Attachment size: {len(content)} bytes")
    
    def get_attachment(self, filename):
        """Retrieve an attachment from memory by filename."""
        if filename in self.attachments_in_memory:
            # Return the BytesIO object to the beginning
            self.attachments_in_memory[filename].seek(0)
            return self.attachments_in_memory[filename]
        return None
    
    def list_attachments(self):
        """List all attachments stored in memory."""
        if not self.attachments_in_memory:
            print("No attachments in memory")
            return
            
        print("Attachments in memory:")
        for filename in self.attachments_in_memory:
            size = self.attachments_in_memory[filename].getbuffer().nbytes
            print(f"- {filename} ({size} bytes)")
    
    def run(self):
        """Main loop to continuously check for new emails."""
        try:
            self.connect()
            
            print(f"Monitoring for emails{'with subject: ' + self.target_subject if self.target_subject else ''}")
            print(f"Checking every {self.check_interval} seconds...")
            
            while True:
                self.fetch_attachments()
                time.sleep(self.check_interval)
                
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.disconnect()


# Example usage
if __name__ == "__main__":
    # Replace with your actual email credentials
    EMAIL = "sachinparmar0246@gmail.com"
    PASSWORD = "ayfv qlil eyaq guny"
    
    # What subject to look for (set to None to fetch from all emails)
    TARGET_SUBJECT = "Important Report"
    
    # Create and run the fetcher
    fetcher = EmailAttachmentFetcher(
        email_address=EMAIL,
        password=PASSWORD,
        target_subject=TARGET_SUBJECT,
        check_interval=30  # Check every 30 seconds
    )
    
    # Start monitoring
    fetcher.run()
    
    # NOTE: The following code won't execute during normal operation
    # since run() contains an infinite loop
    # To access attachments, you would need to modify the script to
    # handle them as needed for your specific use case