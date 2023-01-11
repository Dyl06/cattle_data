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

Cattle_data = SHEET.worksheet('Weight')
data = Cattle_data.get_all_values()
print(data)


class Inputs:
    """
    Class to call google sheets and process sheets.
    """


class CattleWeights:
    """
    Class to group together all the functions for evaluating the cattle weight
    data from the weight SHEET
    """


class CattleFeed:
    """
    Class to group together all the functions for evaluating the feed data
    from the feed SHEET
    """


class Report: 
    """
    Class to compile the data from the CattleWeights and CattleFeed classes 
    and create the usable report to be added to the report SHEET
    """


class Main():
    """
    Class to execute the entire aplication. 
    """