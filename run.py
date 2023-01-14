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
    "cow1": [10, 20, 30, 40, 50, 60],
    "cow2": [11, 22, 33, 44, 55, 66],
    "cow3": [15, 25, 35, 45, 55, 65]
}

feed = {
    'jan': 10,
    'feb': 11,
    'nov': 10,
    'dec': 12

}

DEC_INDEX = -1
NOV_INDEX = -2
DEC_DAYS = 31
TARGET_WEIGHT = 750
FEED_COST = 150


class Inputs:
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
    # create one function that calculates total and then pass used and wasted
    #  into it.
    def total_used_feed(self):
        """
        Function to calculate the total amount of feed used over the year.
        """
        # sum(len(feed row))

    def total_wasted_feed(self):
        """
        Function to calculate how much food has been wasted over the year.
        """
        # sum(len(waste row))

    def total_consumed(self):
        """
        Function for the amount of food actually consumed by the cattle over
        the year.
        """
        # consumed = total_used_feed() - total_wasted_feed()

    # possibly use the same on e function that calculates totals and just
    # pass it the feed cost.
    def feed_cost(self):
        """
        Function for the total cost of all the feed for the year. Assuming an
        average cost of feed of £150 per ton.
        """
        # cost = total_used_feed() * 150

    def cost_of_waste(self):
        """
        Function for the total cost of all the wasted food for the year.
        Assuming the same cost of £150 per ton
        """
        # waste = total_wasted_feed() * 150

    def individual_consumption(self):
        """
        Function to calculate the average consumption of each individual
        animal.
        """
        # ind_consumption = consumed / len(row1)

    def average_consumption(self):
        """
        Function to calculate the average consumption per month
        """
        # avg_consumption = consumed / len(feed column)
    
    dec_intake = feed['dec']#feed intake for month of DEC from feed dict
    def feed_conversion_ratio(self, weight, intake):
        """
        Function to calculate how many kg's of food the average animal ate to
        put on 1kg of body weight. The function is divided by 1000 to convert
        the feed from tons to killograms.
        Function works by calculating the difference in weight gain from one
        month to the next (Nov-Dec) and then dividing that by the amount of
        food eaten over the same period.
        """
        fcr = round((((gained_weight) / (dec_intake)) / 1000), 4)
        return fcr
    conversion_ratio = feed_conversion_ratio(gained_weight, dec_intake)

class Report:
    """
    Class to compile the data from the CattleWeights and CattleFeed classes
    and create the usable report to be added to the report SHEET
    """
    def remaining_time(self, target, weight, average):
        """
        Function to get an estimate of the time remaining before cattle reach
        their target weight of 750kg
        Returns number of days estimated to reach target weight
        """
        time_to_target = round(((TARGET_WEIGHT - total_dec_weight) / average_weight_gain))
        return time_to_target
    target_days = remaining_time(TARGET_WEIGHT, total_dec_weight, average_weight_gain)

    def feed_to_target(self, days, ratio):
        """
        Function to calculate the amount of food required to get the average
        animal to target weight
        """
        feed_required = target_days * conversion_ratio
        return feed_required
    feed_to_finish = feed_to_target(target_days, conversion_ratio)

    def cost_to_target(self, feed, cost):
        """
        Function to calculate the cost of getting the animals from their
        current weights to the target weights of 750kg
        based on how much food they still require and the cost of that food.
        Price of food is based on an industry average of £150 per ton.
        Price is divided by 1000 to get the price in kg as the feed required
        is in kg's.
        """
        target_cost = (feed_to_finish * FEED_COST) / 1000
        return target_cost
    finishing_cost = cost_to_target(feed_to_finish, FEED_COST)


class Main():
    """
    Class to execute the entire aplication.
    """
