#!/usr/bin/env python3
import random
from tkinter import *

# global constants, now modified by entries and sliders
LENGTH = 10
LOWERS = 1
UPPERS = 1
NUMBERS = 1
PUNCTUATIONS = 1

KPS = 1000000000 # keys per second used in cracking the password, 1 billion default


root = Tk() # make a window called root
root.geometry('600x820') # size of the window
root.title ("TJM Password Analyzer")

# function for copy to clipboard button
def copy_to_clipboard(strongPass):
    # Clear the clipboard
	root.clipboard_clear()
	# Copy to clipboard
	root.clipboard_append(strongPass)


# output to bottom of gui when a strong password is entered
# v1.3: ogColor parameter added for text color
def output_strong(rules_met, originalTime, password, ogColor):
    #print('Strong output')
    #print('Rules met: ' + str(rules_met))
    #print('Orinal time to crack: ' + originalTime)
    #print('Password: ' + password)

    # strong output rules met label
    lbl_os_rulesmet = Label(bottomFrame, text='This password meets ' + str(rules_met) + ' out of ' + str(rules_met) + ' rules.')
    lbl_os_rulesmet.grid(row=0, column=0, columnspan=2, pady=20)

    # v1.4: If the password meets all requirements, but still is less than a year to crack,
    # suggest that the user increases password requirements
    if ogColor == 'green':
        # very strong pass label
        lbl_veryStrong = Label(bottomFrame, text='You have a very strong password!')
        lbl_veryStrong.grid(row=1, column=0, columnspan=2, pady=20)
    else:
        lbl_increaseReqs = Label(bottomFrame, text='Your password meets all requirements but is still weak. Try increasing requirements!')
        lbl_increaseReqs.grid(row=1, column=0, columnspan=2, pady=20)

    # time to crack label
    lbl_timeToCrack = Label(bottomFrame, text='Approximate time to crack:')
    lbl_timeToCrack.grid(row=2, column=0, sticky=E)

    #original time label
    lbl_originalTime = Label(bottomFrame, text= originalTime, fg=ogColor)
    lbl_originalTime.grid(row=2, column=1, sticky=W)

    # copy to clipboard button
    btn_Copy = Button(bottomFrame, text='Copy strong password to clipboard', height=2, width=40, command=copy_to_clipboard(password))
    btn_Copy.grid(row=3, column=0, columnspan=2, pady=20)


# output to bottom of gui when a weak password is entered
# v1.3: ogColor and sugColor added for text colors
def output_weak(rules_met, originalTime, suggestedPass, suggestionTime, ogColor, sugColor, how_many_rules):
    #print('weak output')
    #print('Rules met: ' + str(rules_met))
    #print('Original time to crack: ' + originalTime)
    #print('Suggested pass: ' + suggestedPass)
    #print('Suggestion time: ' + suggestionTime)

    # weak output rules met label
    lbl_ow_rulesmet = Label(bottomFrame, text='This password meets ' + str(rules_met) + ' out of ' + str(how_many_rules) + ' rules.')
    lbl_ow_rulesmet.grid(row=0, column=0, columnspan=2, pady=20)

    # time to crack label
    lbl_timeToCrack = Label(bottomFrame, text='Approximate time to crack:')
    lbl_timeToCrack.grid(row=1, column=0, sticky=E)

    #original time label
    lbl_originalTime = Label(bottomFrame, text= originalTime, fg=ogColor)
    lbl_originalTime.grid(row=1, column=1, sticky=W)

    # label frame for suggested pass
    lf_suggestion = LabelFrame(bottomFrame, text='Try using this stronger password')
    lf_suggestion.grid(row=2, column=0, columnspan=2, pady=20)

    # textbox containing suggested pass
    text_suggestedPass = Text(lf_suggestion, height=1, width=50)
    text_suggestedPass.insert('end', suggestedPass)
    text_suggestedPass.config(state='disabled') # user cannot edit
    text_suggestedPass.pack(padx=20, pady=20)

    # suggetion time to crack label
    lbl_sug_timeToCrack = Label(bottomFrame, text='Approximate time to crack:')
    lbl_sug_timeToCrack.grid(row=3, column=0, sticky=E)

    # suggestion time label
    lbl_sugTime = Label(bottomFrame, text= suggestionTime, fg=sugColor)
    lbl_sugTime.grid(row=3, column=1, sticky=W)

    # copy to clipboard button
    btn_Copy = Button(bottomFrame, text='Copy strong password to clipboard', height=2, width=40, command=copy_to_clipboard(suggestedPass))
    btn_Copy.grid(row=4, column=0, columnspan=2, pady=20)


