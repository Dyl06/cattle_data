username = input("Username:\n")
password = input("password:\n")


while True:
    username = input("Username:\n")
    password = input("password:\n")





while True:
    print("Pleas enter cattle weights for the last three months.")
    print("Weights should be three numbers separated by commas")
    print("Example: 260, 300, 360")

    weights_data = input("Enter cattle weights here: \n")
    
    weight_input = weights_data.split(",")
    validate_weights_data(weight_input)

    if validate_weights_data(weight_input):
        print("Weights are valid")
        break

return weight_input

def validate_weights_data(values):

    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


