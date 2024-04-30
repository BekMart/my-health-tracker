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
                    validate(height, weight, unit)
                    break
                else:
                    #If user enters anything else, then they will be prompted to re-enter
                    print("Please input either KG for kilograms or LB for pounds")
            except ValueError:
                print("You must input a number")
        except ValueError:
            print("You must input a whole number")
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
        get_data() 
    #If response isn't recognised a message will show and function will repeat
    else:
        print(f"{confirm} is not valid. Please try again.")
        validate(height, weight, unit) 

def display_main_menu(height, weight, unit):
    """
    Menu for user to choose what they want to do with this program
    """
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
        print("Calculate BMI")
    elif choice == "3":
        print("Set Weight Goal")
    elif choice == "4":
        print("Record Data to Spreadsheet")
    elif choice == "5":
        print("Reload Program")
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

intro()
get_data()

