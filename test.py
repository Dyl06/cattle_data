cows = {
    "cow1": [10, 20, 30, 40, 50, 60],
    "cow2": [11, 22, 33, 44, 55, 66],
    "cow3": [15, 25, 35, 45, 55, 65]
}
DEC_INDEX = -1
NOV_INDEX = -2

def total_monthly_weight(data, month_index):
    """
    Function to calculate the total weight of all the cattle combined for
    each month
    """
    month_total = 0
    for cow, weights in data.items():
        month_total += weights[month_index]
        
    print(month_total)
    return month_total


total_dec_weight = total_monthly_weight(cows, DEC_INDEX)
total_nov_weight = total_monthly_weight(cows, NOV_INDEX)

def average_weight(self, total_weight):
    """
    Calculate the average weight of an individual animal for each month
    of the year.
    Using the total weight for each month of the year from the
    total_monthly_weight function and then
    dividing it by the number of cattle in this case 20.
    """
    # average weight = total_weight/ len(row[1]
    average_weight = total_weight / len(cows)
    round_average_weight = round(average_weight, 2)
    print(round_average_weight)
    return round_average_weight


avg_weight = average_weight(cows, total_dec_weight)
DEC_DAYS = 31


def average_daily_gain(self, total_nov_weight):
    """
    Function to calculate the average daily weight gain of the average
    cow in the herd.
    """
    adg = (total_dec_weight - total_nov_weight) / DEC_DAYS
    print(adg)
    return adg


average_daily_gain(total_dec_weight, total_nov_weight)


feed = {
    'jan': 10,
    'feb': 11,
    'march': 12,
    'april': 12

}

def total_used_feed():
        """
        Function to calculate the total amount of feed used over the year.
        """
        #sum(len(feed row))
        consumption = sum(feed.values())
        return consumption


fed = total_used_feed()
print(fed)


def feed_cost(fed):
    """
   Function for the total cost of all the feed for the year. Assuming an
    average cost of feed of £150 per ton.
    """
    cost = fed * 150
    return cost


price = feed_cost(fed)
print(price)


def average_monthly_consumption(fed, feed):
    """
    Function to calculate the average consumption of each individual 
    animal.
    """
    avg_consumption = fed / len(feed)
    print(avg_consumption)


average_monthly_consumption(fed, feed)


def individual_consumption(fed, cow):
    """
    Function to calculate the average consumption of each individual 
    animal per month.
    """
    ind_consumption = fed / len(cows)
    print(ind_consumption)

individual_consumption(fed, cows)