# Document Analyzer Crew  

An AI-powered multi-agent system for analyzing documents, extracting key information, comparing it against reference data, and generating detailed reports. Built using **Crew AI**, this project enables seamless workflow automation with a Gradio-based user interface.  

## Features  
- **Multi-Agent Functionality**:  
  Leverages three specialized AI agents:
  - **Text Extraction Specialist**: Extracts key details from document text.  
  - **Document Comparison Expert**: Compares extracted details against reference standards and identifies discrepancies.  
  - **Detailed Report Generator**: Creates comprehensive analysis reports.  

- **PDF Text Extraction**: Extracts text from uploaded PDF documents.  
- **Email Extraction**: Detects email addresses embedded in the document.  
- **Automated Emailing**: Sends the analysis results to the detected email (optional).  
- **Gradio UI**: Provides a user-friendly interface for interacting with the system.  

---
## Set up environment variables for email functionality:
- **SMTP_EMAIL**: Your email address for sending reports.
- **SMTP_PASSWORD**: Your email password or app-specific password.


---
## Code Overview
###Multi-Agent System
The project employs a multi-agent architecture using Crew AI:


---
## Text Extraction Agent:
- **Role**: Extracts key details from documents.
- **Goal**: Parse and identify critical information.

## Comparison Agent:
- **Role**: Validates extracted data against reference data.
- **Goal**: Identify discrepancies and highlight differences.

## Reporting Agent:
- **Role**: Summarizes findings in a user-friendly format.
- **Goal**: Deliver actionable insights.


---
## Email Functionality
Optional email integration allows automated delivery of analysis results to the email address extracted from the document.

---
## Gradio UI
Provides an intuitive interface for:
**Uploading PDFs**.
**Configuring analysis settings**.
**Viewing detailed results**.
