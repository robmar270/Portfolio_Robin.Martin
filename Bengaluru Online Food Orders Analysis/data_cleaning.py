import pandas as pd

def load_data(filepath): # reading csv file
    return pd.read_csv(filepath)

def standardize_column_names(df): # standarize with snake_case lower case format
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
    return df

def examine_income_column(df):
    print("Unique values in 'monthly_income':")
    print(df['monthly_income'].unique())
    return df['monthly_income'].describe()

def convert_to_categorical(df, columns): # Converts specified columns to categorical data type.
    for col in columns:
        df[col] = df[col].astype('category')
    return df

def convert_monthly_income(df): # I choose to convert this beacuse to make it easier to use in looker studio
    income_mapping = {
        'No Income': 0,
        'Below Rs.10000': 5000,
        '10001 to 25000': 17500,
        '25001 to 50000': 37500,
        'More than 50000': 75000
    }
    df['monthly_income'] = df['monthly_income'].replace(income_mapping).astype(int)
    return df

def categorize_area(row): # Categorize with zones to a Area column, based on longitude and latitude
    lat = row['latitude']
    lon = row['longitude']

    # I choose this cordinate based on the city center
    central_lat = 12.9614
    central_lon = 77.5731
    # This defines a range of kilometers (4km)
    lat_range = 0.04  
    lon_range = 0.04

    if central_lat - lat_range <= lat <= central_lat + lat_range and \
       central_lon - lon_range <= lon <= central_lon + lon_range:
        return 'Central Bengaluru'
    elif 12.9716 <= lat <= 13.1000 and 77.5000 <= lon <= 77.6200:
        return 'North Bengaluru'
    elif 12.8000 <= lat < 12.9716 and 77.5000 <= lon <= 77.6200:
        return 'South Bengaluru'
    elif 12.8000 <= lat <= 13.1000 and 77.6201 <= lon <= 77.7500:
        return 'East Bengaluru'
    elif 12.8000 <= lat <= 13.1000 and 77.3700 <= lon < 77.5000:
        return 'West Bengaluru'
    return 'Other'

# Here is where I put all the functions together
def process_data(filepath):
    df = load_data(filepath)
    df = standardize_column_names(df)
    print(examine_income_column(df))
    df = convert_to_categorical(df, ['gender', 'marital_status', 'occupation', 'educational_qualifications', 'output', 'feedback'])
    df = convert_monthly_income(df)
    df['coordinates'] = df.apply(lambda row: f"{row['latitude']},{row['longitude']}", axis=1)
    df['area'] = df.apply(categorize_area, axis=1)
    return df

if __name__ == "__main__":
    filepath = 'onlinefoods.csv'  # insert the path for the file
    cleaned_data = process_data(filepath)
    cleaned_data.to_csv('clean_data.csv', index=False) # Saves it to a new file
    print("Data processed and saved for Looker Studio.")