def analyzer(password): # function to check if the password meets the rules
    rules_met = 0 # variable to track how many rules are met
    lowercase = 0 # variable to count number of lowercase letters
    lower_chars = 'abcdefghijklmnopqrstuvwxyz' # variable containing lower chars
    uppercase = 0 # variable to count number of uppercase letters
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # variable containing upper chars
    number = 0 # variable to count number of numbers
    number_chars = '1234567890' # variable containing numbers
    punctuation = 0 # variable to count number of punctuation characters

    # create boolean variable for each rule
    length_met = False
    lowercase_met = False
    uppercase_met = False
    numbers_met = False
    punc_met = False

    # loop through each character in the password, and check for each type of character
    for c in password:
        if c in lower_chars: # if c is lower
            lowercase += 1 # increment lowercase
        elif c in upper_chars: # if c is upper
            uppercase += 1 # increment uppercase
        elif c in number_chars: # if c is a number
            number += 1 # increment number
        else: # if none of the above, c must be punctuation
            punctuation += 1

    # test the rules
    # v1.3: get value of entries to use as rules
    LENGTH = int(entry_minLength.get())
    LOWERS = int(entry_lowers.get())
    UPPERS = int(entry_uppers.get())
    NUMBERS = int(entry_numbers.get())
    PUNCTUATIONS = int(entry_punc.get())

    # v1.4: If any requirement is 0, they don't count towards total number of rules
    how_many_rules = 0
    if LENGTH > 0:
        how_many_rules += 1
    if LOWERS > 0:
        how_many_rules += 1
    if UPPERS > 0:
        how_many_rules += 1
    if NUMBERS > 0:
        how_many_rules += 1
    if PUNCTUATIONS > 0:
        how_many_rules += 1

    # v1.4: In order for a rule to be met, the rule must also not be 0
    if len(password) >= LENGTH and LENGTH != 0:
        rules_met += 1
        length_met = True
    
    if lowercase >= LOWERS and LOWERS != 0:
        rules_met += 1
        lowercase_met = True
    
    if uppercase >= UPPERS and UPPERS != 0:
        rules_met += 1
        uppercase_met = True
    
    if number >= NUMBERS and NUMBERS != 0:
        rules_met += 1
        numbers_met = True
    
    if punctuation >= PUNCTUATIONS and PUNCTUATIONS != 0:
        rules_met += 1
        punc_met = True

    # call a function that will make the checkboxes by each rule
    # red x for not met, green check for met
    # pass in the boolean values for each rule
    checkboxes(length_met, lowercase_met, uppercase_met, numbers_met, punc_met)

    # call the time_to_crack function, the function will return the time of the original pass
    # as a string
    originalTime = time_to_crack(password)[0]
    ogColor = time_to_crack(password)[1]

    # if all rules are met, call a function that creates the output section of the gui
    # variables passed in: rules_met, originalTime, password
    if rules_met == how_many_rules:  # v1.4: rules_met should equal how_many_rules if all rules are met
        output_strong(rules_met, originalTime, password, ogColor)
    # if not every rule is met, prepare to call the suggestion function
    else:
        # initialize variables to pass into suggestion function
        need_length = 0
        need_lower = 0
        need_upper = 0
        need_number = 0
        need_punc = 0

        # set the variables to proper value
        if len(password) < LENGTH:
            need_length = LENGTH - len(password)
        if lowercase < LOWERS:
            need_lower = LOWERS - lowercase
        if uppercase < UPPERS:
            need_upper = UPPERS - uppercase
        if number < NUMBERS:
            need_number = NUMBERS - number
        if punctuation < PUNCTUATIONS:
            need_punc = PUNCTUATIONS - punctuation
        
        # call the suggestion function when not all rules are met, it returns the string
        suggestedPass = suggestion(password, need_length, need_lower, need_upper, need_number, need_punc)

        # now call time to crack to return time to crack of suggested pass
        suggestionTime = time_to_crack(suggestedPass)[0]
        sugColor = time_to_crack(suggestedPass)[1]

        # finally, pass all the needed args into the function to create the weak output
        output_weak(rules_met, originalTime, suggestedPass, suggestionTime, ogColor, sugColor, how_many_rules)  
        # v1.4: add how_many_rules parameter


