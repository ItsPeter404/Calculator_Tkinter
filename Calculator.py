from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator) # Here this set function set the value of StringVariable to operator :D

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set(operator)

def btnEqualInput():
    global operator
    try:
        sumup = str(eval(text_Input.get()))  # Here this eval is a inbuild python function which silves a expression in a sting :D
        operator = sumup
        text_Input.set(sumup)
    except SyntaxError:
        text_Input.set("ERROR")
        operator = ""
    except NameError:
        text_Input.set("ERROR")
        operator = ""
    except ZeroDivisionError:
        text_Input.set("Can't divide by Zero")
        operator = ""

    


cal = Tk()
icon = PhotoImage(file = './Iconcalculator.png') # Setting up icon
cal.iconphoto(False, icon)
cal.resizable(False, False) # making it unscallabel
cal.title("Calculator") # Giving title
operator = ""
text_Input = StringVar()

text_Display = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                     bg='powder blue', justify='right').grid(columnspan=4)

# Setting Up and Rendring Buttons

btn7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="7", bg="powder blue", command=lambda: btnClick(7)).grid(row=1, column=0,pady=(0,10))
btn8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="8", bg="powder blue", command=lambda: btnClick(8)).grid(row=1, column=1,pady=(0,10))
btn9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="9", bg="powder blue", command=lambda: btnClick(9)).grid(row=1, column=2,pady=(0,10))
Addition = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="+", bg="#F3CA40", command=lambda: btnClick('+')).grid(row=1, column=3,pady=(0,10))
# =============================================================================================================
btn4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=2, column=0,pady=(0,10))
btn5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="5", bg="powder blue", command=lambda: btnClick(5)).grid(row=2, column=1,pady=(0,10))
btn6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="6", bg="powder blue", command=lambda: btnClick(6)).grid(row=2, column=2,pady=(0,10))
Substract = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                   text="-", bg="#F3CA40", command=lambda: btnClick('-')).grid(row=2, column=3,pady=(0,10))
# =============================================================================================================
btn1 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1", bg="powder blue", command=lambda: btnClick(1)).grid(row=3, column=0,pady=(0,10))
btn2 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="2", bg="powder blue", command=lambda: btnClick(2)).grid(row=3, column=1,pady=(0,10))
btn3 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="3", bg="powder blue", command=lambda: btnClick(3)).grid(row=3, column=2,pady=(0,10))
Multiply = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="*", bg="#F3CA40", command=lambda: btnClick('*')).grid(row=3, column=3,pady=(0,10))
# =============================================================================================================
btn0 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="0", bg="powder blue", command=lambda: btnClick(0)).grid(row=4, column=0,pady=(0,10))
btnClear = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="c", bg="#F2A541", command=btnClearDisplay).grid(row=4, column=1,pady=(0,10))
btnEquals = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                   text="=", bg="#ED254E", command=btnEqualInput).grid(row=4, column=2,pady=(0,10))
Devision = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text='/', bg="#F3CA40", command=lambda: btnClick('/')).grid(row=4, column=3,pady=(0,10))


cal.mainloop()
