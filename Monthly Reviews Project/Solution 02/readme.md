# Solution 02: Monthly Reviews Project

## Overview
This solution involves sending personalized emails using data retrieved from Google Sheets, processed with a Python script, and sent using SMTP. The script dynamically integrates data into an HTML email template.

## Steps and Explanations

1. **Data Retrieval**:
    - **Google Sheets API**: The script uses the Google Sheets API to fetch data.
    - **Data Sources**: Data is retrieved from two sheets: `clean_data` and `email`.
    - **Script Location**: The Python script for data retrieval and email automation is located in `solution_02.py`.

2. **Data Processing**:
    - **Pandas**: Data is loaded into pandas DataFrames for processing.
    - **Merging Data**: The data from `clean_data` and `email` sheets are merged on `company_id`.

3. **Email Automation**:
    - **Jinja2**: The HTML email content is generated using the Jinja2 templating engine.
    - **SMTP**: Emails are sent using the SMTP protocol with SSL for secure email sending.
    - **HTML Template**: The HTML email template is located in `email_template.html`.

## Key Features
- **Data Retrieval**: Fetches data from Google Sheets.
- **Data Processing**: Uses pandas for data manipulation and merging.
- **Dynamic Content**: Integrates processed data into an HTML template.
- **Email Automation**: Sends out personalized emails through a secure SMTP connection.


## Files in the Repository

- `montly_reviews_project.py`: The main Python script for data retrieval and email automation.
- `flow_01.sql`: The SQL script I did for flow 01

## Usage Restrictions
Copyright [2024] [Robin Martin]. All Rights Reserved.

Unauthorized copying, modification, distribution, or use of this software, via any medium, is strictly prohibited without the prior written permission of Robin Martin.

For permissions or inquiries, please contact: [robin.martin35@gmail.com]
