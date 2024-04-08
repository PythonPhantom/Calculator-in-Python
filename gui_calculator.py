import customtkinter
from tkinter import *


expression = ""

# Functions

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def evaluate():
    global expression
    try :
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set("Error")
        expression = ""

def clearEquation():
    global expression
    expression = ''
    equation.set('')

def deleteBtn():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# Window

app = customtkinter.CTk()
app.geometry("500x700")
app.title("Calculator")
app.resizable(False, False)
equation = StringVar()

font = 'Verdana'
ent = customtkinter.CTkEntry(master=app, textvariable=equation, width=500, height=100, font=((font), 100), justify="right", state='disabled')
ent.pack()

button_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ".", "+", "-", "/", "*", "=", "C", "Del"]

# Special Buttons

clear = customtkinter.CTkButton(master=app, text_color='orange', fg_color='#242424',hover_color='#2e2e2e', text=button_lst[-2], height=100, width=100, font=(font, 40),
                                command = lambda :
clearEquation())
clear.place(relx=0.03, rely=0.19)

delete = customtkinter.CTkButton(master=app, text_color='orange', fg_color='#242424',hover_color='#2e2e2e', text=button_lst[-1], height=100, width=100, font=(font, 40),
                                 command = lambda :
deleteBtn())
delete.place(relx=0.2847, rely=0.19)

percent = customtkinter.CTkButton(master=app, text_color='orange', fg_color='#242424', hover_color='#2e2e2e', text='%', height=100 ,width=100, font=(font, 40), command = lambda : press('%'))
percent.place(relx=0.53, rely=0.19)

divide = customtkinter.CTkButton(master=app, text_color='orange', fg_color='#242424',hover_color='#2e2e2e', text=button_lst[-5], height=100, width=100, font=(font, 40), command = lambda :
press(
    '/'))
divide.place(relx=0.76, rely=0.19)

multiply = customtkinter.CTkButton(master=app, text_color='orange', fg_color='#242424',hover_color='#2e2e2e', text=button_lst[-4], height=100, width=100, font=(font, 40), command = lambda :
press('*'))
multiply.place(relx=0.76, rely=0.35)

add = customtkinter.CTkButton(master=app, text_color='orange', fg_color='#242424',hover_color='#2e2e2e', text=button_lst[-7], height=100, width=100, font=(font, 40), command = lambda : press(
    '+'))
add.place(relx=0.76, rely=0.513)

subtract = customtkinter.CTkButton(master=app, text_color='orange', fg_color='#242424',hover_color='#2e2e2e', text=button_lst[-6], height=100, width=100, font=(font, 40), command = lambda :
press('-'))
subtract.place(relx=0.76, rely=0.675)

equals_button = customtkinter.CTkButton(master=app, fg_color='orange',hover_color='#2e2e2e', text=button_lst[-3], height=100, width=220, font=(font, 40),
                                        command = lambda :evaluate(), corner_radius=500)
equals_button.place(relx=0.53, rely=0.84)

# First Row Numbers

seven = customtkinter.CTkButton(master=app, fg_color='#242424',hover_color='#2e2e2e', text=button_lst[7], height=100, width=100, font=(font, 40), command = lambda :
press(7))
seven.place(relx=0.03, rely=0.35)

eight = customtkinter.CTkButton(master=app, fg_color='#242424',hover_color='#2e2e2e', text=button_lst[8], height=100, width=100, font=(font, 40), command = lambda :
press(8))
eight.place(relx=0.2847, rely=0.35)

nine = customtkinter.CTkButton(master=app, fg_color='#242424',hover_color='#2e2e2e', text=button_lst[9], height=100, width=100, font=(font, 40), command = lambda :
press(9))
nine.place(relx=0.53, rely=0.35)

# Second Row Numbers

four = customtkinter.CTkButton(master=app, fg_color='#242424',hover_color='#2e2e2e', text=button_lst[4], height=100, width=100, font=(font, 40), command = lambda :
press(4))
four.place(relx=0.03, rely=0.513)

five = customtkinter.CTkButton(master=app, fg_color='#242424',hover_color='#2e2e2e', text=button_lst[5], height=100, width=100, font=(font, 40), command = lambda :
press(5))
five.place(relx=0.2847, rely=0.513)

six = customtkinter.CTkButton(master=app, fg_color='#242424',hover_color='#2e2e2e', text=button_lst[6], height=100, width=100, font=(font, 40), command = lambda :
press(6))
six.place(relx=0.53, rely=0.513)

# Third Row Numbers

one = customtkinter.CTkButton(master=app, fg_color='#242424',hover_color='#2e2e2e', text=button_lst[1], height=100, width=100, font=(font, 40), command = lambda :
press(1))
one.place(relx=0.03, rely=0.675)

two = customtkinter.CTkButton(master=app, fg_color='#242424',hover_color='#2e2e2e', text=button_lst[2], height=100, width=100, font=(font, 40), command = lambda :
press(2))
two.place(relx=0.2847, rely=0.675)

three = customtkinter.CTkButton(master=app, fg_color='#242424',hover_color='#2e2e2e', text=button_lst[3], height=100, width=100, font=(font, 40), command = lambda :
press(3))
three.place(relx=0.53, rely=0.675)

# Fourth Row

zero = customtkinter.CTkButton(master=app, fg_color='#242424',hover_color='#2e2e2e', text=button_lst[0], height=100, width=100, font=(font, 40), command=lambda: press(0))
zero.place(relx=0.2847, rely=0.84)

decimal = customtkinter.CTkButton(master=app, fg_color='#242424',hover_color='#2e2e2e', text=button_lst[10], height=100, width=100, font=(font, 40), command = lambda :
press('.'))
decimal.place(relx=0.03, rely=0.84)

app.mainloop()
