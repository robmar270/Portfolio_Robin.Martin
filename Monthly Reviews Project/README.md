# Monthly Reviews Project

## Overview
During my internship at a startup B2B SaaS company, I spearheaded the development of a monthly review system akin to "Spotify Wrapped" for our customers. This system provided valuable insights on how customers used our platform, enhancing business value and fostering stronger customer relationships.

## Project Description
The project aimed to automate the distribution of personalized monthly updates to customers, segmented into four distinct categories based on platform usage and industry. The solution involved creating complex SQL queries for data extraction and using automation tools to send customized emails.

### Solutions Implemented

#### Solution 1: Microsoft Power Automate

1. **Data Extraction**:
    - Developed SQL scripts to retrieve customer data from the company's database.
    - Exported the retrieved data as CSV files.
    - Loaded the CSV files into four different Excel sheets.

2. **Email Automation**:
    - Utilized Microsoft Power Automate to extract data from the Excel sheets based on `customer_id`.
    - Created HTML email templates to personalize the email content.
    - Automated the email send-out process.

**Key Features:**
- **Data Retrieval**: Fetches company data from Excel sheets.
- **Email Automation**: Sends out personalized emails through Microsoft Power Automate.
- **Dynamic Email Content**: Integrates processed data into HTML templates.

#### Solution 2: Python Script with Google Sheets API

1. **Data Retrieval**:
    - Leveraged the Google Sheets API to fetch customer data from a Google spreadsheet.

2. **Data Manipulation**:
    - Performed basic data manipulations to tailor the information for each customer segment.
    - Dynamically inserted the processed data into an HTML template based on the `company_id`.

3. **Email Automation**:
    - Configured the application with app-specific credentials obtained from Google.
    - Sent out personalized emails.
    - Logged and displayed the email addresses to which the updates were successfully sent.

**Key Features:**
- **Data Retrieval**: Fetches company data from Google Sheets.
- **Data Manipulation**: Processes and segments data for personalized communication.
- **Dynamic Email Content**: Integrates processed data into HTML templates.
- **Email Automation**: Sends out personalized emails through a secured application.
- **Logging**: Tracks and displays the recipients of each email.

## Usage Restrictions
Copyright [2024] [Robin Martin] All Rights Reserved

Unauthorized copying, modification, distribution, or use of this software, via any medium, is strictly prohibited without the prior written permission of Robin Martin.

For permissions or inquiries, please contact: [robin.martin35@gmail.com]
