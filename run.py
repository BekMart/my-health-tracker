from datetime import datetime, timedelta, date
import math

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
SHEET = GSPREAD_CLIENT.open('MyHealthTracker')

#Global variables
height = 0
weight = 0
unit = ""
client_data = []
rounded_bmi = 0

def intro():
    """
    Get name of user and introduce program
    """
    name = input("\nEnter your name: ").title()
    print(f"Hello {name}. Welcome to your health tracker. Please enter your height and weight information to begin..")
    return name

def get_data():
    """
    Get height and weight data from user to enable next actions
    """
    while True:
        try:
            #User to enter figures for their height in CM. If this is not an integer then it'll throw an error
            height = int(input("\nEnter your height in CM: "))
            break
        except ValueError:
            print("You must input a whole number only")
            continue  # Continue the loop to prompt for height again

    while True:
        try: 
            #User to enter figures for their weight. If this is not a number then it'll throw an error
            weight = float(input("\nEnter your weight: "))
            break
        except ValueError:
            print("You must input a number only")
            continue  # Continue the loop to prompt for weight again

    while True:
        #User to input either KG or LB to represent the unit of measurment for their weight
        unit = input("Is that in kilograms or pounds? (KG/LB)\n").upper()
        if unit == "KG" or unit == "LB":
            validate(height, weight, unit)
        else:
            #If user enters anything else, then they will be prompted to re-enter
            print(f"{unit} is an invalid response. Please input either KG for kilograms or LB for pounds\n")
            
    return height, weight, unit

def validate(height, weight, unit):
    """
    Check with user that details are correct before proceeding to main menu
    """
    #If user is happy that their detailsd are correct, proceed to main menu
    confirm = input(f"\nYour height is {height}CM and your current weight is {weight}{unit}.\nIs that correct? (Y/N)").upper()
    if confirm == "Y":
        print("\nOk great! Now that we have your details, what would you like to do next?")
        display_main_menu(height, weight, unit)  
    #If user hasn't entered details correctly, they can re-enter
    elif confirm == "N":
        print("No problem, let's try again!")
        height, weight, unit = get_data() 
    #If response isn't recognised a message will show and function will repeat
    else:
        print(f"{confirm} is not valid. Please try again.")
        validate(height, weight, unit) 

def display_main_menu(height, weight, unit):
    """
    Menu for user to choose what they want to do with this program
    """
    #This makes the following variables global so they can be used in various functions and there values can be reset
    global client_data
    if client_data is None:
        client_data = []

    global rounded_bmi
    if rounded_bmi is None:
        rounded_bmi = 0

    print("-------------------------------")
    MENU_OPTIONS = {
        "1" : "Convert weight (imperial/metric)",
        "2" : "Calculate BMI",
        "3" : "Set weight goal",
        "4" : "Record your details",
        "5" : "Reset program",
        "6" : "Exit Program"
    }
    #Print menu to terminal as a dictionary with a prompt for user to make a selection
    display_optins = print("MENU OPTIONS:\n")
    for key, value in MENU_OPTIONS.items():
        print(f"{key}. {value}")
    print(display_optins)
    print("\n-------------------------------")

    choice = input("Please pick an option 1-6: \n")
    #Depending on which choice the user makes a function will be called
    if choice == "1":
        convert_weight(height, weight, unit)
    elif choice == "2":
        calculate_bmi(height, weight, unit)
    elif choice == "3":
        client_data = set_weight_goals(height, weight, unit)
    elif choice == "4":
        update_health_spreadsheet(height, weight, unit)
    elif choice == "5":
        reset_program(height, weight, unit)
    elif choice == "6": 
        #This will exit the program
        print("Exiting program.. See you again soon!")
        exit()
    else:
        #If user enters anything thatr isn't 1-6
        print("Ooops that wasn't an option. Try again..")
        display_main_menu(height, weight, unit)

def convert_weight(height, weight, unit):
    """
    Converts weight between KG and LB
    """
    print("Convert weight (imperial/metric):")
    #If unit was originally in KG then it'll convert to LB and print to terminal
    if unit == "KG":
        weight = round(weight, 1) * 2.205
        unit = "LB"
        print(f"\nYour weight is: {round(weight,1)}{unit}")
    #If unit was originally in LB then it'll convert to KG and print to terminal    
    elif unit == "LB":
        weight = round(weight, 1) / 2.205
        unit = "KG"
        print(f"\nYour weight is: {round(weight,1)}{unit}")
    #Menu displayed after function called so user can make another selection
    display_main_menu(height, weight, unit)
    return weight, unit  