def suggestion(password,  need_length, need_lower, need_upper, need_number, need_punc):
    #print('suggestion')
    lower_chars = 'abcdefghijklmnopqrstuvwxyz' # variable containing lower chars
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # variable containing upper chars
    number_chars = '1234567890' # variable containing numbers
    symbols = '''~`! @#$%^&*()_-+={[}]|\:;"'<,>.?/''' # variable containing symbols
    all_chars = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`! @#$%^&*()_-+={[}]|\:;"'<,>.?/'''


    chars_added = 0 # keep track of how many chars added for length purposes
    # start adding lower chars
    while need_lower > 0:
        c = random.choice(lower_chars) # choose a random lower char
        password += c # add the char to the password
        chars_added += 1 # increment chars_added
        need_lower -= 1 # decrease need_lower
    # now add upper chars
    while need_upper > 0:
        c = random.choice(upper_chars) # choose a random upper char
        password += c # add the char to password
        chars_added += 1 # increment chars_added
        need_upper -= 1 # decrease need_upper
    # add numbers if needed
    while need_number > 0:
        c = random.choice(number_chars) # choose a random number
        password += c # add the char to password
        chars_added += 1 # increment chars_added
        need_number -= 1 # decrease need_number
    # add punctuation if needed
    while need_punc > 0:
        c = random.choice(symbols) # choose a symbol
        password += c # add the char to password
        chars_added += 1 # increment chars_added
        need_punc -= 1 # decrease need_punc

    # Check if more length is still needed, and add chars if it is
    need_length -= chars_added # first decrease needed length by how many chars already added
    # add more length while needed
    while need_length > 0:
        c = random.choice(all_chars) # choose a random character of any type
        password += c # add the char to password
        need_length -= 1 # decrease need_length

    # return the new and improved password, the string will be saved as suggestedPass
    return password


# the function that estimates time to crack a password, returns a string with time and unit
def time_to_crack(password):
    # Seconds = Combinations/KeysPerSecond
    # first we must calculate the number of combinations
    # combinations = (Password Type)^(Password Length)
    # password type is complexity (total possible value for each digit)
    # calculate complexity
    complexity = 0 # number of possible characters contained in a digit
    lower_chars = 'abcdefghijklmnopqrstuvwxyz' # variable containing lower chars
    has_lower = False
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # variable containing upper chars
    has_upper = False
    number_chars = '1234567890' # variable containing numbers
    has_number = False
    symbols = '''~`! @#$%^&*()_-+={[}]|\:;"'<,>.?/''' # variable containing symbols
    has_symbol = False

    # loop through character in password, check if password has lower, upper, numbers, punctuation
    for c in password:
        if c in lower_chars:
            has_lower = True
        elif c in upper_chars:
            has_upper = True
        elif c in number_chars:
            has_number = True
        elif c in symbols:
            has_symbol = True

    # calculate complexity based on what the password contains
    if has_lower == True:
        complexity += 26 # 26 lowercase letters
    if has_upper == True:
        complexity += 26 # 26 uppercase letters
    if has_number == True:
        complexity += 10 # 10 numbers
    if has_symbol == True:
        complexity += 33 # 33 symbols

    # combinations = complexity ^ length
    combinations = complexity ** len(password)

    # Seconds = Combinations/KeysPerSecond
    seconds = combinations / KPS

    # convert to bigger unit depending on how large the number is
    # create a string to return with correct unit
    # v1.3: add Color parameters for each unit and return those as well
    # seconds = red
    # minutes = orange red
    # hours = DarkOrange1
    # days = chartreuse3
    # years = green
    # v1.4: If over 10 million years, use scientific notation
    if seconds >= 315360000000000:
        years = seconds / 31536000
        scientific_years = "{:2e}".format(years)
        return_str = str(scientific_years) + ' years'
        color = 'green'
        return (return_str, color)
    elif seconds >= 31536000: # if more than a year of seconds
        years = seconds / 31536000 # calculate years
        limited_years = "{:.2f}".format(years) #rounding years ##new variable
        # create the return string
        return_str = str(limited_years) + ' years' #inserted new variable
        color = 'green'
        return (return_str, color)
    elif seconds >= 86400: # if more than a day of seconds
        days = seconds / 86400 # calcualte days
        limited_days = "{:.2f}".format(days) #rounding days ##new variable
        return_str = str(limited_days) + ' days' #inserted new variable
        color = 'chartreuse3'
        return (return_str, color)
    elif seconds >= 3600: # if more than an hour of seconds
        hours = seconds / 3600 # calculate hours 
        limited_hours = "{:.2f}".format(hours)
        return_str = str(limited_hours) + ' hours'
        color = 'DarkOrange1'
        return (return_str, color)
    elif seconds >= 60: # if more than a minute of seconds
        minutes = seconds / 60
        limited_minutes = "{:.2f}".format(minutes)
        return_str = str(limited_minutes) + ' minutes'
        color = 'orange red'
        return (return_str, color)
    else:
        limited_seconds = "{:.2f}".format(seconds) #making new variable that rounds
        return_str = str(limited_seconds) + ' seconds'
        color = 'red'
        return (return_str, color)


