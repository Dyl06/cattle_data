import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Cattle_data')


def load_data():
    """
    Load data from Google Docs
    """
    cattle_data = SHEET.worksheet('Weight')
    data = cattle_data.get_all_records()
    print(data)
    return data[0]

load_data()








"""
cattle_data = SHEET.worksheet('Weight')
"""
cows = {}
for ind in range(2, 5):
    cows = cattle_data.col_values(ind)
    print(cows)
"""
#load_data()


def update_worksheet(data, worksheet):
    """ """
    Recieves a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """ """
    
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")

update_worksheet(Weight_input_int, "Weight")
"""