# My Health Tracker 

## Python Project 

This website has been designed and built to give users a place to record and track their weight as well as check their BMI and set goals to lose or gain weight over set periods of time. 

This project is for educational purposes. The main aim is to build a functional and responsive website using Python. 

## [Live Link to Program here.](https://my-health-tracker-92b52c6743f2.herokuapp.com/) 

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

- Somewhere to record weight details.
- Easy to use with lots of feedback.
- Somewhere to find out BMI.
- Somewhere to set weight goals and be told how much to lose over what period.

### Returning Users 

- Somewhere familiar and easy to use.
- User can record their health journey in one place and keep track of progress.
- BMI is calculated on each visit.
- Accurate information provided.

<h2 id="user-stories">User Stories</h2> 

### As a web designer... 

- I want to create an easy-to-use program with clear feedback to users.
- I want to ensure that all functions work correctly and are responsive at all times.
- All calculations must be accurate.

### As a new user... 

- I want to easily be able to use the program and all of its functions.
- I want to be given accurate information.

### As a returning customer... 

- I want to keep track of my health in an easy-to-read format to measure my progress.
- I want a system that is easy to update and maintain.
- I want to be able to access the program on any device.

<h1 id="structure">Structure</h1> 

## Process Flow Chart  

![This is a flow chart demonstrating the structure of this website and the process to navigate around it.][flow-chart] 

- The client initially inputs their basic height and weight information.
- The user is then presented with a menu to choose what they would like to do next.
- After each action the user is prompted to press a key to return to the menu and make another choice.
- The program is designed to provide lots of feedback to assist the user in navigating around the site and creating a better user experience.

## Spreadsheet 

![This image shows the spreadsheet where all of the data that the user inputs is stored and tracked.][spreadsheet] 

- The program is linked to a spreadsheet so if the user wishes to record any of the information, they can select an option from the menu, and it'll be recorded here.

<h1 id="surface">Surface</h1> 

The layout is clear and consistent throughout the program to ensure a professional feel. 
- I have used some basic CSS to style the background and features of the program to make it more aesthetically pleasing. 
- There is consistent spacing throughout the program and the menu is bordered by lines at the top and underneath.  
- Clear and immediate feedback is given to the user to ensure that they know how to use the program and if anything is input incorrectly, they are informed why and prompted to correct.  

