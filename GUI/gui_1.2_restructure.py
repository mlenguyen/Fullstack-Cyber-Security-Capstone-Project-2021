#!/usr/bin/env python3
import random
from tkinter import *

# global constants, these will eventually work with the entry fields and sliders
LENGTH = 10
LOWERS = 1
UPPERS = 1
NUMBERS = 1
PUNCTUATIONS = 1
KPS = 1000000000 # keys per second used in cracking the password, 1 billion default


root = Tk()
root.geometry('600x800')


# function for copy to clipboard button
def copy_to_clipboard(strongPass):
    # Clear the clipboard
	root.clipboard_clear()
	# Copy to clipboard
	root.clipboard_append(strongPass)


# output to bottom of gui when a strong password is entered
def output_strong(rules_met, originalTime, password):
    print('Strong output')
    print('Rules met: ' + str(rules_met))
    print('Orinal time to crack: ' + originalTime)
    print('Password: ' + password)

    # strong output rules met label
    lbl_os_rulesmet = Label(bottomFrame, text='This password meets ' + str(rules_met) + ' out of 5 rules.')
    lbl_os_rulesmet.grid(row=0, column=0, columnspan=2, pady=20)

    # very strong pass label
    lbl_veryStrong = Label(bottomFrame, text='You have a very strong password!')
    lbl_veryStrong.grid(row=1, column=0, columnspan=2, pady=20)

    # time to crack label
    lbl_timeToCrack = Label(bottomFrame, text='Approximate time to crack:')
    lbl_timeToCrack.grid(row=2, column=0, sticky=E)

    #original time label
    lbl_originalTime = Label(bottomFrame, text= originalTime)
    lbl_originalTime.grid(row=2, column=1, sticky=W)

    # copy to clipboard button
    btn_Copy = Button(bottomFrame, text='Copy strong password to clipboard', height=2, width=40, command=copy_to_clipboard(password))
    btn_Copy.grid(row=3, column=0, columnspan=2, pady=20)


# output to bottom of gui when a weak password is entered
def output_weak(rules_met, originalTime, suggestedPass, suggestionTime):
    print('weak output')
    print('Rules met: ' + str(rules_met))
    print('Original time to crack: ' + originalTime)
    print('Suggested pass: ' + suggestedPass)
    print('Suggestion time: ' + suggestionTime)

    # weak output rules met label
    lbl_ow_rulesmet = Label(bottomFrame, text='This password meets ' + str(rules_met) + ' out of 5 rules.')
    lbl_ow_rulesmet.grid(row=0, column=0, columnspan=2, pady=20)

    # time to crack label
    lbl_timeToCrack = Label(bottomFrame, text='Approximate time to crack:')
    lbl_timeToCrack.grid(row=1, column=0, sticky=E)

    #original time label
    lbl_originalTime = Label(bottomFrame, text= originalTime)
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
    lbl_sugTime = Label(bottomFrame, text= suggestionTime)
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
    if len(password) >= LENGTH:
        rules_met += 1
        length_met = True
    
    if lowercase >= LOWERS:
        rules_met += 1
        lowercase_met = True
    
    if uppercase >= UPPERS:
        rules_met += 1
        uppercase_met = True
    
    if number >= NUMBERS:
        rules_met += 1
        numbers_met = True
    
    if punctuation >= PUNCTUATIONS:
        rules_met += 1
        punc_met = True

    # call a function that will make the checkboxes by each rule
    # red x for not met, green check for met
    # pass in the boolean values for each rule
    checkboxes(length_met, lowercase_met, uppercase_met, numbers_met, punc_met)

    # call the time_to_crack function, the function will return the time of the original pass
    # as a string
    originalTime = time_to_crack(password)

    # if all rules are met, call a function that creates the output section of the gui
    # variables passed in: rules_met, originalTime, password
    if rules_met == 5:
        output_strong(rules_met, originalTime, password)
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
        suggestionTime = time_to_crack(suggestedPass)

        # finally, pass all the needed args into the function to create the weak output
        output_weak(rules_met, originalTime, suggestedPass, suggestionTime)


