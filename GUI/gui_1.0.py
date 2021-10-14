#!/usr/bin/env python3

from tkinter import *

root = Tk()
root.geometry('600x800')

def analyze():
    # get the value entered in entry box
    entered_pass = entry_password.get()
    print(entered_pass)

def reset():
    # clear the entered password
    entry_password.delete(0, END)
    print('Reset')


# divide screen vertically with 3 frames
topFrame = Frame(root)
topFrame.pack(side=TOP)
middleFrame = Frame(root)
middleFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# test the frames
#a = Label(topFrame, text='A')
#a.pack()
#b = Label(middleFrame, text='B')
#b.pack()
#c = Label(bottomFrame, text='C')
#c.pack()


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