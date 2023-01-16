

cows = {}

cow_id = input("Enter cows unique id here:")

cow_weights = input("Enter cows weights here:")

cows[cow_id] = cow_weights

print(cows)


"""
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
"""