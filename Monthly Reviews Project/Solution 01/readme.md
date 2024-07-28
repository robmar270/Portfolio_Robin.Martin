## Solution 01: Montly Reviews Project 

### Overview
This solution involves creating personalized emails using data retrieved from an SQL database, processed through Excel, and sent out using Microsoft Power Automate.

### Steps and Explanations

1. **Data Extraction**:
    - **SQL Scripts**: I created four different SQL scripts and you if you wanna see the logic behind.
    - **Example Script**: You can find one of the four scripts in the file `01_flow.sql`.

2. **Excel Integration**:
    - **Description**:
        - After extracting the data using SQL scripts, the data was exported into CSV files.
    - **Note**:
        - Due to privacy concerns, the actual data cannot be displayed.
     
3. **Email Automation**:
    - **Microsoft Power Automate Workflow**:
        - **Description**:
            - Microsoft Power Automate was configured to automate the email send-out process.
            - Triggers were set to extract data from the Excel sheets based on `company_id`.
            - Dynamic HTML email templates were created to personalize the email content using the extracted data.
        - **HTML Template Example**:
            - You can find the HTML template and an example image of the email in the files `email_template.html` and `email_img_example.png`.
         
### Key Features:
- **Data Retrieval**: SQL scripts to fetch relevant data.
- **Email Automation**: Microsoft Power Automate for email distribution.
- **Dynamic Content**: HTML templates for personalized emails.

### Implementation Steps:

1. **Prepare SQL Scripts**:
    - Create and test SQL scripts to ensure they retrieve the correct data for each customer segment.
    - Export the data from the SQL queries into CSV files.

2. **Load Data into Excel**:
    - Open the CSV files and load the data into separate Excel sheets.
    - Ensure each Excel sheet is correctly formatted and contains the necessary columns.

3. **Set Up Microsoft Power Automate**:
    - Log in to Microsoft Power Automate.
    - Create a new flow and set the trigger to start the process (e.g., when a file is updated).
    - Add actions to extract data from the Excel sheets.
    - Configure the dynamic HTML template with placeholders for customer-specific data.
    - Set up the email send-out action and test the flow to ensure emails are sent correctly.

### Usage Restrictions
Copyright [2024] [Robin Martin] All Rights Reserved

Unauthorized copying, modification, distribution, or use of this software, via any medium, is strictly prohibited without the prior written permission of Robin Martin.

For permissions or inquiries, please contact: [robin.martin35@gmail.com]

