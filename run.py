"""
Application for a user to enter cattle weight data and feed consumption data
to be processed and have a report returned with usefull insights into
the performance of his herd and costs related.
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

DEC_INDEX = -1
NOV_INDEX = -2
DEC_DAYS = 31
TARGET_WEIGHT = 750
FEED_COST = 150
# Google sheets headings converted to global variables for better readability.
HEADER_COW_NUMBER = "cow number"
HEADER_WEIGHT_ONE = "w1"
HEADER_WEIGHT_TWO = "w2"
HEADER_WEIGHT_THREE = "w3"


class SheetInputs:
    """
    Class to call google sheets and process sheets.
    """

    def load_data(self):
        """
        Load data from Google Docs
        """
        cattle_data = SHEET.worksheet('Weight')
        data = cattle_data.get_all_records()
        new_cows = {}
        for cow in data:
            new_cows[cow[HEADER_COW_NUMBER]] = [
                cow[HEADER_WEIGHT_ONE],
                cow[HEADER_WEIGHT_TWO],
                cow[HEADER_WEIGHT_THREE]]
        return new_cows


class UserInputs:
    """
    Class to take user inputs and process them.
    """

    def user_cow_input(self):
        """
        Function to take the users unique cow id's and last three
        months weights. Data is added to an empty dictionary.
        """
        extra_cows = {}
        new_feed = []
        while True:
            print("Please enter unique cow id")
            cow_id = input("Enter cows unique id here:\n")

            print("Please enter weights for the last three months.")
            print("Weights should correspond to unique cow id.")
            print("Weights should be three numbers separated by commas")
            print("Example: 260, 300, 360")
            cow_weights = input("Enter cattle weights here:\n")

            weight_input = cow_weights.split(",")

            if self.validate_input_data(weight_input):
                print("Weights are valid")
                weight_input_int = [int(x) for x in weight_input]
                extra_cows[cow_id] = weight_input_int
            else:

                continue

            print("Would you like to enter another cow?")
            print("1) Yes")
            print("2) No")
            answer = input()
            if (answer == "1" or answer.lower() == "yes"):
                continue
            else:
                while True:
                    print("Please enter 3 months feed data.")
                    print("Feed should be in tons")
                    print("Feed should be 3 numbers separated by commas.")
                    print("Example 10, 20, 30")

                    food = input("Enter consumption in tons:\n")

                    food_intake = food.split(",")

                    if self.validate_input_data(food_intake):
                        print("Feed values are valid")
                        food_intake_int = [int(x) for x in food_intake]
                        new_feed = food_intake_int
                    else:
                        print("Invalid data. Please try again.")
                        continue

                    break
            break
        return (extra_cows, new_feed)

    def validate_input_data(self, values):
        """
        Function to validate user inputs and return error if inputs provided
        aren't correct.
        """

        try:
            [int(value) for value in values]
            if len(values) != 3:
                raise ValueError(
                    f"Exactly 3 values required, you provided {len(values)}"
                )
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")
            return False
        return True

    def update_worksheet(self, data, worksheet):
        """
        Recieves a dictionary from user inputs the values are then iterated
        over and converted to a list of integers to be inserted
        into a worksheet.
        Update the relevant worksheet with the data provided
        """

        worksheet_to_update = SHEET.worksheet(worksheet)
        for cow_id, weights in data.items():
            row = []
            row.append(cow_id)
            row = row + weights
            worksheet_to_update.append_row(row)


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
        for _, weights in data.items():
            month_total += weights[month_index]

        return month_total

    def average_weight(self, dec_total, data):
        """
        Calculate the average weight of an individual animal for each month
        of the year.
        Using the total weight for each month of the year from the
        total_monthly_weight function and then
        dividing it by the number of cattle.
        """
        average_weight = dec_total / len(data)
        round_average_weight = round(average_weight, 2)
        return round_average_weight

    def average_daily_gain(self, dec_total, nov_total):
        """
        Function to calculate the average daily weight gain of the average
        cow in the herd.
        """
        first_adg = (dec_total - nov_total) / DEC_DAYS
        adg = round(first_adg, 2)
        return adg


class CattleFeed:
    """
    Class to group together all the functions for evaluating the feed data
    from the feed SHEET
    """
    def __init__(self, updated_feed):
        self.feed = updated_feed

    def feed_conversion_ratio(self, dec_intake, dec_total, nov_total):
        """
        Function to calculate how many kg's of food the average animal ate to
        put on 1kg of body weight. The function is divided by 1000 to convert
        the feed from tons to killograms.
        Function works by calculating the difference in weight gain from one
        month to the next (Nov-Dec) and then dividing that by the amount of
        food eaten over the same period.
        """
        fcr = round((dec_intake * 1000) / (dec_total - nov_total), 2)
        return fcr


class Report:
    """
    Class to compile the data from the CattleWeights and CattleFeed classes
    and create the usable report to be added to the report SHEET
    """
    print("Welcome to Cattle Data")
    print("Please follow all instructions below to input your data.")

    def __init__(self, target, weight, average):
        self.target = target
        self.weight = weight
        self.average = average

    def remaining_time(self, target_weight, avg_weight, daily_gain):
        """
        Function to get an estimate of the time remaining before cattle reach
        their target weight of 750kg
        Returns number of days estimated to reach target weight
        """
        time_to_target = round(((target_weight - avg_weight) / daily_gain))
        print(f"Days left to reach Target Weight: {time_to_target} days\n")
        return time_to_target

    def feed_to_target(self, avg_weight, conversion_ratio):
        """
        Function to calculate the amount of food required to get the average
        animal to target weight
        """
        feed_required = round((TARGET_WEIGHT - avg_weight) * conversion_ratio)
        print(f"Feed Required to reach target weight: {feed_required} kgs\n")
        return feed_required

    def cost_to_target(self, target_feed):
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


class Main():
    """
    Class to execute the entire aplication.
    """

    def print_cows(self, cows):
        """
        Prints the list of cows and their weights from google sheets in a
        more readable and user friendly way.
        Used learning material from code institute python essentials to
        replicate this print layout.
        """
        for cow_id, weights in cows.items():
            print(f"Cow ID {cow_id} weights are: {weights}")

    def __init__(self):

        user_inp = SheetInputs()
        cows = user_inp.load_data()
        self.print_cows(cows)

        user_inputs = UserInputs()
        (extra_cows, new_feed) = user_inputs.user_cow_input()
        cows.update(extra_cows)
        feed = new_feed
        dec_intake = feed[-1]
        user_inputs.update_worksheet(extra_cows, "Weight")

        dec_weight = CattleWeights(cows, DEC_INDEX)
        dec_total = dec_weight.total_monthly_weight(cows, DEC_INDEX)
        nov_weight = CattleWeights(cows, NOV_INDEX)
        nov_total = nov_weight.total_monthly_weight(cows, NOV_INDEX)
        avg_weight = dec_weight.average_weight(dec_total, cows)
        daily_gain = dec_weight.average_daily_gain(dec_total, nov_total)

        consumption = CattleFeed(feed)
        conversion_ratio = consumption.feed_conversion_ratio(
            dec_intake,
            dec_total,
            nov_total)

        report = Report(TARGET_WEIGHT, dec_total, daily_gain)
        report.remaining_time(
            TARGET_WEIGHT,
            avg_weight,
            daily_gain)
        target_feed = report.feed_to_target(avg_weight, conversion_ratio)
        report.cost_to_target(target_feed)


main = Main()
