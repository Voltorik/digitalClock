# Digital Clock
# Displays time based on region

from tkinter import *
from tkinter.ttk import *
from time import strftime

main = Tk()

main.title('Digital clock w/ Python')


def clock():
     tick = strftime('%I:%M:%S %p')  # 12 hr time with am/pm

     clock_label.config(text = tick)

     clock_label.after(1000, clock)


clock_label = Label(main, font=('sans', 80), background='black', foreground='white')

clock_label.pack(anchor='center')

clock()
mainloop()

