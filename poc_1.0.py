#!/usr/bin/env python3

# global constants
LENGTH = 10
LOWERS = 1
UPPERS = 1
NUMBERS = 1
PUNCTUATIONS = 1

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

def analyzer(password):
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
    # take input from the user for a password
    print('Enter "rules" to see password rules.')
    print('Enter "exit" to close the program.')
    password = input('Enter a password: ')
    # if rules is entered, show the rules
    if password == 'rules':
        rules()
    # if exit is entered, close the program
    elif password == 'exit':
        exit()
    # else, call the function to analyze the password
    else:
        analyzer(password)



if __name__ == '__main__':
    main()