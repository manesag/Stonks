import yahoofinance
import algo
import os
import time
import json
from tkinter import *
from winsound import *

def stonks(money, length):
    print(my_entry2.get())
    algo.Get_Stock(money, length)
    
    
def retrieve():
    print(my_entry2.get())
    exe = "python yahoofinance.py "
    uwu = exe + my_entry2.get()
    os.system(uwu)
    time.sleep(1)
    why = "-summary.json"
    imsai = my_entry2.get() + why
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
    window = Toplevel()
    window.title(my_entry2.get())
    newlabel = Label(window, font=("Arial bold", 18), text = my_entry2.get())
    newlabel.pack()
    newlabel = Label(window, font=("Arial", 18), text = "52 week low " + lowEnd + "\n")
    newlabel.pack()
    newlabel1 = Label(window, font=("Arial", 18), text = "52 week high " + highEnd + "\n")
    newlabel1.pack()
    newlabel2 = Label(window, font=("Arial", 18), text = "Beta " + beta)
    newlabel2.pack()

def About():
    window = Toplevel()
    window.title("About")
    newlabel = Label(window, font=("Arial", 18), text = "About this project")
    newlabel.pack()
    newlabel1 = Label(window, text = "This was supposed to be stock determining program for the 2020 UCF Hackathon\n This was made by Clayton, Natasha, Andrew and Michael.")
    newlabel1.pack(side=BOTTOM)
    
def Help():
    window = Toplevel()
    window.title("Help")
    newlabel = Label(window, font=("Arial", 18), text = "Help")
    newlabel.pack()
    newlabel1 = Label(window, text = "To use this program, select a term time, then type in a dollar amount into the text box.\nThen hope it works, some stocks won't work for whatever reason, blame Yahoo Finance or something.")
    newlabel1.pack(side=BOTTOM)

def Settings():
    window = Toplevel()
    window.title("Settings")
    newlabel = Label(window, font=("Arial", 18), text = "Settings")
    newlabel.pack()
    Button5 = Button(window, text = "On", font=("Arial", 12), command = lambda: PlaySound("tetris.wav",  SND_FILENAME|SND_LOOP|SND_ASYNC))
    Button5.pack(padx = 5, pady = 5)
    Button6 = Button(window, text = "Off", command = PlaySound(None,  SND_ALIAS))
    Button6.pack(padx = 5, pady = 5)
    newlabel1 = Label(window, text = "Why?")
    newlabel1.pack()

root = Tk()
frame1 = Frame(root, bd=5, bg="gainsboro")
frame2 = Frame(root, bd=3, bg="LightBlue3", relief=SUNKEN)
root.title("Stonks")

background_image=PhotoImage(file='bg.png')
background_label = Label(frame1, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label = Label(frame1, bg="LightBlue3", relief=SUNKEN, font=("Arial", 24), width = 30, justify=CENTER, text = "Enter a Stock Ticker")
label.pack()

Var1 = StringVar()
short = "short"
med = "med"
long = "long"
RBttn1 = Radiobutton(frame1, text = "Short Term", variable = Var1, value = short)
RBttn1.pack(side = 'top', anchor = 'w', padx = 5, pady = 5)
RBttn2 = Radiobutton(frame1, text = "Medium Term", variable = Var1, value = med)
RBttn2.pack(side = 'top', anchor = 'w', padx = 5, pady = 5)
RBttn3 = Radiobutton(frame1, text = "Long Term", variable = Var1, value = long)
RBttn3.pack(side = 'top', anchor = 'w', padx = 5, pady = 5)

my_entry2 = Entry(frame1, width = 20, font=("Arial", 12))
my_entry2.insert(0,'Money to invest')
my_entry2.pack(padx = 5, pady = 5)

Button0 = Button(frame1, text = "Submit", font=("Arial", 12), command = stonks(my_entry2.get(), value))
Button0.pack(side=BOTTOM, padx = 0, pady = 50)
Button1 = Button(frame2, text = "Settings", command = Settings)
Button1.pack(side=LEFT, padx = 5, pady = 5)
Button2 = Button(frame2, text = "Help", command = Help)
Button2.pack(side=LEFT, padx = 10, pady = 5)
Button3 = Button(frame2, text = "Exit", command = quit)
Button3.pack(side=RIGHT, padx = 10, pady = 5)
Button4 = Button(frame2, text = "About", command = About)
Button4.pack(side=RIGHT, padx = 5, pady = 5)

frame1.pack(side=TOP, padx=1,pady=1)
frame2.pack(side=BOTTOM, fill="x")

root.mainloop()
