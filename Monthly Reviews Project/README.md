# Monthly Reviews Project

## Description
During my last internship at a SaaS B2B company, we needed to send monthly updates to our clients. To address this requirement, I developed a solution that segments our customer base and automates the distribution of personalized emails.

This Python script leverages the Google Sheets API to retrieve company data from a spreadsheet. It performs basic data manipulations to tailor the information for each segment and then dynamically inserts this data into an HTML template based on the `company_id`. The emails are sent using a configured application that requires app-specific credentials, which I obtained by registering the application with Google. The script concludes by logging and displaying the email addresses to which the updates were successfully sent.

### Key Features:
- **Data Retrieval**: Fetches company data from Google Sheets.
- **Data Manipulation**: Processes and segments data for personalized communication.
- **Dynamic Email Content**: Integrates processed data into HTML templates.
- **Email Automation**: Sends out personalized emails through a secured application.
- **Logging**: Tracks and displays the recipients of each email.

### Usage Restrictions
Copyright [2024] [Robin Martin] All Rights Reserved

Unauthorized copying, modification, distribution, or use of this software, via any medium, is strictly prohibited without the prior written permission of Robin Martin.

For permissions or inquiries, please contact: [robin.martin35@gmail.com]
