### Data Cleaning & Visualization of Dataset "Online Foods" from Kaggle

## Project Overview
This project analyzes online food order data from Bengaluru, India. It aims to provide insights into the data using Looker Studio and perform some data cleaning with Python.

## Data Description
The dataset, named `onlinefoods.csv`, includes several fields such as age, gender, marital status, occupation, monthly income, latitude, longitude, and customer feedback. This data is processed and analyzed to understand the market segmentation and customer behavior across different zones of Bengaluru.

## Insights During the Project
- **Student Demographics**: A significant number of orders come from students, with most reporting no income, highlighting the importance of affordable menu options.
- **Geographic Visualization**: Combined longitude and latitude data to create a geographic map in Looker Studio, providing visual insights into popular areas for orders.
- **Income Data Handling**: Addressed messy income data by normalizing income ranges to their midpoints for clearer analysis, e.g., treating '10001 to 25000' as 17500.
- **Zone Categorization**: Initially struggled with miscategorized 'other' zones. Manually verified ambiguous cases via Google Maps, ensuring accurate area classification.
- **Data Limitations**: Noted the lack of temporal data, which could restrict deeper trend analysis over time, suggesting an area for future data collection improvement.


## File Structure
- `onlinefoods.csv`: Raw data file containing online food orders.
- `process_data.py`: Python script for processing and cleaning data.
- `prepared_onlinefoods_for_looker.csv`: Cleaned data file ready for visualization.

## Link to the Data
[Online Food Dataset on Kaggle](https://www.kaggle.com/datasets/sudarshan24byte/online-food-dataset)
