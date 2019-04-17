"""
Author: Nicholas Kurland
Name: Auth_Buttons
Purpose:
Requirements:
"""
from tkinter import *
Auth_Seq = [1,2,3,6,4]

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
    print(Auth)
    print(Auth_Seq)
    Password_Sequence.clear()


def closewindow():
    print("I close now")
    exit()

def Input_Password(Number_Sequence):
    Sav_Sequence = []
    i = 0
    while i < len(Number_Sequence):
        Sav_Sequence.append(Number_Sequence[i])
        i = i + 1
    global Auth_Seq
    Auth_Seq = Sav_Sequence
    Number_Sequence.clear()

def begin_auth():
    height= 0
    width= 0
    master = Tk()

    Passseq = []
    NumSeq = []


    #Makes the 9 Buttons each with 1-9 on them
    buttonNW = Button(master, text="1", command=closewindow)
    buttonN = Button(master, text="2", command=closewindow)
    buttonNE = Button(master, text="3", command=closewindow)
    buttonW = Button(master, text="4", command=closewindow)
    buttonMiddle = Button(master, text="5", command=closewindow)
    buttonE = Button(master, text="6", command=closewindow)
    buttonSW = Button(master, text="7", command=closewindow)
    buttonS = Button(master, text="8", command=closewindow)
    buttonSE = Button(master, text="9", command=closewindow)

    #Create Auth Button and Password Input Button
    Authbutton = Button(master,text="Authenticate", command = lambda: Test_Auth(NumSeq,Auth_Seq))
    PasswordInput= Button(master, text = "Password Input", command = lambda: Input_Password(NumSeq))
    Authbutton.place(x=150,y=0,height=25,width=100)
    PasswordInput.place(x=250,y=0,height=25,width=100)

    #PasswordInput.bind("<ButtonRelease-1>", lambda event: )


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

    #Creates an event where when you mouse over a button it turns red and when you move the mouse away it turns white
    buttonNW.bind("<Enter>", lambda event: NumSeq.append(1))
    #buttonNW.bind("<Leave>", lambda event: buttonNW.configure(bg="blue"))
    buttonN.bind("<Enter>", lambda event: NumSeq.append(2))
    #buttonN.bind("<Leave>", lambda event: buttonN.configure(bg="blue"))
    buttonNE.bind("<Enter>", lambda event: NumSeq.append(3))
    #buttonNE.bind("<Leave>", lambda event: buttonNE.configure(bg="blue"))
    buttonE.bind("<Enter>",lambda event: NumSeq.append(4))
    #buttonE.bind("<Leave>",lambda event: buttonE.configure(bg="blue"))
    buttonMiddle.bind("<Enter>", lambda event: NumSeq.append(5))
    #buttonMiddle.bind("<Leave>", lambda event: buttonMiddle.configure(bg="blue"))
    buttonW.bind("<Enter>", lambda event: NumSeq.append(6))
    #buttonW.bind("<Leave>", lambda event: buttonW.configure(bg="blue"))
    buttonSW.bind("<Enter>", lambda event: NumSeq.append(7))
    #buttonSW.bind("<Leave>", lambda event: buttonSW.configure(bg="blue"))
    buttonS.bind("<Enter>", lambda event: NumSeq.append(8))
    #buttonS.bind("<Leave>", lambda event: buttonS.configure(bg="blue"))
    buttonSE.bind("<Enter>", lambda event: NumSeq.append(9))
    #buttonSE.bind("<Leave>", lambda event: buttonSE.configure(bg="blue"))


    #Sets the geometry to 500x500
    master.geometry("500x600")
    #Mainloop to run the thing
    mainloop()


begin_auth()