def suggestion(password,  need_length, need_lower, need_upper, need_number, need_punc):
    #print('suggestion')
    lower_chars = 'abcdefghijklmnopqrstuvwxyz' # variable containing lower chars
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # variable containing upper chars
    number_chars = '1234567890' # variable containing numbers
    symbols = '''~`! @#$%^&*()_-+={[}]|\:;"'<,>.?/''' # variable containing symbols

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
        c = random.choice(number_chars) # choose a random number
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
    if seconds >= 31536000: # if more than a year of seconds
        years = seconds / 31536000 # calculate years
        # create the return string
        return_str = str(years) + ' years'
        return return_str
    elif seconds >= 86400: # if more than a day of seconds
        days = seconds / 86400 # calcualte days
        return_str = str(days) + ' days'
        return return_str
    elif seconds >= 3600: # if more than an hour of seconds
        hours = seconds / 3600 # calculate hours
        return_str = str(hours) + ' hours'
        return return_str
    elif seconds >= 60: # if more than a minute of seconds
        minutes = seconds / 60
        return_str = str(minutes) + ' minutes'
        return return_str
    else:
        return_str = str(seconds) + ' seconds'
        return return_str


# this function will create the checkboxes indicating which rules are met by an input password
def checkboxes(length_met, lowerercase_met, uppercase_met, numbers_met, punc_met):
    print('checkboxes!!')


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

    # clear any output already written to bottomFrame
    for widget in bottomFrame.winfo_children():
        widget.destroy()

    print('Reset')

# divide screen vertically with 3 frames
topFrame = Frame(root)
topFrame.pack(side=TOP)
middleFrame = Frame(root)
middleFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# first label
passwordRequirements = Label(topFrame, text='PASSWORD REQUIREMENTS')
passwordRequirements.grid(row=0, column=0, columnspan=2)
    
# length label
lbl_minLength = Label(topFrame, text='Minimum Length:')
lbl_minLength.grid(row=1, column=0)
# length entry
entry_minLength = Entry(topFrame, width=5)
entry_minLength.grid(row=1, column=1)
# length slider
slider_minLength = Scale(topFrame, from_=5, to=50, orient=HORIZONTAL)
slider_minLength.grid(row=2, column=0, columnspan=2)

# lowers label
lbl_lowers = Label(topFrame, text='Lowercase Characters:')
lbl_lowers.grid(row=3, column=0)
# lowers entry
entry_lowers = Entry(topFrame, width=5)
entry_lowers.grid(row=3, column=1)
# lowers slider
slider_lowers = Scale(topFrame, from_=0, to=10, orient=HORIZONTAL)
slider_lowers.grid(row=4, column=0, columnspan=2)

# uppers label
lbl_uppers = Label(topFrame, text='Uppercase Characters:')
lbl_uppers.grid(row=5, column=0)
# uppers entry
entry_uppers = Entry(topFrame, width=5)
entry_uppers.grid(row=5, column=1)
# uppers slider
slider_uppers = Scale(topFrame, from_=0, to=10, orient=HORIZONTAL)
slider_uppers.grid(row=6, column=0, columnspan=2)

# numbers label
lbl_numbers = Label(topFrame, text='Number Characters:')
lbl_numbers.grid(row=7, column=0)
# numbers entry
entry_numbers = Entry(topFrame, width=5)
entry_numbers.grid(row=7, column=1)
# numbers slider
slider_numbers = Scale(topFrame, from_=0, to=10, orient=HORIZONTAL)
slider_numbers.grid(row=8, column=0, columnspan=2)

# punc label
lbl_punc = Label(topFrame, text='Punctuation Characters:')
lbl_punc.grid(row=9, column=0)
# punc entry
entry_punc = Entry(topFrame, width=5)
entry_punc.grid(row=9, column=1)
# punc slider
slider_punc = Scale(topFrame, from_=0, to=10, orient=HORIZONTAL)
slider_punc.grid(row=10, column=0, columnspan=2)


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


root.mainloop()