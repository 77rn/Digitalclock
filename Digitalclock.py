from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    d3ate_label.config(text=date_string)

    window.after(1000,update)

window = Tk()

time_label = Label(window,font=("calibri",150),fg="grey",bg="black")
time_label.pack()

day_label = Label(window,font=("calibri",50,"bold"),fg="black")
day_label.pack()
date_label = Label(window,font=("calibri",50,"bold"),fg="black")
date_label.pack()

update()
window.mainloop()

#this is my class project
