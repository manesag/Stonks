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

def About():
    window = Toplevel()
    #window.geometry('350x200')
    newlabel = Label(window, font=("Arial", 18), text = "About this project")
    newlabel.pack()
    newlabel1 = Label(window, text = "This was supposed to be stock determining program for the 2020 UCF Hackathon\n This was made by Clayton, Natasha, Andrew and Michael.")
    newlabel1.pack(side=BOTTOM)

root = Tk()
#root.geometry("450x325")
frame1 = Frame(root, bd=5, bg="gainsboro")
frame2 = Frame(root, bd=3, bg="LightBlue3", relief=SUNKEN)
root.title("Stonks")

background_image=PhotoImage(file='bg.png')
background_label = Label(frame1, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


label = Label(frame1, bg="LightBlue3", relief=SUNKEN, font=("Arial", 24), width = 30, justify=CENTER, text = "Enter a Stock Ticker")
label.pack()

 
my_entry = Entry(frame1, width = 20, font=("Arial", 12))
my_entry.insert(0,'but not TSLA')
my_entry.pack(padx = 5, pady = 15)
 
Button0 = Button(frame1, text = "Submit", font=("Arial", 12), command = retrieve)
Button0.pack(side=BOTTOM, padx = 0, pady = 100)
#Button0.config( height = 5, width = 20 )
Button1 = Button(frame2, text = "Fuck off", command = retrieve)
Button1.pack(side=LEFT, padx = 5, pady = 5)
Button2 = Button(frame2, text = "Help", command = retrieve)
Button2.pack(side=LEFT, padx = 10, pady = 5)
Button3 = Button(frame2, text = "About", command = About)
Button3.pack(side=RIGHT, padx = 10, pady = 5)
Button4 = Button(frame2, text = "Exit", command = quit)
Button4.pack(side=RIGHT, padx = 5, pady = 5)

frame1.pack(side=TOP, padx=1,pady=1)
frame2.pack(side=BOTTOM, fill="x")

root.mainloop()
