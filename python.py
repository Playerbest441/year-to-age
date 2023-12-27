from tkinter import *
from datetime import date
from tkinter import messagebox
#setup
window = Tk()
window.geometry("400x400")
#today date information
today = date.today()	
d2 = today.strftime("%Y")
d2 = int(d2)
#defs
def say_age():
    userage = int(E1.get())
    result = (d2 - userage)
    if result < 0 :
        messagebox.showerror("what?", "somethong went wrong")
    else:
        lbl.configure(text=f"your age is {result}")
#####
Label(text="please enter ur year:", font=("bold",21)).pack()
E1 = Entry(width=45,)
E1.pack(padx=20,pady=20)
Button(text="say my age", command=lambda:say_age(),cursor="hand2").pack()
lbl = Label(text="",font=(21))
lbl.pack(padx=20,pady=20)
window.mainloop()
