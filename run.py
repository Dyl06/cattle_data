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
    # create one function that calculates total and then pass used and wasted into it.
    def total_used_feed():
        """
        Function to calculate the total amount of feed used over the year.
        """
        #sum(len(feed row))


    def total_wasted_feed():
        """
        Function to calculate how much food has been wasted over the year. 
        """
        #sum(len(waste row))


    def total_consumed():
        """
        Function for the amount of food actually consumed by the cattle over the year. 
        """
        #consumed = total_used_feed() - total_wasted_feed()


# possibly use the same one function that calculates totals and just pass it the feed cost. 
    def feed_cost():
        """
        Function for the total cost of all the feed for the year. Assuming an average cost of feed of £150 per ton.
        """
        # cost = total_used_feed() * 150


    def cost_of_waste():
        """
        Function for the total cost of all the wasted food for the year. Assuming the same cost of £150 per ton
        """
        #waste = total_wasted_feed() * 150


    def individual_consumption():
        """
        Function to calculate the average consumption of each individual animal.
        """
        #ind_consumption = consumed / len(row1)
        

    def average_consumption():
        """
        Function to calculate the average consumption per month
        """
        #avg_consumption = consumed / len(feed column)


    def feed_conversion_ratio():
        """
        Function to calculate how many kg's of food the average animal ate to put on 1kg of body weight.
        """
        #fcr = consumed / ((-1index avg december weight)-(0 index avg january weight))


    
class Report: 
    """
    Class to compile the data from the CattleWeights and CattleFeed classes 
    and create the usable report to be added to the report SHEET
    """
    def remaining_time():
        """
        Function to get an estimate of the time remaining before cattle reach their target weight of 750kg
        """
        #target = (750 - average weight) / average_daily_gain


    def feed_to_target():
        """
        Function to calculate the amount of food required to get the average animal to target weight
        """
        #feed_required = target * Avg FCR
    

    def cost_to_target():
        """
        Function to calculate the cost of getting the animals from their current weights to the target weights of 750kg 
        based on how much food they still require and the cost of that food.
        """
class Main():
    """
    Class to execute the entire aplication. 
    """