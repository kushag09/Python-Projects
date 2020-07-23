from tkinter import *

root = Tk()
'''Project 1: Making a basic calculator'''
#Creating a box that shows the output of calculation
enterer = Entry(root, width=35, borderwidth=5)
enterer.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#What happens when we click on a number
def clik(num):
    inputs = enterer.get() #Gets the integer
    enterer.delete(0, END) #Deletes the value in input form
    enterer.insert(0, str(inputs) + str(num))

#Function for clearing the box
def clearer():
    enterer.delete(0, END)

#Function for addition
def adder():
    first_num = enterer.get()
    global f_num
    global maths
    maths = 'addition'
    f_num = int(first_num)
    enterer.delete(0, END)

#What happens when we press equals
def equals():
    sec_num = enterer.get()
    enterer.delete(0, END)
    if maths == 'addition':
        enterer.insert(0, f_num + int(sec_num))
    if maths == 'subtraction':
        enterer.insert(0, f_num - int(sec_num))
    if maths == 'multiplication':
        enterer.insert(0, f_num * int(sec_num))
    if maths == 'division':
        enterer.insert(0, f_num / int(sec_num))

#Function for subtraction
def subber():
    first_num = enterer.get()
    global f_num
    global maths
    maths = 'subtraction'
    f_num = int(first_num)
    enterer.delete(0, END)

#Function for multiplication
def product():
    first_num = enterer.get()
    global f_num
    global maths
    maths = 'multiplication'
    f_num = int(first_num)
    enterer.delete(0, END)

#Function for division
def divider():
    first_num = enterer.get()
    global f_num
    global maths
    maths = 'division'
    f_num = int(first_num)
    enterer.delete(0, END)

#Making buttons for numbers and operators

button1 = Button(root, text='1', padx=40, pady=20, command=lambda: clik(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: clik(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: clik(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: clik(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: clik(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: clik(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: clik(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: clik(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: clik(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: clik(0))

buttonadd = Button(root, text='+', padx=39, pady=20, command=adder)
buttoneq = Button(root, text='=', padx=91, pady=20, command=equals)
buttoncl = Button(root, text='Clear', padx=79, pady=20, command=clearer)
buttonsub = Button(root, text='-', padx=41, pady=20, command=subber)
buttonprod = Button(root, text='x', padx=40, pady=20, command=product)
buttondiv = Button(root, text='/', padx=40, pady=20, command=divider)

#Adding buttons on the window
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttoncl.grid(row=4, column=1, columnspan=2)
buttonadd.grid(row=5, column=0)

buttoneq.grid(row=5, column=1, columnspan=2)
buttonsub.grid(row=6, column=0)
buttonprod.grid(row=6, column=1)

buttondiv.grid(row=6, column=2)

root.mainloop()
