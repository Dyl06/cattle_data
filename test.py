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


# Ask for username
username = input()

Ask for password
password = input()

# Load database for that 
database = json.load(open(f"{username}.json","r"))

# Check password
if password != database['password']:
	print("Invalid password, bye")
	exit()

# Password okay, load data
cows = database['cows']


# Ask for username
username = input()

Ask for password
password = input()

# Load database for that 
try:
	database = json.load(open(f"{username}.json","r"))
except FileNotFound:
	# user doesnt exist, lets sign them up
	database = {}
	database['passsword'] = password
	database['cows'] = {}
	in_str = json.dumps(database)
	with open(f"{username}.json","w") as fw:
    	fw.write(in_str)

    print("Congrats, you have signed up!")

##

# Check password
if password != database['password']:
	print("Invalid password, bye")
	exit()

# Password okay, load data
cows = database['cows']