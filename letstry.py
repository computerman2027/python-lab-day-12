import tkinter as tk
from tkinter import messagebox

def check():
    try:
        val =int(entertext.get(1.0, "end-1c"))
        if val<0:
            messagebox.showerror("Error", "invalid entry")
        if val>=18:
            result.config(text="Elligible for voting",fg="green")
        else:
            result.config(text="NOT Elligible for voting",fg="red")
    except:
        messagebox.showerror("Error", "only in accepted")

root=tk.Tk()

root.title("Age calculator")

root.geometry("300x300")

heading=tk.Label(root,text="enter age : ",font=('Arial',20))
heading.pack()

entertext=tk.Text(root,height=1, width=5)
entertext.pack()

submitbutton=tk.Button(root,text="CHECK",command=check)
submitbutton.pack()

resulttext=tk.StringVar()
resulttext.set("a")

result=tk.Label(root,text="",font=('Arial',20))
result.pack()
root.mainloop()