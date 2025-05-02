import numpy as np

# Create a dictionary mapping month abbreviations (uppercase) to month numbers
month_abbr_to_num = {
    'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
    'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12
}


# Function to convert Fiscal Year and Month (abbv) to a Year-Date
def convert_to_fiscal_year_date(row):
    month_num = month_abbr_to_num[row['Month (abbv)'].upper()]
    fiscal_year = int(row['Fiscal Year'])  # Convert Fiscal Year to integer
    
    # Adjust fiscal year for months January through September
    if month_num >= 10:  # Jan - Sep belong to the previous calendar year
        fiscal_year -= 1
    
    # Format the fiscal year and month into a date string
    return f"{fiscal_year}-{month_num:02d}-01"


# Function for MAPE, probably something predefined but here for ease of use
def mean_absolute_percentage_error(y_true, y_pred):
    return np.abs((y_true - y_pred) / y_true) * 100

def calculate_mape(predictions, actuals):
    return np.mean(np.abs((actuals - predictions) / actuals)) * 100