# this function will create the checkboxes indicating which rules are met by an input password
def checkboxes(length_met, lowerercase_met, uppercase_met, numbers_met, punc_met):
    
    # first uncheck everything
    check_length.deselect()
    check_lowers.deselect()
    check_uppers.deselect()
    check_numbers.deselect()
    check_punc.deselect()

    # check boxes for met rules
    if length_met:
        check_length.select()
    if lowerercase_met:
        check_lowers.select()
    if uppercase_met:
        check_uppers.select()
    if numbers_met:
        check_numbers.select()
    if punc_met:
        check_punc.select()


# analyze button function
def analyze():
    # get the value entered in entry box
    entered_pass = entry_password.get()
    # print(entered_pass)

    # clear any output already written to bottomFrame
    for widget in bottomFrame.winfo_children():
        widget.destroy()

    # call the analyzer function
    analyzer(entered_pass)


# reset button function
def reset():
    # clear the entered password
    entry_password.delete(0, END)

    # reset checkboxes
    check_length.deselect()
    check_lowers.deselect()
    check_uppers.deselect()
    check_numbers.deselect()
    check_punc.deselect()

    # clear any output already written to bottomFrame
    for widget in bottomFrame.winfo_children():
        widget.destroy()

    #print('Reset')
    
    # Reset requirement entries
    #entry_minLength.delete(0, END)
    #entry_minLength.insert(0, 10)
    # Trying to reset the entries leads to an error, so reset sliders instead
    slider_minLength.set(LENGTH)
    slider_lowers.set(LOWERS)
    slider_uppers.set(UPPERS)
    slider_numbers.set(NUMBERS)
    slider_punc.set(PUNCTUATIONS)

def correct(inp):
    if inp.isdigit():
        return True
    elif inp == "":
        return True
    elif inp.isspace(): #resticting spaces
        return False
    else:
        return False


# v1.4: Add new frames in top row and format with grid to balance out checkbuttons
# NWFrame
NWFrame = Frame(root, width=220, height= 100)
NWFrame.grid(row=0, column=0)
# NEFrame
NEFrame = Frame(root, width=180, height= 100)
NEFrame.grid(row=0, column=2)

# divide screen vertically with 3 frames
topFrame = Frame(root)
topFrame.grid(row=0, column=1)
middleFrame = Frame(root)
middleFrame.grid(row=1, column=0, columnspan=3)
bottomFrame = Frame(root)
bottomFrame.grid(row=2, column=0, columnspan=3)

# first label
passwordRequirements = Label(topFrame, text='PASSWORD REQUIREMENTS')
passwordRequirements.grid(row=0, column=1, columnspan=2, pady=10)
    
# length label
lbl_minLength = Label(topFrame, text='Minimum Length:')
lbl_minLength.grid(row=1, column=1)

