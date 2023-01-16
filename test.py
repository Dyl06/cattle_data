def user_cow_input():
    """
    Function to take the users unique cow id's and last three
    months weights. Data is added to an empty dictionary.
    """
    extra_cows = {}
    new_feed = {}
    while True:
        print("Please enter unique cow id")
        print("Please enter weights for the last three months.")
        print("Weights should correspond to unique cow id.")
        print("Weights should be three numbers separated by commas")
        print("Example: 260, 300, 360")

        cow_id = input("Enter cows unique id here:\n")

        cow_weights = input("Enter cattle weights here:\n")
            
        weight_input = cow_weights.split(",")
            
        if validate_weights_data(weight_input):
            print("Weights are valid")
            extra_cows[cow_id] = weight_input
        else:
            print("Invalid data. Please try again.\n")
     
        print("Would you like to enter another cow?")
        print("1) Yes")
        print("2) No")
        answer = input()
        if (answer == "1" or answer.lower() == "yes"):
            continue
        else:
            print("Please enter one month and one feed value at a time.")
            print("Feed should be in tons")
            print("Enter data for 3 consecutive months.")

            for i in range(3):
                month = input("Enter the month:\n")
                food = input("Enter consumption in tons:\n")

                new_feed[month] = food

            break

    return (extra_cows, new_feed)

def validate_weights_data(values):
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
        except ValueError as e:
            return False
        return True


(extra_cows, new_feed) = user_cow_input()
print(extra_cows)
print(new_feed)

