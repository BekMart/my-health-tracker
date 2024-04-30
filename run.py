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
            try: 
                #User to enter figures for their weight. If this is not a number then it'll throw an error
                weight = float(input("\nEnter your weight: "))
                #User to input either KG or LB to represent the unit of measurment for their weight
                unit = input("Is that in kilograms or pounds? (KG/LB)\n").upper()
                if unit == "KG" or unit == "LB":
                    break
                else:
                    #If user enters anything else, then they will be prompted to re-enter
                    print("Please input either KG for kilograms or LB for pounds")
            except ValueError:
                print("You must input a number")
        except ValueError:
            print("You must input a whole number")

    print(f"\nYour height is {height}CM and your current weight is {weight}{unit}.")
    return height, weight, unit

intro()
get_data()

