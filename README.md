# Fullstack-Cyber-Security-Capstone-Project-2021
Final Project Version info

poc_1.0.py

First version of the program.
Features include: 
-Global constants that are adjustable for an organizations rule requirements.
-Rules function that displays the rules to the user.
-Analyzer function that displays which rules an input password meets.
-Basic menu to view rules, exit program, or take input.




mvp_2.0.py

Second version of the program
Changes from last version:
-Added a time_to_crack function that estimates the time a password will take to crack with brute force. The function uses a basic combinations=complexity^length equation, then calculates seconds to crack using the equation seconds=combinations/KeysPerSecond. Default KPS is one billion. Large answers are converted to larger units.
-Main menu now takes a number as input to execute a chosen function.



mvp_2.1.py

Third Version
Changes:
-Added a suggestion function that adds characters to strengthen a password that is given to the analyzer function. The suggestion function takes multiple parameters to determine what characters are needed to add to the password and adds to it accordingly.



mvp_2.2.py

Fourth version
Changes:
-Move where the time_to_crack function is called, so that instead of being accessed independently in the menu, the function is executed when a password is analyzed and again when a stronger password is suggested.



gui_1.0.py

First gui version
-set up the basic look of gui
-includes sliders and entry boxes for rules, but they have no function yet
-includes entry box to input password
-analyze button simply prints the entry to terminal
-reset button clears entry field



gui_1.1_makegui.py

Second gui version
-Added functionality to analyze button
-Analyze button now correctly analyzes the input, and outputs to the terminal
    -how many rules are met
    -time to crack the input password
    -suggests a stronger password if necessary
    -time to crack suggested password
-The gui is now created within a makegui function
-The makegui function contains the analyze button, where analysis functions are called

    What to work on moving to next version:
    -output_strong and output_weak functions build the correct gui elements instead of terminal output
    -checkboxes function create the correct gui items
    Issues to solve:
    -these functions exist outside the makegui function, so how will they interact with the gui?
    -Can these functions be moved within makegui and still work?


gui_1.2_restructure.py

Third gui version
-Restructured the way the gui is made, it no longer is called in a function
-output_strong and output_weak now correctly display gui widgets in the output section of the gui
-The reset button now works, it removes all widgets in output section
-Analyze button also removes all widgets before making new ones
-Copy to clipboard button works as intended

    What to work on next:
    -password requirement entry boxes will change the rules
    -checkboxes show up when analyzing to show which rules are met
    -time to crack shows in colors based on unit of time
    -sliders?


gui_1.3.py

Fourth gui version
-Password requirement sliders and entry boxes now work together and share a value
-Analyze function now gets values from sliders/entrys for the password requirements
-In the output section, the color of the text varies based on the unit of time! green is good

    What to work on next:
    -If a requirement is set to 0, change max requirements to be less than 5
    -ex.:'This password meets 1 out of 3 rules'
    -Some sort of input validation for password requirement entries (disallow non-number characters)
    -Format time output to display to 2 decimal places (or some number of places)
    -Spaces in the password, what do we want to do with that
    -checkboxes!


gui_1.3.2.py

-Time to crack output now displays to two decimal places
-Restricted input in requirement to only numbers
-Minimum requirement now 1 instead of 0 for lowers, uppers, numbers, punc

    What to work on:
    -Fix bug with really long numbers (make large numbers scientific notation again)
    -Restrict spaces in password entry (this one has been tough)
    -CHECKBOXESSSSSs


gui_1.4.py

-Numbers over 10 million years now get formatted with scientific notation
-Added NW and NE frames to balance out checkboxes and format base frames with grid instead of pack
-Checkboxes now work, showing which rules are met by the input. Reset button resets all checks.
-Removed all print statements. (no longer needed, everything gui!)
-Non-length rules can be lowered to 0 again
-If a requirement is set to 0, it will not count towards the number of rules counted
-If the entered password meets all requirements, but still takes less than a year to crack, suggest that the user increase requirements
-If more length is needed for the suggestion, a random character of any type is suggested (previously it only gave numbers)

    What to work on:
    -Restrict spaces in password entry
        -If we can figure that out, make the suggestion function no longer able to add spaces (and adjust symbols in general)
        -Also minor adjustment to time_to_crack complexity calculation
    -Any other stretch goals?
