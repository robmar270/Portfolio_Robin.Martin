# Standard libraries for system operations and data manipulation
import os
import ssl

# Data handling and analysis
import pandas as pd

# Email functionality libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Web requests and templating
import requests
from jinja2 import Template

# Environment variable management
from dotenv import load_dotenv

# Google API and authentication
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Load environment variables from .env file
load_dotenv()

# Initialize Google Sheets API with read-only access
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SERVICE_ACCOUNT_FILE = "keys.json"
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build("sheets", "v4", credentials=creds)

def fetch_data(sheet_id, range_name):
    """
    Retrieve data from Google Sheet using sheet ID and range in A1 notation.
    
    Returns a list of rows, each row as a list of values.
    """
    sheet = service.spreadsheets().values().get(spreadsheetId=sheet_id, range=range_name).execute()
    return sheet.get('values', [])

# Environment variables for spreadsheet ID
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

# Try to fetch data from Google Sheets and handle potential errors
try:
    # Fetch and prepare data
    data_clean = fetch_data(SPREADSHEET_ID, "clean_data")
    data_email = fetch_data(SPREADSHEET_ID, "email")
except Exception as e:
    print(f"Failed to fetch data: {e}")
    raise SystemExit(e)  # Exit the script if data fetch fails

# Proceed with data processing only if the fetching is successful
df_clean = pd.DataFrame(data_clean[1:], columns=data_clean[0])
df_email = pd.DataFrame(data_email[1:], columns=data_email[0])

# Merge DataFrames on 'company_id'
merged_df = pd.merge(df_clean, df_email[['company_id', 'email']], on='company_id', how='left')

# Convert merged DataFrame to dictionary for template processing
merged_data_dict = merged_df.to_dict(orient='records')

# Fetch company logo from GitHub
github_token = os.getenv('GITHUB_TOKEN')
github_raw_url = os.getenv('GITHUB_RAW_URL')
response = requests.get(github_raw_url, headers={"Authorization": f"token {github_token}"})

# Check response and handle image content
if response.status_code == 200:
    image_content = response.content
    print("Image fetched successfully.")
else:
    print("Failed to fetch image.")

# HTML template
html_body_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
   body {
      font-family: 'Open Sauce Sans', sans-serif;
      background-color: #f4f5f6db;
      margin: 0;
      padding: 0;
    }

    .email-container {
      width: 100%;
      max-width: 600px; /* Adjust as needed for your email layout */
      margin: auto;
      padding: 24px;
      background: #958fb0;
      border: 1px solid #eaebed;
      border-radius: 16px;
      text-align: center;
    }

    .logo img {
      max-width: 100%;
      height: auto;
      text-align: center;
    }

    .introduction {
      text-align: center;
      margin-bottom: 40px;
    }

    .introduction h1 {
      color: #1f2a37;
      font-family: 'Open Sauce Sans', sans-serif;
      font-size: 42px;
      margin-bottom: 10px;
    }

    .introduction h2 {
      color: #1f2a37;
      font-family: 'Open Sauce Sans', sans-serif;
      font-size: 22px;
      margin-top: 10px;

    }

    .introduction h3 {
      color: #1f2a37;
      font-family: 'Open Sauce Sans', sans-serif;
      font-size: 18px;      
    }

    .first-section{
      background-color: #958fb0;
      display: flex;
      justify-content: space-between;
    }

    .box1, .box2 {
      background-color: #eaebed;
      border-radius: 5px;
      width: 280px;
      height: 125px;
      margin: 5px auto;
      box-shadow: 0 7px 1px rgba(0, 0, 0, 0.1);
      height: auto;
      padding-bottom: 10px;
    }
    .box1 h4, .box2 h4 {
      text-align: center;
      font-size: 20px;
      margin-top: 15px;
    }


    .box1 p, .box2 p {
      text-align: center;
      font-size: 18px;
    }


    .second-section{
      background-color: #958fb0;
      display: flex;
      justify-content: space-between;
      padding-top: 2%;
    }
    .box3 {
      background-color: #eaebed;
      border-radius: 5px;
      width: 590px;
      height: auto;
      padding-bottom: 10px;
      align-items: center;
      margin: auto;  
      margin: 5px auto;
      box-shadow: 0 7px 1px rgba(0, 0, 0, 0.1);
      line-height: -1; /* Adjust the value to make the text closer */

    }

    .box3 h4 {
      text-align: center;
      font-size: 20px;
      margin-bottom: 10px;
      margin-top: 15px;
    }

    .box3 p{
    text-align: center;
    font-size: 18px;
    }
    .box3 div {
    text-align: center;
    margin-top: 5px;
    font-size: 16px;
    }

    .logo-lines {
      border-top: 2px solid #1f2a37;
      border-bottom: 2px solid #1f2a37;
      margin: 20px 0;
      border-radius: 2px;
    }

