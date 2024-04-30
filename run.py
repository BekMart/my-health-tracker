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

intro()