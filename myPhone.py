# import Button
from tkinter import Tk, Label, Button, StringVar
from tkinter.messagebox import showinfo

def append(num):
    if not isinstance(num, str):
        num = str(num)
    keyNum.set(keyNum.get() + num)

def call():
    msg = "Calling..."
    showinfo(message = msg)

# Creating the GUI window.
root = Tk()
root.title("Telephone")
root.geometry("500x170")

keyNum = StringVar(value='')
keypad = Label(root, width=25, height=1, textvariable= keyNum)
keypad.grid(row=0, column=0)

#Keypad Buttons 7, 8, 9
button7 = Button(root, text='7', width=2, command=lambda: append(7))
button7.grid(row=1, column=1)
button8 = Button(root, text='8', width=2, command=lambda: append(8))
button8.grid(row=1, column=2)
button9 = Button(root, text='9', width=2, command=lambda: append(9))
button9.grid(row=1, column=3)

#Keypad Buttons 4, 5, 6
button4 = Button(root, text='4', width=2, command=lambda: append(4))
button4.grid(row=2, column=1)
button5 = Button(root, text='5', width=2, command=lambda: append(5))
button5.grid(row=2, column=2)
button6 = Button(root, text='6', width=2, command=lambda: append(6))
button6.grid(row=2, column=3)

#Keypad Buttons 1, 2, 3
button1 = Button(root, text='1', width=2, command=lambda: append(1))
button1.grid(row=3, column=1)
button2 = Button(root, text='2', width=2, command=lambda: append(2))
button2.grid(row=3, column=2)
button3 = Button(root, text='3', width=2, command=lambda: append(3))
button3.grid(row=3, column=3)

#Keypad Button *, 0, #
buttonAsk = Button(root, text='*', width=2, command=lambda: append("*"))
buttonAsk.grid(row=4, column=1,)
button0 = Button(root, text='0', width=2, command=lambda: append(0))
button0.grid(row=4, column=2,)
buttonHash = Button(root, text='#', width=2, command=lambda: append("#"))
buttonHash.grid(row=4, column=3,)

#Keypad Call Button
buttonCall = Button(root, padx=10, text="Call", command=call)
buttonCall.grid(row=5,column=2)

root.mainloop()
