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

# Global variables
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
    print(f"Hello {name}. Welcome to your health tracker.")
    print("Please enter your height and weight information to begin..")
    return name


def get_data():
    """
    Get height and weight data from user to enable next actions
    """
    while True:
        try:
            # User to enter figures for their height in CM.
            height = int(input("\nEnter your height in CM: "))
            break
        except ValueError:
            # If height is not an integer then it'll throw an error
            print("You must input a whole number only")
            # Continue the loop to prompt for height again
            continue

    while True:
        try:
            # User to enter figures for their weight.
            weight = float(input("\nEnter your weight: "))
            break
        except ValueError:
            # If this is not a number then it'll throw an error
            print("You must input a number only")
            # Continue the loop to prompt for weight again
            continue

    while True:
        # User to input either KG or LB for the unit of weight measurment
        unit = input("Is that in kilograms or pounds? (KG/LB)\n").upper()
        if unit == "KG" or unit == "LB":
            validate(height, weight, unit)
        else:
            # If user enters anything else, they will be prompted to re-enter
            print(f"{unit} is an invalid response.")
            print("Please input either KG for kilograms or LB for pounds\n")
    return height, weight, unit


def validate(height, weight, unit):
    """
    Check with user that details are correct before proceeding to main menu
    """
    # If user is happy that their details are correct, proceed to main menu
    print(f"\nYour height is {height}CM and your weight is {weight}{unit}.")
    confirm = input("\nIs that correct? (Y/N)").upper()
    if confirm == "Y":
        print("\nOk great! Now that we have your details,")
        print("what would you like to do next?")
        display_main_menu(height, weight, unit)
    # If user hasn't entered details correctly, they can re-enter
    elif confirm == "N":
        print("No problem, let's try again!")
        height, weight, unit = get_data()
    # If response isn't recognised a message will show and function will repeat
    else:
        print(f"{confirm} is not valid. Please try again.")
        validate(height, weight, unit)


def display_main_menu(height, weight, unit):
    """
    Menu for user to choose what they want to do with this program
    """
    # This makes the following variables global so they can be used in various
    # functions and there values can be reset
    global client_data
    if client_data is None:
        client_data = []

    global rounded_bmi
    if rounded_bmi is None:
        rounded_bmi = 0

    print("-" * 30)
    MENU_OPTIONS = {
        "1": "Convert weight (imperial/metric)",
        "2": "Calculate BMI",
        "3": "Set weight goal",
        "4": "Record your details",
        "5": "Reset program",
        "6": "Exit Program"
    }

    # Print menu options as dictionary and promt user to make a selection
    print("MENU OPTIONS:\n")
    for key, value in MENU_OPTIONS.items():
        print(f"{key}. {value}")
    print("-" * 30)

    choice = input("\nPlease pick an option 1-6: ")
    # Depending on which choice the user makes a function will be called
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
        # This will exit the program
        print("Exiting program.. See you again soon!")
        print("-" * 30)
        exit()
    else:
        # If user enters anything thatr isn't 1-6
        print("Ooops that wasn't an option. Try again..")
        display_main_menu(height, weight, unit)


def return_to_menu(height, weight, unit):
    """
    Called at the end of each option to get user to enter a key
    which will return them to main menu
    """
    while True:
        user_input = input("Press any key to return to menu: \n")
        # Check if anything in input/or just enter pressed
        if user_input or user_input == "":
            # Menu displayed so user can make another selection
            display_main_menu(height, weight, unit)
            break  # Exit the loop if user presses a key


def convert_weight(height, weight, unit):
    """
    Converts weight between KG and LB
    """
    print("Convert weight (imperial/metric):")
    # If unit is in KG, it'll convert to LB and print to terminal
    if unit == "KG":
        weight = round(weight, 1) * 2.205
        unit = "LB"
        print(f"\nYour weight is: {round(weight,1)}{unit}")
    # If unit is in LB, it'll convert to KG and print to terminal
    elif unit == "LB":
        weight = round(weight, 1) / 2.205
        unit = "KG"
        print(f"\nYour weight is: {round(weight,1)}{unit}")
    print("-" * 30)

    return_to_menu(height, weight, unit)
    return weight, unit


def calculate_bmi(height, weight, unit):
    """
    Calculate users BMI using the data they have already input
    """
    global rounded_bmi
    print("Calculate BMI:")

    # Convert weight to kg and round to 1 decimal place to make calculation
    if unit == "LB":
        weight_kg = round(weight, 1) / 2.205
    elif unit == "KG":
        weight_kg = round(weight, 1)

    # Convert height to meters
    height_m = height / 100
    # Height squared
    height_sq = height_m * height_m

    # BMI = weight(kg) / height squared(m)
    bmi = weight_kg / height_sq
    # Rounded to 1 decimal place
    rounded_bmi = round(bmi, 1)

    print(f"\nYour BMI is {rounded_bmi}")

    # The terminal will then print data relating to weight catagory
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
    print("-" * 30)

    return_to_menu(height, weight, unit)
    return rounded_bmi