[Back to Contents](#contents) 

<h1 id="features">Features</h1> 

This program consists of one page which has been deployed through Heroku. The program is linked to Google Sheets which allows users to record data from the program using an API. 

The program consists of the following features: 

### Welcome 

- When the program starts, the user is prompted to input their name and there is a welcome message to introduce them to the program.  
- If no name is entered, then feedback is given to prompt user to input this. 

![Screenshot of introduction to the program. User is asked for their name and a welcome message is displayed.][welcome] 

### Data Input 

- The user is then prompted to input their height and weight information.  
- If the details are input in an incorrect format or a negative figure is entered, then an error message appears to clearly state why, and the questions will reappear to enable the user to try again.  

![User is asked for their height and weight details. There is a demonstration of all the error messages that will appear if invalid data is entered.][get-data] 

### Validation  

- Before proceeding to the main menu, there is feedback for the user to confirm that all the details entered are correct.  
- If not, they will be directed back to the beginning to re-enter the correct data.  

![A message displays the information obtained and asked the user if this is correct. If the user enters anything other than y or n then a message appears, and the question is repeated. If user clicked n, then the user will be directed back to the beginning of the function to re-enter the data.][validate] 

### Main Menu 

- The main menu has a border and title.  
- It consists of 6 options which are clearly labelled by numbers. 
- There is a prompt after the menu for the user to make a selection between 1-6.
- Feedback is given if an invalid selection is made.  

![After the user confirms that the data collected is correct, the menu is displayed. The menu gives the user 6 options of what to do next and they are prompted to choose an option by entering 1-6.][menu] 

### Convert Weight 

- This function does a calculation to change the measurement from kilograms to pounds or vice versa. 
- Feedback is given to the user to inform them of the alternative measurement.  

![When the user chooses option 1, to convert the weight between metric and imperial, a heading is displayed to confirm this and then the weight is displayed in the alternative measurement. Then the user is prompted to press any button to reload the main menu. If they choose option 1 again, the process will repeat, and the original weight and measurement entered is displayed.][convert] 

### Calculate BMI 

- In order to perform this calculation, the measurement must be converted to kilograms.  
- The calculation is then completed using the initial data that the user has input. 
- Feedback is given to the user stating what their calculated BMI is. 
- There is also feedback to inform users of what their BMI category is based on information from the NHS website.  

![Option 2 is to calculate BMI, when this is selected, a heading is displayed followed by a sentence letting the user know what their calculated BMI is and which category they are in, considering the NHS guidelines.][bmi] 

### Set Weight Goals 

- The user will be asked what their target goal weight is. 
- If a negative figure or invalid value is entered then the user will be asked to re-enter.
- The surplus weight will be converted to pounds. 
- Feedback will be given to users to inform them of the weight difference. If this is negative, then feedback will be how much weight to gain and if positive then how much to lose.  
- The user will then be prompted to input the date by which they would like to reach this goal.  
- Feedback will be given if this date is in the past or is not input in the correct format.  
- Once we have all this information, a calculation will be made, and feedback will be given in a readable sentence to tell users how much weight they would need to lose or gain each week in order to reach their weight goals.  

![Option 3 is to set weight goals. When this is selected, the user will be asked what weight they would like to reach. If a negative figure is entered or if an invalid value is entered, then feedback will inform them why and the question will be asked again.][set-goals-1] 

![The user will also be asked when they would like to reach this goal by. If a date in the past is entered or an invalid format, then feedback will instruct the user how to rectify this and ask the question again. When all the details are established, the user will receive feedback stating how much weight they need to lose or gain each week in order to reach their desired goal.][set-goals-2] 

### Record Details 

- There is an option for users to record their data onto a Google Sheets page. 
- The data recorded is the current date, height and weight, goal weight, total weight lose target in pounds, target date, how many pounds the user needs to lose per week, number of weeks and their calculated BMI. 
- If the data has yet to be calculated then the user will be redirected to the correct menu option to obtain the data first. 
- If we have all the necessary details, the data will be pulled across and update the spreadsheet accordingly.  
- Feedback is given to let the user know that the spreadsheet has been updated successfully.  

![This image demonstrates that when option 4 is selected without having collected the data needed, it will redirect the user to the correct option to complete this before being able to record. It also demonstrates that if a weight goal is set, which is greater than their current weight, the user is informed how much weight to gain each week instead of losing each week.][gain] 

![If all the necessary data is available when option 4 is selected, to record your details, the screen displays a message 'Updating spreadsheet...' and then 'Thank you for your information. The spreadsheet has been updated successfully!' when the spreadsheet has been updated.][update] 

### Return to Menu 

- After making a menu selection and the action is complete, there is a message for the user to press any key in order to return to the main menu. 

### Reset Program 

- This clears all of the data that has been obtained and restarts the program from the beginning. 

![When the user chooses option 5, to reset the program, the program will reset all the data received and reload the program from the beginning, by firstly requesting the user's name.][reset] 

### Exit Program 

- This option closes the program. 
- Feedback is given to tell the user that this has been done.  

![When option 6 is selected, to exit the program a message is displayed 'Exiting program.. See you again soon!' and the program stops running.][exit] 

<h2 id="features-to-implement">Features Left To Implement</h2> 

- I would like to have had different tabs within the Google spreadsheet so that if different users enter their details, it would filter to separate tabs within the spreadsheet.  
- I could also add an option where the program calculates a user's healthy BMI and information on how to best reach that in a safe and healthy manner.  

[Back to Contents](#contents) 

<h1 id="technology-used">Technology Used</h1> 

### Python 

- Python is the language used to create the entire program. 

### CSS 

- I added some basic CSS to style the program. 

### Git Pod 

- This is the development hosting platform which was used to create the website. 

### GitHub 

- This is the software hosting platform which was used to keep the project in a remote location. 

### Heroku 

- The platform used to deploy the website online. 

### Google Sheets 

- Used to record data that is obtained from the program. 

### Google API 

- Used to link the program to the Google spreadsheet. 

### Google Gemini 

- AI used to assist me in debugging elements in my code. 

### CI Python Linter 

- Python validator used to ensure that my code met the standards required 

### Figma 

- Used to create a process flow chart for my project 

[Back to Contents](#contents) 

<h1 id="testing">Testing</h1> 

<h2 id="functionality">Functionality Testing</h2> 

Below is a table to show all of the functions of the program, their expected outcomes and whether or not they work as intended. 

| Action | Expected Result | Result | 
| --- | --- | ---| 
| Run program | Program launches successfully | Pass | 
| Input data | Client inputs data and this is stored in global variables | Pass | 
| Validation of data | If data provided is in the wrong format, then feedback will be given, and the user prompted to re-enter | Pass | 
| Menu | Menu is displayed, and user can make a selection 1-6 | Pass | 
| Convert weight | Weight can be converted between kilograms and pounds | Pass | 
| Calculate BMI | BMI calculated, and output displayed to tell the user what their BMI is and which category they are in, according to the NHS website | Pass | 
| Set weight goals | User inputs target weight and date so that program can display how many pounds they need to lose or gain over how many weeks | Pass | 
| Record details | Details pulled across to Google spreadsheet to record progress | Pass | 
| More info needed | If more information is needed to record data, the user is redirected to the necessary options to resolve this | Pass | 
| Return to menu | After each option in the menu is completed, a message to press any key is displayed to return to the main menu | Pass | 
| Restart program | All obtained data is cleared, and the program is restarted from the beginning | Pass | 
| Exit Program | Program closed | Pass | 

The above has all been tested manually via VS code and Python shell. 

<h2 id="compatibility">Compatibility Testing</h2> 

This program has been tested in Chrome, Firefox and Safari web browsers: 
- There were no issues found when the program was run on either Chrome or Firefox. 
- In Safari, the program loaded but no other actions were possible making me think that some of the software is not compatible with this browser.  

I tested the website on the following hardware devices: 
- MacBook Pro 
    - This works fine, with no issues. 
- Galaxy S20 
    - The program loads, however, when I enter any data into the input field, it displays all of the inputs concatenated when new data is entered. 
- iPhone 13 
    - The program loads but no other actions are possible. 

<h2 id="story-testing">User Stories Testing</h2> 

### As a web designer... 

- I want to create an easy-to-use program with clear feedback to users.
    - At each step of this program, there is feedback which tells the user: 
        - What to expect/what to do next.
        - If they have entered any details incorrectly, feedback will explain why and prompt them to re-enter correctly. 
- I want to ensure that all functions work correctly and are responsive at all times.
    - Tests have been carried out on all functions within the program and they work as intended. 
- All calculations must be accurate.
    - All calculations have been tested and are accurate, they have been rounded to a single decimal place.  
    - Calculations include: 
        - Converting between metric to imperial.
        - BMI calculations.
        - Calculations which relay how much weight people need to lose/gain over what period of time to reach their goals.

### As a new user... 

- I want to easily be able to use the program and all of its functions.
    - This is achieved by the feedback being very clear and informative throughout. 
- I want to be given accurate information.
    - All the information which is output has been tested for accuracy. 

### As a returning customer... 

- I want to keep track of my health in an easy-to-read format to measure progress.
    - The user is able to update their data after each use to a spreadsheet, where they can see their progress over time. 
- I want a system that is easy to update and maintain.
    - It is a simple system where the user just needs to enter their current height and weight details and then select the menu option to record data. 
    - If the user hasn't input any weight goals or checked their BMI, they will be re-directed to these options automatically before being able to record their data, as this is all information to be recorded.  
- I want to be able to access on any device.
    - It seems that this program is not well suited to being on mobile devices.  

<h2 id="issues">Issues Found</h2> 

### Solved Bugs 

- When I first created the main menu, another line was added displaying 'None' after the last option within the dictionary.  
    - This was because I originally created the MENU_OPTIONS variable, which contained the menu content, but also created a variable named display_options to print the MENU_OPTIONS and called both of these.  
    - Since print doesn't return anything, the variable display_options was assigned 'None', which is why it was displayed at the end of the menu. 
    - To rectify this, I erased the display options variable all together and just printed the MENU_OPTIONS. 

- When a user inputs data in the get_data function, if something was entered in the wrong format, it would tell the user, but the while loop would return them to the beginning of the whole function opposed to repeating the current question.  
    - I had originally nested the try statements within the function which was within a while loop.  
    - I separated the function into three while loops so that each input section is dealt with separately and if the input isn't it the correct format, feedback will be given to the user and they will be returned to the question that they were on, rather than starting at the beginning of the function each time.  

- When the user chooses the option to set weight goals, a variable named client_data is created. This variable holds all of the data which we want to transfer to the google spreadsheet in order to record and track their health information. I was finding that the values that were obtained from this function were not updating in the variable globally.  
    - This issue was resolved by making client_data a global variable, which I declared in each function that it was associated with and returned the value of it when I need its value to be updated. (In set_weight_goals and rest_program functions) 

### Unsolved bugs 

- I want the program to work on all devices including mobile, however, in many of my tests it seemed that the program wasn't compatible with many of the devices or software.  

<h2 id="performance">Performance Testing</h2> 

### Lighthouse 

- I completed an audit through Chrome Devtools using the Lighthouse program.  
- The performance value sometimes varies. 
- The results were as follows when last checked: 

![Image of lighthouse results showing Performance at 100, Accessibility at 100, Best Practice at 100 and SEO at 100.][lighthouse] 

<h2 id="validation">Code Validation</h2> 

### Python 

I used [CI Python Linter](https://pep8ci.herokuapp.com/) to validate my Python code.  
- I had some E501 errors where my code was too long, so I reduced these to fit within the guidelines. 
- I also saw some E231 errors because there was unnecessary whitespace present within my code.  
- All of the errors were rectified and now the code is all valid.  

![This image shows the code passing through validator, showing no errors.][validator] 

[Back to Contents](#contents) 

<h1 id="deployment">Deployment</h1> 

The site was created in Git pod and deployed to Heroku via GitHub. The steps to deploy were as follows: 
- Firstly, I needed to create a list of dependencies that our project needs to run, as Heroku will need to install these also.  
    - To obtain this list type 'pip3 freeze > requirements.txt' into the Git pod terminal and the list will appear in requirements.txt file 
- I created a Heroku account
- I clicked 'Create new app' on the Heroku dashboard 
    - I added the app name and selected my region, then clicked 'Create app' 
- On the app dashboard I went to "Settings"
    - In settings, I went to 'Config vars' and added the following: 
        - Key: CREDS / Value: (Copy and paste contents of CREDS.json from Git pod)
        - Key: PORT / Value: 8000
    - Then to the 'Buildpacks' section within settings and clicked "Add build pack" 
        - I added the python buildpack first followed by the nodejs buildpack (ensuring they were in the correct order)
- I left settings by clicking the "Deploy" tab
    - I selected GitHub as the deployment method 
    - I input the repository name to search for it and clicked 'Connect'
    - In the manual deploy section, I checked that it was set to 'main' and pressed 'Deploy branch' 
    - Once the program had been deployed a message was displayed "Your app was successfully deployed"  
    - I then clicked 'View' to view the deployed version 

Visit the live website [here.](https://my-health-tracker-92b52c6743f2.herokuapp.com/) 

[Back to Contents](#contents) 

<h1 id="credits">Credits</h1> 

### Code Institute

- Provided the deployment terminal.

### Google Gemini 

- I used [Google Gemini AI](https://gemini.google.com/app/dcd808a4f3bdce46) to assist me in correcting and refining my code throughout.

### CI Tutor support 

- I had some assistance from the Code Institute tutor support when trying to fix my bug relating to how to make my variables global so I could update and access their values throughout the program.

### NHS website 

- I got information on how to calculate BMI [here](https://www.nhs.uk/health-assessment-tools/calculate-your-body-mass-index/calculate-bmi-for-adults) and information relating to BMI and what the different categories are [here](https://www.nhs.uk/health-assessment-tools/calculate-your-body-mass-index/calculate-bmi-for-adults/result).

[Back to Contents](#contents) 

 
[flow-chart]: assets/process-flow-chart.png 
[spreadsheet]: assets/spreadsheet.png 
[lighthouse]: assets/lighthouse.png 
[validator]: assets/validator.png
[welcome]: assets/welcome.png 
[get-data]: assets/get-data.png 
[validate]: assets/validate-n.png 
[menu]: assets/menu.png 
[convert]: assets/convert.png 
[bmi]: assets/bmi.png 
[set-goals-1]: assets/set-goal-1.png 
[set-goals-2]: assets/set-goal-2.png 
[update]: assets/update.png 
[reset]: assets/restart.png 
[exit]: assets/exit.png 
[gain]: assets/gain.png 
