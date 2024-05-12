# My Health Tracker

## Python Project

This website has been designed and built to give users a place to record and track their weight as well as check their BMI and set goals to lose or gain weight over set periods of time.

This project is for educational purposes. The main aim is to build a functional and responsive website using Python.

## [Live Link To Program here.](https://my-health-tracker-92b52c6743f2.herokuapp.com/)

<h1 id="contents">Table of Contents</h1>

- [UX](#UX)
    - [Website Owner Business Goals](#website-owner-goals) 
    - [User Goals](#user-goals)
    - [User Stories](#user-stories)
    - [Structure](#structure)
    - [Surface](#surface)
- [Features](#features)
    - [Features Left To Implement](#features-to-implement)
- [Technology Used](#technology-used)
- [Testing](#testing)
    - [Functionality Testing](#functionality)
    - [Compatibility Testing](#compatibility)
    - [User Stories Testing](#story-testing)
    - [Issues Found](#issues)
    - [Performance Testing](#performance)
    - [Code Validation](#validation)
- [Deployment](#deployment)
- [Credits](#credits)

<h1 id="UX">UX</h1>

<h2 id="website-owner-goals">Website Owner Business Goals</h2>

- To engage users by providing them with a useful website which is easy to use and provides them with something that they want. 
- Ensure that users return as they find the program valuable and enjoyable to use. 
- Users enjoy using the program so they tell others about it and encourage them to use it too and seek out other programs from the creator.

<h2 id="user-goals">User Goals</h2>

### New Users

- Somewhere to record weight details
- Easy to use with lots of feedback
- Somewhere to find out BMI
- Somewhere to set weight goals and be told how much to lose over what period

### Returning Users

- Somewhere familiar and easy to use
- User can record their health journey in one place and keep track of progress
- BMI is calculated on each visit 
- Accurate information provided

<h2 id="user-stories">User Stories</h2>

### As a web designer...

- I want to create an easy to use program with clear feedback to users 
- I want to ensure that all functions work correctly and are responsive at all times
- All calculatins must be accurate

### As a new user...

- I want to easily be able to use the program and all of its functions
- I want to be given accurate information

### As a returning customer...

- I want to keep track of my health in an easy to read format to measure progress
- I want a system that is easy to update and maintain
- I want to be able to access on any device

<h1 id="structure">Structure</h1>

## Process Flow Chart 

![This is a flow chart demonstrating the structure of this website and the process to navigate around it]()

- The client initially inputs their basic height and weight information
- The user is then presented with a menu to choose what they would like to do next
- After each action the user is prompted to press a key to return to the menu and make another choice
- The program is designed to provide lots of feedback to assist the user in navigating around the site and createing a better user experience

## Spreadsheet

![This image shows the spreadhseet where all of the data that the user inputs is stored and tracked]()

- The program is linked to a spreadsheet so if the user wishes to record any of the information, they can select an option from the menu and it'll be recorded here

<h1 id="surface">Surface</h1>

The layout is clear and consistant throughout the program to ensure a professional feel. 
- There is consistent spacing throughout the program and the menu is bordered by lines at the top and underneath. 
- Clear and immediate feedback is given to the user to ensure that they know how to use the program and if anything is input incorrectly, they are informed why and prompted to correct.  

[Back to Contents](#contents)

<h1 id="features">Features</h1>

This program consists of one page which has bas been deployed through Heroku. The program is linked to Google Sheets which allows users to record data from the prpogram using an API.

The program consists of the following features:

### Welcome

- When the program starts, the user is prompted to input their name and there is a welcome message to introduce them to the program. 

### Data Input

- The user is then prompted to input their height and weight information. 
- If the details are input in the incorrect format then an error message appears to clearly state why and the input fiels will reappear to enable the user to try again. 

### Validation 

- Before proceeding to the main menu, there is feedback for the user to confirm that all the details entered are correct. 
- If not, they will be directed back to the begining to re-enter the correct data. 

### Main Menu

- The main menu has a border and title. 
- It consists of 6 options which are clearly labelled by numbers.
- There is a prompt after the menu for the user to make a selection between 1-6.
- Feedback is given if an invalid selection is made. 

### Convert Weight

- This function does a calculation to change the mesaurement from kilograms to pounds or vice versa.
- Feedback is given to the user to inform them of the alternative measurement. 

### Calculate BMI

- In order to perform this caluclation, the measurement must be converted to kilograms. 
- The calculation is then completed using the initial data that the user has input.
- Feedback is given to the user stating what their calculated BMI is.
- There is also feedback to inform user of what their BMI catagory is based on information from the NHS website. 

### Set Weight Goals

- The user will be asked what their target goal weight is.
- The surplus weight will be converted to pounds.
- Feedback will be given to user to inform them of the weight difference. If this is negative then feedback will be how much weight to gain and if positive then how much to lose. 
- The user will then be prompted the input the date by which they would like to reach this goal. 
- Feedback will be given if this date is in the past or is not input in the correct format. 
- Once we have all this information, a calculation will be made and feedback will be given in a readable sentance to tell users, how much weight they would need to lose/gain each week in order to reach their weight goals. 

### Record Details

- There is an option for users to record their data onto a Google Sheets page.
- The data recorded is the current date, height and weight, goal weight, total weight lose target in pounds, target date, how many pounds the user needs to lose per week, number of weeks and their calculated BMI.
- If the data has yet to be calculated then the user will be redirected to the correct menu option to obtain the data first.
- If we have all the necessary details, the data will be pulled across and update the spreadsheet accordingly. 
- Feedback is given to let the user know that the spreadsheet has been updated successfully. 

### Return to Menu

- After making a menu selection and the action is complete, there is a message for the user to press any key in order to return to the main menu.

### Reset Program

- This clears all of the data that has been obtained and restarts the program from the begining.

### Exit Program

- This option closes the program.
- Feedback is given to tell the user that this has been done. 

<h2 id="features-to-implement">Features Left To Implement</h2>

- I would like to have had different tabs within the Google spreadsheet so that if different users enter their details, it would filter to seperate tabs within the spreadsheet. 
- I could also add an option where the program calculates a users healthy BMI and information on how to best reach that in a safe and healthy manner. 