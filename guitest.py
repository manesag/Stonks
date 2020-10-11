import yahoofinance
import os
import time
import json
from tkinter import *
 
def retrieve():
    print(my_entry.get())
    exe = "python yahoofinance.py "
    uwu = exe + my_entry.get()
    os.system(uwu)
    time.sleep(1)
    why = "-summary.json"
    imsai = my_entry.get() + why
    f = open(imsai)
    data = json.load(f)
    beta = data['Beta (5Y Monthly)']
    print(beta)
    string =  data['52 Week Range']
    lowEnd, highEnd = string.split(' - ')
    print(lowEnd)
    print(highEnd)
    f.close()
    os.remove(imsai)
 
root = Tk()
root.geometry("300x100")
frame = Frame(root)
frame.pack()


label = Label(frame, text = "Enter a Stock Ticker")
label.pack()

frame = Frame(root)
frame.pack()
 
my_entry = Entry(frame, width = 20)
my_entry.insert(0,'but not TSLA')
my_entry.pack(padx = 5, pady = 5)
 
 
Button = Button(frame, text = "Submit", command = retrieve)
Button.pack(padx = 5, pady = 5)


root.mainloop()
