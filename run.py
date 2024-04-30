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
    #User to enter figures for their height and weight values
    height = int(input("\nEnter your height in CM: "))
    weight = int(input("\nEnter your weight: "))
            
    #User to input either KG or LB to represent the unit of measurment for their weight
    unit = input("Is that in kilograms or pounds? (KG/LB)\n").upper()

    print(f"\nYour height is {height}CM and your current weight is {weight}{unit}.")
    return height, weight, unit

intro()
get_data()