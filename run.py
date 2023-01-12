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

    def total_monthly_weight():
        """
        Function to calculate the total weight of all the cattle combined for each month
        """
        """
        [Jan: 2456, Feb: 2982...]
        create a dictionary where the months are the keys and then sum of all cattle is the value.
        possibly calculate the the total weight for each month first then assign that to the value. Using a for loop?
        """
    total_weight = total_monthly_weight()

    def average_weight(total_weight):
        """
        Calculate the average weight of an individual animal for each month of the year. 
        Using the total weight for each month of the year from the total_monthly_weight function and then 
        dividing it by the number of cattle in this case 20. 
        """
        #average weight = total_weight/ len(row[1])

    def average_monthly_gain():
        """
        Difference in the average weight gained by the cattle from month to month.
        Using the average_weight function and calculating the difference in one month from the previous.
        """
        #monthly gain = average_weight[december] - average_weight[november] etc


    def average_daily_gain():
        """
        Function to calculate the average daily weight gain of the average cow in the herd.
        """
        #adg = average_weight/(number of days in each month) need to round() answer down to 1 decimal place
        #adg = [jan: 1,2, feb: 1,4, ... etc]


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