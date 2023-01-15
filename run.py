"""
Code comment here
"""
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

cows = {
    "cow1": [10, 20, 30, 40, 150, 260],
    "cow2": [11, 22, 33, 44, 155, 266],
    "cow3": [15, 25, 35, 45, 155, 265]
}

feed = {
    'jan': 1,
    'feb': 1.1,
    'nov': 1,
    'dec': 1.2

}

DEC_INDEX = -1
NOV_INDEX = -2
DEC_DAYS = 31
TARGET_WEIGHT = 750
FEED_COST = 150
DEC_INTAKE = feed['dec']


class SheetInputs:
    """
    Class to call google sheets and process sheets.
    """

    def load_data(self):
        """
        Load data from Google Docs
        """
        cattle_data = SHEET.worksheet('Weight')
        data = cattle_data.get_all_values()
        return data[0]

    def get_user_inputs():
        """
        Get Cattle weights and feed inputs from the user.
        Data will be inputted into a dictionary to be run
        and proccessed by the application.
        Data will be integer values.
        """
        while True:
            print("Please enter your last 3 cattle weights.")
            print("Weights should be whole numbers.")
            print("Example: 168, 204, 320\n")


class UserInputs:
    """
    Class to take user inputs and process them.
    """

    def login():
        """
        Function to input and process the username and password.
        New users get a signup and returning users data is loaded from
        external sheets
        """

    def user_cow_input():
        """
        Function to take the users unique cow id's and last three
        months weights. Data is added to an empty dictionary.
        """

    def user_feed_input():
        """
        Function to take users feed usage for the last three months.
        Data added to an empty dictionary.
        """


class CattleWeights:

    """
    Class to group together all the functions for evaluating the cattle weight
    data from the weight SHEET
    """
    def __init__(self, data, month_index):
        self.data = data
        self.month_index = month_index

    def total_monthly_weight(self, data, month_index):

        """
        Function to calculate the total weight of all the cattle combined for
        each month
        """

        month_total = 0
        for cow, weights in cows.items():
            month_total += weights[month_index]

        print(month_total)
        return month_total

    def average_weight(self):
        """
        Calculate the average weight of an individual animal for each month
        of the year.
        Using the total weight for each month of the year from the
        total_monthly_weight function and then
        dividing it by the number of cattle in this case 20.
        """
        average_weight = DEC_TOTAL / len(cows)
        round_average_weight = round(average_weight, 2)
        print(round_average_weight)
        return round_average_weight

    def average_daily_gain(self):
        """
        Function to calculate the average daily weight gain of the average
        cow in the herd.
        """
        first_adg = (DEC_TOTAL - NOV_TOTAL) / DEC_DAYS
        adg = round(first_adg, 2)
        print(adg)
        return adg


dec_weight = CattleWeights(cows, DEC_INDEX)
DEC_TOTAL = dec_weight.total_monthly_weight(cows, DEC_INDEX)
nov_weight = CattleWeights(cows, NOV_INDEX)
NOV_TOTAL = nov_weight.total_monthly_weight(cows, NOV_INDEX)
avg_weight = dec_weight.average_weight()
daily_gain = dec_weight.average_daily_gain()


class CattleFeed:
    """
    Class to group together all the functions for evaluating the feed data
    from the feed SHEET
    """
    def __init__(self, data):
        self.feed = feed

    def total_used_feed(self, data):
        """
        Function to calculate the total amount of feed used over the year.
        """
        consumption = sum(feed.values())
        print(consumption)
        return consumption

    def feed_cost(self):
        """
        Function for the total cost of all the feed for the year. Assuming an
        average cost of feed of £150 per ton.
        """
        cost = total_consumed * FEED_COST
        print(cost)
        return cost

    def feed_conversion_ratio(self, dec_intake):
        """
        Function to calculate how many kg's of food the average animal ate to
        put on 1kg of body weight. The function is divided by 1000 to convert
        the feed from tons to killograms.
        Function works by calculating the difference in weight gain from one
        month to the next (Nov-Dec) and then dividing that by the amount of
        food eaten over the same period.
        """
        fcr = round((DEC_INTAKE * 1000) / (DEC_TOTAL - NOV_TOTAL), 2)
        print(fcr)
        return fcr



consumption = CattleFeed(feed)
total_consumed = consumption.total_used_feed(feed)
feed_cost = consumption.feed_cost()
conversion_ratio = consumption.feed_conversion_ratio(DEC_INTAKE)


class Report:
    """
    Class to compile the data from the CattleWeights and CattleFeed classes
    and create the usable report to be added to the report SHEET
    """
    print("Please see your Cattle Data Report.\n")
    
    def __init__(self, target, weight, average):
        self.target = target
        self.weight = weight
        self.average = average

    def remaining_time(self, target, weight, average):
        """
        Function to get an estimate of the time remaining before cattle reach
        their target weight of 750kg
        Returns number of days estimated to reach target weight
        """
        time_to_target = round(((TARGET_WEIGHT - avg_weight) / daily_gain))
        print(f"Days left to reach Target Weight: {time_to_target} days\n")
        return time_to_target

    def feed_to_target(self):
        """
        Function to calculate the amount of food required to get the average
        animal to target weight
        """
        feed_required = round((TARGET_WEIGHT - avg_weight) * conversion_ratio)
        print(f"Feed Required to reach target weight: {feed_required} kgs\n")
        return feed_required

    def cost_to_target(self):
        """
        Function to calculate the cost of getting the animals from their
        current weights to the target weights of 750kg
        based on how much food they still require and the cost of that food.
        Price of food is based on an industry average of £150 per ton.
        Price is divided by 1000 to get the price in kg as the feed required
        is in kg's.
        """
        target_cost = round(((target_feed * FEED_COST) / 1000), 2)
        print(f"Cost for each animal to reach target weight: £{target_cost}\n")
        return target_cost


report = Report(TARGET_WEIGHT, DEC_TOTAL, daily_gain)
time_left_report = report.remaining_time(TARGET_WEIGHT, DEC_TOTAL, daily_gain)
target_feed = report.feed_to_target()
cost_target = report.cost_to_target()


class Main():
    """
    Class to execute the entire aplication.
    """
