from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from math import *

calc = Tk()
calc.title("GUI")
calc.geometry('370x450')
calc.title("My Calcualtor")
 
#Defining the display frame
disp_input=StringVar()
disp=Frame(calc, width=390, height = 200, bd = 0, bg = "mint cream")
disp.pack(side=TOP)
disp_ent=Entry(disp, font = ('Cambria', 18, 'bold'), textvariable = disp_input, width = 50, bg = "mint cream", bd = 0, justify = RIGHT)
disp_ent.grid(row=0,column=0)
disp_ent.pack(ipady=10)

#defining the input
buttons_input=Frame(calc, width = 380, height = 300, bg = "grey")
buttons_input.pack()

expression = ""

#when the square button is clicked
def do_square(x):
    global expression
    expression = expression + "**2"
    expression = str(eval(expression))
    disp_input.set(expression)

#when the squareroot button is clicked
def do_sqrt(x):
    global expression
    expression = expression + "**0.5"
    expression = str(eval(expression))
    disp_input.set(expression)

#when the other buttons are clicked
def click(x):
    global expression
    expression = expression + str(x)
    disp_input.set(expression) 

#when C is clicked
def clc():
    global expression
    expression = ""
    disp_input.set("")
 
 #when "=" is clicked
def equals_to():
    global expression
    result = str(eval(expression))
    disp_input.set(result)
    expression = result
    
 

#placing of Buttons
squareroot = Button(buttons_input, text = "√", fg = "black", width = 12, height = 3, bd = 0, bg = "azure", cursor = "hand2", command = lambda: do_sqrt("sqrt")).grid(row = 1, column = 0, padx = 1, pady = 1)
squared = Button(buttons_input, text = "x²", fg = "black", width = 12, height = 3, bd = 0, bg = "azure", cursor = "hand2", command = lambda: do_square("**2")).grid(row = 1, column = 1, padx = 1, pady = 1)
divide = Button(buttons_input, text = "/", fg = "black", width = 12, height = 3, bd = 0, bg = "azure", cursor = "hand2", command = lambda: click("/")).grid(row = 1, column = 2, padx = 1, pady = 1)
clear = Button(buttons_input, text = "C", fg = "black", width = 12, height = 3, bd = 0, bg = "azure", cursor = "hand2", command = lambda: clc()).grid(row = 1, column = 3, padx = 1, pady = 1)
one=Button(buttons_input, text = "1", fg = "black", width = 12, height = 5, bd = 0, bg = "white", cursor = "hand2", command = lambda: click(1)).grid(row = 2, column = 0, padx = 1, pady = 1)
two=Button(buttons_input, text = "2", fg = "black", width = 12, height = 5, bd = 0, bg = "white", cursor = "hand2", command = lambda: click(2)).grid(row = 2, column = 1, padx = 1, pady = 1)
three=Button(buttons_input, text = "3", fg = "black", width = 12, height = 5, bd = 0, bg = "white", cursor = "hand2", command = lambda: click(3)).grid(row = 2, column = 2, padx = 1, pady = 1)
multiply=Button(buttons_input, text = "*", fg = "black", width = 12, height = 5, bd = 0, bg = "azure", cursor = "hand2", command = lambda: click("*")).grid(row = 2, column = 3, padx = 1, pady = 1)
four = Button(buttons_input, text = "4", fg = "black", width = 12, height = 5, bd = 0, bg = "white", cursor = "hand2", command = lambda: click(4)).grid(row = 3, column = 0, padx = 1, pady = 1)
five = Button(buttons_input, text = "5", fg = "black", width = 12, height = 5, bd = 0, bg = "white", cursor = "hand2", command = lambda: click(5)).grid(row = 3, column = 1, padx = 1, pady = 1)
six = Button(buttons_input, text = "6", fg = "black", width = 12, height = 5, bd = 0, bg = "white", cursor = "hand2", command = lambda: click(6)).grid(row = 3, column = 2, padx = 1, pady = 1)
minus = Button(buttons_input, text = "-", fg = "black", width = 12, height = 5, bd = 0, bg = "azure", cursor = "hand2", command = lambda: click("-")).grid(row = 3, column = 3, padx = 1, pady = 1)
seven = Button(buttons_input, text = "7", fg = "black", width = 12, height = 5, bd = 0, bg = "white", cursor = "hand2", command = lambda: click(7)).grid(row = 4, column = 0, padx = 1, pady = 1)
eight = Button(buttons_input, text = "8", fg = "black", width = 12, height = 5, bd = 0, bg = "white", cursor = "hand2", command = lambda: click(8)).grid(row = 4, column = 1, padx = 1, pady = 1)
nine = Button(buttons_input, text = "9", fg = "black", width = 12, height = 5, bd = 0, bg = "white", cursor = "hand2", command = lambda: click(9)).grid(row = 4, column = 2, padx = 1, pady = 1)
plus = Button(buttons_input, text = "+", fg = "black", width = 12, height = 5, bd = 0, bg = "azure", cursor = "hand2", command = lambda: click("+")).grid(row = 4, column = 3, padx = 1, pady = 1)
zero = Button(buttons_input, text = "0", fg = "black", width = 25, height = 5, bd = 0, bg = "white", cursor = "hand2", command = lambda: click(0)).grid(row = 5, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(buttons_input, text = ".", fg = "black", width = 12, height = 5, bd = 0, bg = "azure", cursor = "hand2", command = lambda: click(".")).grid(row = 5, column = 2, padx = 1, pady = 1)
equals = Button(buttons_input, text = "=", fg = "black", width = 12, height = 5, bd = 0, bg = "azure", cursor = "hand2", command = lambda: equals_to()).grid(row = 5, column = 3, padx = 1, pady = 1)
 
calc.mainloop()
