cows = {
    "cow1": [10, 20, 30, 40, 50, 60],
    "cow2": [11, 22, 33, 44, 55, 66],
    "cow3": [15, 25, 35, 45, 55, 65]
}


def total_monthly_weight(data, month_index):
    """
    Function to calculate the total weight of all the cattle combined for
    each month
    """
    month_total = 0
    for cow, weights in data.items():
        month_total += weights[month_index]
        
    print(month_total)
    

JAN_INDEX = 0
feb_index = 1
mar_index = 2
apr_index = 3
may_index = 4
june_index = 5
july_index = 6
aug_index = 7
sept_index = 8
oct_index = 9
nov_index = 10
dec_index = 11

total_monthly_weight(cows, JAN_INDEX)
total_monthly_weight(cows, feb_index)
total_monthly_weight(cows, mar_index)
total_monthly_weight(cows, apr_index)
total_monthly_weight(cows, may_index)
total_monthly_weight(cows, june_index)

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
