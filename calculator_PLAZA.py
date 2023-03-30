from tkinter import *
class MyWindow:
    def __init__(self, win):

#widgets start from here
        self.lbl1 = Label(win, text="1st No.")
        self.lbl1.place(x=100, y=50)

        self.lbl2 = Label(win, text= "2nd No.")
        self.lbl2.place(x=100, y=100)

        self.lbl3 = Label(win, text="Result")
        self.lbl3.place(x=100, y=150)

        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=200, y=50)

        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=200, y=100)

        self.txt3 = Entry(win, bd=3)
        self.txt3.place(x=200, y=150)

        self.btnadd = Button(win, text="Addition" , fg = "White" , bg = "#008080")
        self.btnadd.place(x=400, y=85)
        self.btnadd.bind('<Button-1>', self.add)

        self.btnsub = Button(win, text="Subtraction" , fg = "White" , bg = "#008080")
        self.btnsub.place(x=400, y=120)
        self.btnsub.bind('<Button-1>', self.sub)

        self.btnmulti = Button(win, text="Multiplication", fg = "White", bg = "#008080" , command = self.multi)
        self.btnmulti.place(x=400, y=155)

        self.btndivi = Button(win, text="Division", fg = "White", bg = "#008080" , command = self.divi)
        self.btndivi.place(x=400, y=190)

        self.btnclr = Button(win, text="Clear" , fg= "White" , bg = "#89CFF0")
        self.btnclr.place(x=400, y=45)
        self.btnclr.bind('<Button-1>', self.clr)

#add event-handling /bind () method

    def add(self, add):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END, str(result))

    def sub(self, sub):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1-num2
        self.txt3.insert(END, str(result))

    def multi(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))

    def divi(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 / num2
        self.txt3.insert(END, str(result))

    def clr(self, clr):
        self.txt1.delete(0)
        self.txt2.delete(0)
        self.txt3.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()







