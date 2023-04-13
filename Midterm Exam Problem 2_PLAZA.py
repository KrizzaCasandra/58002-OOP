from tkinter import *

class myWindow:
    def __init__(self, win):
        self.lbl0 = Label(win, text="My Full Name", foreground="red", font="verdana")
        self.lbl0.place(x=200, y=25)

        self.lbl1 = Label(win, text="Enter Given Name: ", foreground="red" )
        self.lbl1.place(x=100, y=50)

        self.lbl2 = Label(win, text="Enter Middle Name: ", foreground="red")
        self.lbl2.place(x=100, y=100)

        self.lbl3 = Label(win, text="Enter Last Name: ", foreground="red")
        self.lbl3.place(x=100, y=150)

        self.lbl4 = Label(win, text="My Full Name is: ", foreground="red")
        self.lbl4.place(x=100, y=200)

        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=300, y=50)

        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=300, y=100)

        self.txt3 = Entry(win, bd=1)
        self.txt3.place(x=300, y=150)

        self.txt4 = Entry(win, bd=3, foreground="red")
        self.txt4.place(x=300, y=200, width=189)

        self.btnfn = Button(win, text="Show Full Name", )
        self.btnfn.place(x=200, y=250, width="150")
        self.btnfn.bind('<Button-1>', self.fname)

        self.btnfn = Button(win, text="Clear All", )
        self.btnfn.place(x=200, y=300, width="150")
        self.btnfn.bind('<Button-1>', self.clr)

    def fname(self, fname):
        num1 = (self.txt1.get())
        num2 = (self.txt2.get())
        num3 = (self.txt3.get())
        result = num3 + ", " + num1 + " " + num2
        self.txt4.insert(END, str(result))

    def clr(self, clr):
        self.txt1.delete(0)
        self.txt2.delete(0)
        self.txt3.delete(0)
        self.txt4.delete(0, 'end')

window = Tk()
mywin = myWindow(window)
window.geometry("500x400+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()