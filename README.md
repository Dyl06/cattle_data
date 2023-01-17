![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Dyl06,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

# Cattle Data

Cattle data is a python terminal application for feedlot users looking to fatten cattle to the industry standard 750kg weight to be sent to market.
Users are able to input their cattle weights and feed consumption and the application processes that data and returns a report telling the user how long until cattle are likely to reach that target weight and how many kilograms of food they will require to reach that target and at what cost to the user.

## How it works

Upon opening the application users will be presented with an input allowing them to enter an individual cow id followed by the three most recent weights of that animal, based on accepted industry standard for monthly weighing.

Once they have entered the first animal they are able to repeat the process until they have entered either their entire herd or all the animals they wish to analyse. Analysis of just one animal is also possible.

Once user has inputted cattle data the application requests the feed consumption from the same three months. Feed inputs are taken in tons and specific month data is not required from the user. Instead average calculations in the application are based on a month length of 31Days.

Once they submit that data the application processes that data and returns a report to the user with:
- the time left before animals have reached the target weight of 750kg, 
- the amount of food each animal requires to achieve that weight and 
- the cost of that food based on an industry average of £150 per ton.

This information will then be uploaded to an external worksheet using gspread so the users data is available in a excel format.  

## Existing Features

Users are greeted with a detailed list of instructions as to what information they are required to input into the terminal.
![Terminal display requesting user inputs](images/Screenshot%202023-01-17%20at%2003.30.37.png)




## Future Features

In the future the application will allow a signup with username and password for added user security. 

Once the user has an account they can then update existing cows on a month by month basis and also delete cows once they have achieved target weights and are no longer in the feedlot. 

Reports can be generated then from month to month with an email or other alert sent to the user based on their preference. 

In future users could also be able to alter feed prices and include a more detailed feed ingredients and prices to allow them to compare prices of different feeds and calculate profit based on those calculations. 

Actual month and year data can be included in future features so long term users can start to build a comprehensive database that allows for long term trends and data reviews. 

Users want an application that gives them valuable data taken from the weights of their cattle and the amount of feed those cattle eat.

The cows individual data can then be manually entered into the application along with their monthly weights for the year.
After which  


## Code References

- https://www.mygreatlearning.com/blog/python-dictionary-append/
- https://bobbyhadz.com/blog/python-add-user-input-to-dictionary
I used these links to see how to add multiple values to a single key in a dictionary. 

https://docs.gspread.org/en/latest/user-guide.html#getting-all-values-from-a-worksheet-as-a-list-of-dictionaries
I used this guide to help me to link my application to sheets in gspread. I also used the love_sandwiches code along project as a reference to help me link my sheets.

The rest of my code came from learning material on code institute lessons as well as refreshers from google on specific syntax and methods. 