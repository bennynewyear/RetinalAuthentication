"""
Author: Nicholas Kurland
Name: Auth_Buttons
Purpose: This program is designed to use tkinter to create a button GUI that allows the user to authenticate themselves
This is meant to be a helper function for general authentication using retinal authentication and
retinal eye tracking to move a house
This program is to be updated and upgraded in the future to accodomate for more complicated passwords and other
functionalities as necessary.
Requirements: Python3
"""
from tkinter import *
import time
#Global Variables that the program uses

Auth_Seq = [1,2,3,4,6]
#Indicates whether or not we are counting the timer
state = False
#The stored timer value in Minutes, Seconds, Centiseconds
timer = [0,0,0]
#Number Sequence that is referred to by multiple functions
NumSeq = []


#Function name: Test Auth
#Purpose: Tests whether or not a password inputted is the correct password and than gives back if it was
#Input: Password Sequence- The sequence to test against the auth sequence
#       Auth_Sequence- The password sequence to be tested against
#Output: Tells if the user authenticated correctly or not
def Test_Auth(Password_Sequence, Auth_Sequence):
    Auth = True
    P = len(Password_Sequence)
    A = len(Auth_Sequence)

    if P != A:
        Auth = False
    else:
        i = 0
        while i < len(Auth_Sequence):
            x = Password_Sequence[i]
            y = Auth_Sequence[i]
            if x != y:
                Auth= False
                break
            i = i +1


    if Auth == True:
        print("Password is correct")
    else:
        print("Password is incorrect")
    Password_Sequence.clear()

#Function Name: Update Timer
#Purpose: This function begins running the moment the program starts and keeps going
#         Until the end, it updates the timer when the timer is active.
#         Timer is only active when the user's mouse hovers over a button
#         Minute counter is here in case seconds overflow occurs
def update_Timer():
    if state==True:
        global timer
        # Increments the timer by 1 centisecond when this function is called
        timer[2] += 1

        # If there are 100 centiseconds, go up by 1 second
        if (timer[2] >= 100):
            timer[2] = 0
            timer[1] += 1
        # If there are 60 seconds, count up 1 minute
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        # Calls the update_Timer() function after 1 centisecond
    #Calls the update Timer function every centisecond
    master.after(10, update_Timer)

#Function Name: Start Timer
#Purpose: Simply starts the timer
def start_timer():
    global state
    state = True

#Function Name: stop_timer
#Purpose: Stops the timer and checks to see if the number of seconds is greater than 5 to simulate focus on the button
#         for 5 seconds. If the time spent focusing on a button is greater than or equal to 5 seconds than it appends
#         the button number to the Num_Seq as input
#Inputs: Number(int)- What number to input if user focus on the button is greater than 5 seconds
def stop_timer(number):
    global state
    global NumSeq
    global timer
    state = False
    if timer[1] >= 5 or timer[0] > 0:
        NumSeq.append(number)
    timer = [0,0,0]



#Function Name: Input Password
#Purpose: Test function to allow a tester to change the password and than auth against it
#Input: Number Sequence- Sequence to change the overall password to authenticate against to
def Input_Password(Number_Sequence):
    Sav_Sequence = []
    i = 0
    while i < len(Number_Sequence):
        Sav_Sequence.append(Number_Sequence[i])
        i = i + 1
    global Auth_Seq
    Auth_Seq = Sav_Sequence
    Number_Sequence.clear()

#This segment past here is to initial the buttons and the GUI for user usage
master = Tk()



#Makes the 9 Buttons each with 1-9 on them
buttonNW = Button(master, text="1")
buttonN = Button(master, text="2")
buttonNE = Button(master, text="3")
buttonW = Button(master, text="4")
buttonMiddle = Button(master, text="5")
buttonE = Button(master, text="6")
buttonSW = Button(master, text="7")
buttonS = Button(master, text="8")
buttonSE = Button(master, text="9")

#Create Auth Button and Password Input Button
#Auth button calls the Test Auth Function
#Password Input button calls the Input_Password Button
Authbutton = Button(master,text="Authenticate", command = lambda: Test_Auth(NumSeq,Auth_Seq))
PasswordInput= Button(master, text = "Password Input", command = lambda: Input_Password(NumSeq))
Authbutton.place(x=150,y=0,height=25,width=100)
PasswordInput.place(x=250,y=0,height=25,width=100)

#Places each of the buttons at the 8 directions of the canvas plus one in the middle
buttonNW.pack()
buttonNW.place(x=0,y=50,height=50,width=50)
buttonN.pack()
buttonN.place(x=225,y=50, height=50, width=50)
buttonNE.pack()
buttonNE.place(x=450,y=50, height=50, width=50)
buttonW.pack()
buttonW.place(x=0,y=275, height=50, width=50)
buttonMiddle.pack()
buttonMiddle.place(height=50, width=50,x=225,y=275)
buttonE.pack()
buttonE.place(x=450,y=275, height=50, width=50)
buttonSW.pack()
buttonSW.place(x=0,y=500, height=50, width=50)
buttonS.pack()
buttonS.place(x=225,y=500, height=50, width=50)
buttonSE.pack()
buttonSE.place(x=450,y=500, height=50, width=50)

#Creats events for each of the buttons
#Enter Event: Run the Start_Timer program to start the timer
#Leave Event: Run the Stop_Timer program to stop the timer and input the number if a user focused on it
#for 5 seconds
buttonNW.bind("<Enter>", lambda event: start_timer())
buttonNW.bind("<Leave>", lambda event: stop_timer(1))

buttonN.bind("<Enter>", lambda event: start_timer())
buttonN.bind("<Leave>", lambda event: stop_timer(2))

buttonNE.bind("<Enter>", lambda event: start_timer())
buttonNE.bind("<Leave>", lambda event: stop_timer(3))

buttonW.bind("<Enter>", lambda event: start_timer())
buttonW.bind("<Leave>", lambda event: stop_timer(4))

buttonMiddle.bind("<Enter>", lambda event: start_timer())
buttonMiddle.bind("<Leave>", lambda event: stop_timer(5))

buttonE.bind("<Enter>",lambda event: start_timer())
buttonE.bind("<Leave>",lambda event: stop_timer(6))

buttonSW.bind("<Enter>", lambda event: start_timer())
buttonSW.bind("<Leave>", lambda event: stop_timer(7))

buttonS.bind("<Enter>", lambda event: start_timer())
buttonS.bind("<Leave>", lambda event: stop_timer(8))

buttonSE.bind("<Enter>", lambda event: start_timer())
buttonSE.bind("<Leave>", lambda event: stop_timer(9))

#Starts the update_timer function to start the timer
update_Timer()
#Sets the geometry to 500x500
master.geometry("500x600")
#Mainloop to run the thing
mainloop()
