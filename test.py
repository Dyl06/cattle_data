cows = {
    "cow1": [10,20,30,40,50,60],
    "cow2": [11,22,33,44,55,66],
    "cow3": [15,25,35,45,55,65]
}


def total_monthly_weight():
    """
    Function to calculate the total weight of all the cattle combined for
    each month
    """
    month_total = 0
    for cow,weights in cows.items():
        month_total += weights[0]
        
    return month_total


total_monthly_weight()


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