</style>
</head>
<body>
<!-- ... (previous template code) -->
<div class="email-container">
    <div class="logo-section logo-lines">
        <div class="logo">
            <img src="cid:logo_image" alt="Company Logo">
        </div>
    </div>    <!-- Dynamically generated sections for each company's data -->
        {% for company_id, metric_entries in merged_data_dict|groupby('company_id') %}
            <div class="metric-container" id="metric_{{ company_id }}">
                {% if metric_entries|length > 0 %}
                    <div class="introduction">
                        <h1>{{ metric_entries[0].company_name }}</h1>
                        <h2>Monthly Performance</h2>
                        <h3>Let's see what you have achieved with us</h3>
                    </div>
                {% endif %}

                <div class="first-section">
                    {% for entry in metric_entries %}
                        {% if entry.metric_name == 'Total Count Of Transports (This Month)' %}
                            <div class="box1">
                                <h4>Total Count of Transports</h4>
                                <p><b>Last Month</b></p>
                                <p>{{ entry.metric_value }}</p>
                                {% if 'Total Count Of Transports (This Year)' in metric_entries|map(attribute='metric_name') %}
                                    <p><b>Year to Date</b></p>
                                    <p>{{ metric_entries|selectattr('metric_name', 'equalto', 'Total Count Of Transports (This Year)')|map(attribute='metric_value')|first }}</p>
                                {% endif %}
                            </div>
                        {% elif entry.metric_name == 'Total Deliveries Not On Time (This Month)' %}
                            <div class="box2">
                                <h4>Total Deliveries Not On Time</h4>
                                <p><b>Last Month</b></p>
                                <p>{{ entry.metric_value }}</p>
                                {% if 'Total Deliveries Not On Time (This Year)' in metric_entries|map(attribute='metric_name') %}
                                    <p><b>Year to Date</b></p>
                                    <p>{{ metric_entries|selectattr('metric_name', 'equalto', 'Total Deliveries Not On Time (This Year)')|map(attribute='metric_value')|first }}</p>
                                {% endif %}
                            </div>
                        {% endif %}
                    {% endfor %}
                </div>

                <!-- Add the second-section here -->
                <div class="second-section">
                    <div class="box3">
                        <h4>Top Destinations</h4>
                        {% for entry in metric_entries %}
                            {% if entry.metric_name == 'Top Destinations (This Month)' or entry.metric_name == 'Top Destinations (This Year)' %}
                                {% if entry.metric_name == 'Top Destinations (This Month)' %}
                                    <p><b>Last Month</b></p>
                                {% elif entry.metric_name == 'Top Destinations (This Year)' %}
                                    <p><b>Year to Date</b></p>
                                {% endif %}
                                <div>{{ entry.metric_value }}</div>
                            {% endif %}
                        {% endfor %}
                    </div>
                </div>
            </div>
        {% endfor %}
        <footer style="text-align: center; padding: 20px; font-size: 12px; color: #fff; ">
  © 2024 Robin Martin. All rights reserved.
</footer>
</div>

</body>
</html>
"""

# Initialize the Jinja2 template with the HTML content
template = Template(html_body_template)

# Render the template with data to be used in emails
rendered_template = template.render(merged_data_dict=merged_data_dict)
# Uncomment the below line to output the rendered HTML for debugging purposes
# print(rendered_template)

# Group data by company_id for email targeting
grouped_df = merged_df.groupby("company_id")

# Email credentials (stored in variables for clarity and security)
email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")

# Loop through each grouped data subset to send personalized emails
for (metric_id, email_address), group_data in merged_df.groupby(['company_name', 'email']):
    if not group_data.empty:  # Check to ensure data is present before sending
        # Construct email subject using company name and a specific metric
        current_subject = f"Your Subject for {group_data.iloc[0]['company_name']} - Metric: {metric_id}"

        # Render HTML content for this specific group
        html_content = template.render(
            merged_data_dict=group_data.to_dict(orient="records"),
        )

        # Setup the MIME multi-part structure for the email content
        em = MIMEMultipart()
        em["From"] = email_sender
        em["To"] = email_address
        em["Subject"] = current_subject

        # Attach the HTML content
        html_part = MIMEText(html_content, "html")
        em.attach(html_part)

        # Attach the company logo image using Content-ID for embedding in HTML
        image_attachment = MIMEImage(image_content)
        image_attachment.add_header("Content-ID", "<logo_image>")
        em.attach(image_attachment)

        # Setup secure SMTP connection using SSL
        context = ssl.create_default_context()

        # Log in to SMTP server and send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_address, em.as_string())
            # Log output for each sent email for tracking
            print(f"Email sent to {email_address}")