# create min length variable for entry and slider
var_minLength = IntVar(value=10)
# length entry
entry_minLength = Entry(topFrame, width=5, textvariable=var_minLength)
entry_minLength.grid(row=1, column=2)
reg = root.register(correct)
entry_minLength.config(validate='key',validatecommand=(reg,'%P'))
# length slider
slider_minLength = Scale(topFrame, from_=1, to=50, orient=HORIZONTAL, variable=var_minLength, showvalue=0)
slider_minLength.grid(row=2, column=1, columnspan=2, pady=8)

# lowers variable
var_lowers = IntVar(value=1)
# lowers label
lbl_lowers = Label(topFrame, text='Lowercase Characters:')
lbl_lowers.grid(row=3, column=1)
# lowers entry
entry_lowers = Entry(topFrame, width=5, textvariable=var_lowers)
entry_lowers.grid(row=3, column=2)
entry_lowers.config(validate='key',validatecommand=(reg,'%P'))
# lowers slider
slider_lowers = Scale(topFrame, from_=0, to=10, orient=HORIZONTAL, variable=var_lowers, showvalue=0)
slider_lowers.grid(row=4, column=1, columnspan=2, pady=8)

# uppers var
var_uppers = IntVar(value=1)
# uppers label
lbl_uppers = Label(topFrame, text='Uppercase Characters:')
lbl_uppers.grid(row=5, column=1)
# uppers entry
entry_uppers = Entry(topFrame, width=5, textvariable=var_uppers)
entry_uppers.grid(row=5, column=2)
entry_uppers.config(validate='key',validatecommand=(reg,'%P'))
# uppers slider
slider_uppers = Scale(topFrame, from_=0, to=10, orient=HORIZONTAL, variable=var_uppers, showvalue=0)
slider_uppers.grid(row=6, column=1, columnspan=2, pady=8)

# numbers var
var_numbers = IntVar(value=1)
# numbers label
lbl_numbers = Label(topFrame, text='Number Characters:')
lbl_numbers.grid(row=7, column=1)
# numbers entry
entry_numbers = Entry(topFrame, width=5, textvariable=var_numbers)
entry_numbers.grid(row=7, column=2)
entry_numbers.config(validate='key',validatecommand=(reg,'%P'))
# numbers slider
slider_numbers = Scale(topFrame, from_=0, to=10, orient=HORIZONTAL, variable=var_numbers, showvalue=0)
slider_numbers.grid(row=8, column=1, columnspan=2, pady=8)

# punc var
var_punc = IntVar(value=1)
# punc label
lbl_punc = Label(topFrame, text='Symbols Characters:') #changing to symbols
lbl_punc.grid(row=9, column=1)
# punc entry
entry_punc = Entry(topFrame, width=5, textvariable=var_punc)
entry_punc.grid(row=9, column=2)
entry_punc.config(validate='key',validatecommand=(reg,'%P'))
# punc slider
slider_punc = Scale(topFrame, from_=0, to=10, orient=HORIZONTAL, variable=var_punc, showvalue=0)
slider_punc.grid(row=10, column=1, columnspan=2, pady=8)


# in the middle frame, create the password entry field
lf_enterPass = LabelFrame(middleFrame, text='Enter your password')
lf_enterPass.pack(pady=20)

# make entry box where password is entered inside label frame
entry_password = Entry(lf_enterPass, width=50)
entry_password.pack(padx=20, pady=20)


# create the analyze button
btn_analyze = Button(middleFrame, text='Analyze', height=3, width=20, command=analyze)
btn_analyze.pack(side=LEFT)

# create the reset button
btn_reset = Button(middleFrame, text='Reset', height=3, width=20, command=reset)
btn_reset.pack(side=RIGHT)

# v1.4: create the empty checkboxes here
check_length = Checkbutton(topFrame, state=DISABLED)
check_length.grid(row=1, column=3, padx=10)

check_lowers = Checkbutton(topFrame, state=DISABLED)
check_lowers.grid(row=3, column=3, padx=10)

check_uppers = Checkbutton(topFrame, state=DISABLED)
check_uppers.grid(row=5, column=3, padx=10)

check_numbers = Checkbutton(topFrame, state=DISABLED)
check_numbers.grid(row=7, column=3, padx=10)

check_punc = Checkbutton(topFrame, state=DISABLED)
check_punc.grid(row=9, column=3, padx=10)


root.mainloop()