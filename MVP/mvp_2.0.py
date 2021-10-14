#!/usr/bin/env python3

# global constants
LENGTH = 10
LOWERS = 1
UPPERS = 1
NUMBERS = 1
PUNCTUATIONS = 1
KPS = 1000000000 # keys per second used in cracking the password, 1 billion default

def time_to_crack(password): # function to estimate the time to crack a password
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

    print('') # print blank line

    # convert to bigger unit depending on how large the number is
    if seconds >= 31536000: # if more than a year of seconds
        years = seconds / 31536000 # calculate years
        print('Your password takes approximately ' + str(years) + ' years to crack.') # print calculation in years
    elif seconds >= 86400: # if more than a day of seconds
        days = seconds / 86400 # calcualte days
        print('Your password takes approximately ' + str(days) + ' days to crack.') # print calculation in days
    elif seconds >= 3600: # if more than an hour of seconds
        hours = seconds / 3600 # calculate hours
        print('Your password takes approximately ' + str(hours) + ' hours to crack.') # print calculation in hours
    elif seconds >= 60: # if more than a minute of seconds
        minutes = seconds / 60
        print('Your password takes approximately ' + str(minutes) + ' minutes to crack.') # print calculation in minutes
    else:
        print('Your password takes approximately ' + str(seconds) + ' seconds to crack.') # print the calculation in seconds
    
    print('') # blank line
    main()

def rules(): # function to show the rules that must be met for the password
    print('') # blank line
    print('Your password must meet the following rules to be considered strong:')
    print('Length: ' + str(LENGTH))
    print('At least ' + str(LOWERS) + ' lowercase letter(s).')
    print('At least ' + str(UPPERS) + ' uppercase letter(s).')
    print('At least ' + str(NUMBERS) + ' number(s).')
    print('At least ' + str(PUNCTUATIONS) + ' punctuation character(s).')
    print('') # blank line

    main()  # return to main function

def analyzer(password): # function to check if a password meets the rules
    rules_met = 0 # variable to track how many rules are met
    lowercase = 0 # variable to count number of lowercase letters
    lower_chars = 'abcdefghijklmnopqrstuvwxyz' # variable containing lower chars
    uppercase = 0 # variable to count number of uppercase letters
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # variable containing upper chars
    number = 0 # variable to count number of numbers
    number_chars = '1234567890' # variable containing numbers
    punctuation = 0 # variable to count number of punctuation characters

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

    # first check length
    print('Your password is ' + str(len(password)) + ' character(s) long.')
    if len(password) >= LENGTH: # if long enough
        print('Your password meets the minimum length requirement.')
        rules_met += 1
    else:
        print('Your password does not meet the minimum length requirement.')

    # state if lowercase rule is met
    print('Your password contains ' + str(lowercase) + ' lowercase character(s).')
    if lowercase >= LOWERS: # if rule is met
        print('Your password meets the lowercase character requirement.')
        rules_met += 1
    else:
        print('Your password does not meet the lowercase character requirement.')
    
    # state if the uppercase rule is met
    print('Your password contains ' + str(uppercase) + ' uppercase character(s).')
    if uppercase >= UPPERS: # if rule is met
        print('Your password meets the uppercase character requirement.')
        rules_met += 1
    else:
        print('Your password does not meet the uppercase character requirement.')
    
    # state if the number rule is met
    print('Your password contains ' + str(number) + ' number(s).')
    if number >= NUMBERS: # if rule is met
        print('Your password meets the number character requirement.')
        rules_met += 1
    else:
        print('Your password does not meet the number character requirement.')

    # state if the punctuation rule is met
    print('Your password contains ' + str(punctuation) + ' punctuation character(s).')
    if punctuation >= PUNCTUATIONS: # if rule is met
        print('Your password meets the punctation character requirement.')
        rules_met += 1
    else:
        print('Your password does not meet the punctuation character requirement.')

    # finally, state how many rules are met and if it is a strong password
    print('') # blank line
    # if all rules are met, it is a strong password
    if rules_met == 5:
        print('Your password meets every rule. You have a very strong password!')
    else: # if not all rules are met, say how many rules are met and want to do better
        print('Your password meets ' + str(rules_met) + ' out of 5 rules.')
        # now print suggestions based on which rules were not met
        if len(password) < LENGTH:
            print('Try making your password at least ' + str(LENGTH) + ' characters long.')
        if lowercase < LOWERS:
            print('Try a password that contains at least ' + str(LOWERS) + ' lowercase character(s).')
        if uppercase < UPPERS:
            print('Try a password that contains at least ' + str(UPPERS) + ' uppercase character(s).')
        if number < NUMBERS:
            print('Try a password that cointains at least ' + str(NUMBERS) + ' number(s).')
        if punctuation < PUNCTUATIONS:
            print('Try a password that contains at least ' + str(PUNCTUATIONS) + ' punctuation character(s).')

    print('') # blank line

    main() # return to main


def main():
    # take input from the user in the menu
    print('Enter "1" to see password rules.')
    print('Enter "2" to test if a password meets the rules.')
    print('Enter "3" to see how long a password will take to crack.')
    print('Enter "4" to close the program.')
    menu_option = input('Choose an option: ')
    # if 1 is entered, show the rules
    if menu_option == '1':
        rules()
    # if 2 is entered, prompt for a password to analyze
    elif menu_option == '2':
        password = input('Enter a password: ')
        analyzer(password)
    # if 3 is entered, prompt for a password to check the length to crack
    elif menu_option == '3':
        password = input('Enter a password: ')
        time_to_crack(password)
    # if 4 is entered, close the program
    elif menu_option == '4':
        exit()
    # if something else is answered, ask again for proper input
    else:
        print('Please choose a valid option.')
        main()



if __name__ == '__main__':
    main()