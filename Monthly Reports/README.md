# 📧 Monthly Reviews Project

## 📝 Overview
This project streamlines the process of sending **personalized monthly review emails** using data from Google Sheets. A Python script does the heavy lifting—retrieving, processing, and automating secure email delivery.

---

## 🚀 Key Steps

### 1️⃣ Fetching the Data
- **Google Sheets API**: Data is retrieved from two sheets: `clean_data` and `email`.
- **Script Location**: The Python script handling data retrieval and email automation is `solution_02.py`.

### 2️⃣ Processing the Data
- **Pandas**: Data is imported into pandas DataFrames for cleaning and manipulation.
- **Merging**: The script combines data from both sheets using `company_id` as a common key.

### 3️⃣ Automating Emails
- **Jinja2**: Custom email content is dynamically created with the Jinja2 templating engine.
- **SMTP with SSL**: Emails are sent securely using the SMTP protocol.
- **HTML Template**: The email design is defined in `email_template.html` for a polished, professional look.

---

## ✨ Features
- **Dynamic Data Handling**: Real-time integration with Google Sheets.
- **Personalized Emails**: Each email contains metrics tailored to the recipient's company.
- **Secure Delivery**: All emails are sent through an SSL-secured SMTP connection.
- **Reusable Design**: Modular code and templates ensure scalability and adaptability.

---

## 📂 Files in the Project
- **`monthly_reviews_project.py`**: Main Python script for data retrieval and email automation.
- **`flow_01.sql`**: SQL script for Flow 01 transformations.

---

This project combines automation, secure email handling, and dynamic content generation to deliver personalized insights effectively. 🌟