def set_weight_goals(height, weight, unit):
    """
    Calculates how many LB the user needs to lose to meet their weight goal
    """
    global client_data
    print("Set weight goal:")

    while True:
        try:
            # Call function to get goal_weight and goal_weight_unit values
            goal_weight, goal_weight_unit = get_weight_and_unit(
                "\nWhat weight do you want to get to?", "KG or LB"
                )

            # Converting weight to pounds to calculate surplus weight
            weight_lb = weight * 2.205 if unit == "KG" else weight
            goal_weight_lb = (
                goal_weight * 2.205
                if goal_weight_unit == "KG"
                else goal_weight
                )
            surplus_weight_lb = weight_lb - goal_weight_lb

            # Message displays how much to lose (if surplus weight >= 0)
            if surplus_weight_lb >= 0:
                print(f"You want to lose {round(surplus_weight_lb, 1)} LB")
                break
            else:
                # Message displays how much to gain (if surplus weight < 0)
                # Convert surplus weight to positive for weight gain
                weight_to_gain = round(abs(surplus_weight_lb), 1)
                print(f"You want to gain {weight_to_gain} LB")
                break

        # Print the specific error message if invalid value is entered
        except ValueError as e:
            print(e)

    # Use datetime to calculate todays date
    today = datetime.now().date()
    # Convert into string to update the spreadsheet
    date_str = today.strftime("%Y-%m-%d")

    while True:
        try:
            # User inputs the date they want to get to their goal weight by
            print("\nWhen do you want to reach your goal weight by?")
            target_date_str = input("(YYYY-MM-DD)\n")
            target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()

            # Check if target date is in the past (before today)
            if target_date < today:
                raise ValueError("PastDateError")  # Exception for past date

            # This is converted to a string to update the spreadsheet
            target_date_str = target_date.strftime("%Y-%m-%d")
            break

        except ValueError as e:
            # Handle specific errors
            if str(e) == "PastDateError":
                print("Date can't be in the past. Please enter a future date.")
            else:
                print("Invalid target date format. Please use YYYY-MM-DD.")

    # Calculate how many weeks between target_date and now
    timeframe = target_date - today
    timeframe_weeks = math.floor(timeframe.days / 7)

    # Calculates how many LB the user should lose each week to reach their goal
    goal = surplus_weight_lb / timeframe_weeks
    rounded_goal = round(goal, 1)

    # Compile client data
    client_data = [
        date_str, height, round(weight_lb, 1),
        round(goal_weight_lb, 1), round(surplus_weight_lb, 1),
        target_date_str, rounded_goal, timeframe_weeks
        ]

    # Display results to user in a readable sentance
    print(f"\nTo reach {goal_weight}{goal_weight_unit} by {target_date},")
    if surplus_weight_lb >= 0:
        print(f"lose {rounded_goal}LB each week for {timeframe_weeks} weeks.")
    else:
        print(f"gain {weight_to_gain}LB each week for{timeframe_weeks} weeks.")
    print("-" * 30)

    return_to_menu(height, weight, unit)

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
                raise ValueError(f"{goal_weight_unit} is an invalid response.")
                print("Please input either KG or LB")
            return goal_weight, goal_weight_unit
        except ValueError as e:
            # Print the specific error message
            print(e)


def update_health_spreadsheet(height, weight, unit):
    """
    Update spreadsheet with data from user inputs
    """
    # Use the following global variables within this function
    global client_data
    global rounded_bmi

    # If user hasn't set weight goals, they will be directed to that function
    if client_data == []:
        print("You need to set weight goals first..")
        client_data = set_weight_goals(height, weight, unit)

    # If user hasn't calculated BMI, they will be directed to that function
    if rounded_bmi == 0:
        print("You need to calculate your BMI first..")
        calculate_bmi(height, weight, unit)

    # This add the BMI value to the client_data list
    client_data.append(rounded_bmi)

    print("Updating spreadsheet..")

    # Input client_data into spreadsheet
    health_spreadsheet = SHEET.worksheet("client1")
    health_spreadsheet.append_row(client_data)

    print("\nThank you for your information.")
    print("The spreadsheet has been updated successfully!")
    print("-" * 30)

    return_to_menu(height, weight, unit)


def reset_program(height, weight, unit):
    """
    This will reset all the settings and restart the program
    """
    # Use the following global variables within this function
    global client_data
    global rounded_bmi

    print("Restarting Program..")

    # Reset all of the data
    height = 0
    weight = 0
    unit = ""
    client_data = []
    rounded_bmi = 0

    # Restart program
    intro()
    height, weight, unit = get_data()

    # Retrun reset values of the following variables
    return height, weight, unit, client_data, rounded_bmi


intro()
height, weight, unit = get_data()