def calculate_bmi(height, weight, unit):
    """
    Calculate users BMI using the data they have already input
    """
    global rounded_bmi
    print("Calculate BMI:")

    #Convert weight to kg and round to 1 decimal place to make calculation
    if unit == "LB":
        weight_kg = round(weight, 1) / 2.205
    elif unit == "KG":
        weight_kg = round(weight, 1)
    
    #Convert height to meters
    height_m = height / 100
    #Height squared
    height_sq = height_m * height_m

    #BMI = weight(kg) / height squared(m)
    bmi = weight_kg / height_sq
    #rounded to 1 decimal place
    rounded_bmi = round(bmi, 1)

    print(f"\nYour BMI is {rounded_bmi}")

    #The terminal will then print data relating to weight catagory
    if rounded_bmi <= 18.4:
        print("According to the NHS website you are considered underweight")
    elif rounded_bmi <= 24.9:
        print("According to the NHS website you are considered healthy")
    elif rounded_bmi <= 29.9:
        print("According to the NHS website you are considered overweight")
    elif rounded_bmi > 30:
        print("According to the NHS website you are considered obese")
    else:
        print("Sorry we do not recognise your response")

    #Menu displayed after function called so user can make another selection
    display_main_menu(height, weight, unit)
    return rounded_bmi

def set_weight_goals(height, weight, unit):
    """
    Allows user to calculate how many LB they need to lose to meet their weight goal
    """
    global client_data
    print("Set weight goal:")

    while True:
        try:
            # Call function to get goal_weight and goal_weight_unit values
            goal_weight, goal_weight_unit = get_weight_and_unit("\nWhat weight do you want to get to?", "KG or LB")

            # Converting weight to pounds to calculate surplus weight
            weight_lb = weight * 2.205 if unit == "KG" else weight
            goal_weight_lb = goal_weight * 2.205 if goal_weight_unit == "KG" else goal_weight
            surplus_weight_lb = weight_lb - goal_weight_lb

            # Message to user to inform them of surplus weight
            print(f"You want to lose {round(surplus_weight_lb, 1)} LB")
            break

        # Print the specific error message if invalid value is entered
        except ValueError as e:
            print(e)  

    # Use datetime to calculate todays date and convert into string to update spreadsheet
    today = datetime.now().date()
    date_str = today.strftime("%Y-%m-%d")

    while True:
        try:
            # This is where user is to input the date they want to get to their goal weight by and this is converted to a string to update spreadsheet
            target_date = datetime.strptime(input("\nWhen do you want to reach your goal weight by? (YYYY-MM-DD) "), "%Y-%m-%d").date()
            target_date_str = target_date.strftime("%Y-%m-%d")
            break
        except ValueError:
            # Error message printed if invalid format is entered
            print("Invalid target date format. Please use YYYY-MM-DD.")

    # Calculate how many weeks between target_date and now
    timeframe = target_date - today
    timeframe_weeks = math.floor(timeframe.days / 7)

    # This calculates how many pounds the user should lose each week to reach their goal
    goal = surplus_weight_lb / timeframe_weeks
    rounded_goal = round(goal, 1)

    # Compile client data (list comprehension)
    client_data = [date_str, height, round(weight_lb,1), round(goal_weight_lb,1), round(surplus_weight_lb,1), target_date_str, rounded_goal, timeframe_weeks]

    # Display results to user in a readable sentance 
    print(f"\nTo reach {goal_weight}{goal_weight_unit} by {target_date}, lose {rounded_goal} LB each week for {timeframe_weeks} weeks.")
    
    #Menu displayed after function called so user can make another selection
    display_main_menu(height, weight, unit)

    # Return client_data so that this can be updated to spreadsheet
    return client_data

def get_weight_and_unit(prompt, unit_message):
    """
    Prompts user for weight and unit, validates input, and returns both values.
    """
    while True:
        try:
            goal_weight = float(input(prompt + " "))
            goal_weight_unit = input(f"Is that in {unit_message}? \n").upper()
            if goal_weight_unit not in ("KG", "LB"):
                raise ValueError(f"{goal_weight_unit} is an invalid response. Please input either KG or LB")
            return goal_weight, goal_weight_unit
        except ValueError as e:
            print(e)  # Print the specific error message

def update_health_spreadsheet(height, weight, unit):
    """
    Update spreadsheet with data from user inputs
    """
    #Use the following global variables within this function
    global client_data
    global rounded_bmi

    #If user hasn't set weight goals, then they will be redirected to the function to do this
    if client_data == []:
        print("You need to set weight goals first..")
        client_data = set_weight_goals(height, weight, unit)
    
    #If user hasn't calculated BMI, then they will be directed to the correct function
    if rounded_bmi == 0:
        print("You need to calculate your BMI first..")
        calculate_bmi(height, weight, unit)

    #This add the BMI value to the client_data list
    client_data.append(rounded_bmi)

    print("Updating spreadsheet..")

    #Input client_data into spreadsheet
    health_spreadsheet = SHEET.worksheet("client1")
    health_spreadsheet.append_row(client_data) 

    print("\nThank you for your information. The spreadsheet has been updated successfully!")

    #Menu displayed after function called so user can make another selection
    display_main_menu(height, weight, unit)

def reset_program(height, weight, unit):
    """
    This will reset all the settings and restart the program
    """
    #Use the following global variables within this function
    global client_data
    global rounded_bmi

    print("Restarting Program..")
    
    #Reset all of the data 
    height = 0
    weight = 0
    unit = ""
    client_data = []
    rounded_bmi = 0

    #Restart program
    intro()
    height, weight, unit = get_data()

    #Retrun reset values of the following variables 
    return height, weight, unit, client_data, rounded_bmi

intro()
height, weight, unit = get_data()