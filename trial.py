import tkinter as tk
from tkinter import*
import webbrowser


with open('currencydata.txt')as f:
    lines=f.readlines()

    currencyDict={}
    for line in lines:
        parsed=line.split('\t')
        currencyDict[parsed[0]]=parsed[1]

#FUNCTION TO OPEN THE EMBEDDED URL ON THE BROWSER USING TKINTER GUI
def open_net():
    webbrowser.open("https://www.x-rates.com/graph/?from=INR&to=USD&amount=1")

#FUNCTION TO DISPLAY 2ND WINDOW IN WHICH RESULT IS PRINTED.

def display_result(result):
    global result_window
    result_window=tk.Toplevel(window)
    result_window.title("DISPLAY PAGE")
    imm=tk.PhotoImage(file='C:/Users/acer/Downloads/currency.png')
    result_window.iconphoto(False,imm)
    result_window.geometry("700x600")
    res_label=tk.Label(result_window,text=result,font=("Bookman Old Style",20))
    res_label.pack()


#MAIN PURPOSE OF THIS FUNCTION IS TO TRIGGER THE DLELETION OPERATION WHEN "CONVERT" BUTTON IS HIT.
def deletion():
    result_window.destroy()


#FUNCTION FOR CONVERTING CURRENCY 
def convert_currency():
    try:
        amount=float(amount_ent.get())
        currency=currency_var.get()
        result=amount*float(currencyDict[currency])
        display_result(f"{amount}INR IS EQUAL TO {result}{currency}")
    except ValueError:
        display_result("INVALID INPUT") 

#MAIN WINDOW CREATION 
window=tk.Tk()

    
window.title("CURRENCY CONVERTER")
#IMPORTING PNG FILE TO PLACE IT AS AN ICON FOR THE TKINTER WINDOW
img=tk.PhotoImage(file='C:/Users/acer/Downloads/currency.png')
window.iconphoto(False,img)
window.geometry("1920x1080")



#AMOUNT LABEL
label=tk.Label(window,text="ENTER THE DESIRED AMOUNT IN INR",font=("Times",20))
label.pack()

#AMOUNT ENTRY
#OBJECTIVE-TO CREATE AN ENTRY FIELDS
amount_ent=tk.Entry(window)
amount_ent.pack()

#VARIABLE IS GETTING CREATED TO STORE SELECTED CURRENCY.
currency_var=tk.StringVar(window)
currency_var.set("SELECTIONS MENU")

#CURRENCY LABEL
currency_label=tk.Label(window,text="ENTER THE PREFFERED CURRENCY",font=("Times",20))
currency_label.pack()

#DROPDOWN MENU CREATION
currency_menu=tk.OptionMenu(window,currency_var,*currencyDict)
currency_menu.pack()

#BUTTON FOR OPPENING OF EMBEDDED URL
open_button=tk.Button(window,text="REFER HERE",command=open_net)
open_button.pack()

#BUTTON FOR CONVERSION
conversion_button=tk.Button(window,text="CONVERT",command=convert_currency)
conversion_button.pack()

#BUTTON FOR CLOSING THE WINDOW
conversion_button1=tk.Button(window,text="CLOSE",command=deletion)
conversion_button1.pack(side=LEFT,padx=750,pady=0)
#WE VE USED THE SIDE MODULE TO PLACE THE CLOSE BUTTON AT CENTER


#the upper button is for conversion triggering and the lower button is to close the "DISPLAY WINDOW"

#RESULT LABEL WHICH IS GETTING CONFIGURIZED IN  DISPLAY_RESULT FUNCTION
res_label=tk.Label(window,text="")
res_label.pack()

# MAINLOOP CREATION TO START EVENT LOOP FOR WHOLE OF THE TKINTER GUI WINDOW AND ITS COMPONENT.
window.mainloop()
