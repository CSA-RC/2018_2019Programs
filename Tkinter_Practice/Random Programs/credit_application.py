from tkinter import *

root = Tk()

class App:

    def __init__(self,master):

        master.title("Credit Application")

        masterframe = Frame(master, width=200, height=150)
        masterframe.pack()

        self.loantype = IntVar()
        self.name=StringVar()
        self.age=StringVar()
        carb = Radiobutton(masterframe, text="Car", var=self.loantype, value=1)
        carb.grid(column=0, row=1, sticky="w")

        houseb = Radiobutton(masterframe, text="House", var=self.loantype, value=2)
        houseb.grid(column=0, row=2, sticky="w")

        personalb = Radiobutton(masterframe, text="Personal", var=self.loantype, value=3)
        personalb.grid(column=0, row=3, sticky="w")

        spacer = Label(masterframe, text="          ")
        spacer.grid(column=1, row=1)

        namelabel = Label(masterframe, text="Name :")
        namelabel.grid(column=2, row=0, sticky="w")

        nameentry=Entry(masterframe, width=20, textvar=self.name)
        nameentry.grid(column=2, row=1)

        agelabel = Label(masterframe, text="Age :")
        agelabel.grid(column=2, row=2, sticky="w")

        ageentry = Entry(masterframe, width=5, textvar=self.age)
        ageentry.grid(column=2, row=3, sticky="w")

        self.submitbutton = Button(masterframe, text="SUBMIT", command=self.store)
        self.submitbutton.grid(column=0, row=4, sticky="w")

    def clear(self):
        self.loantype.set(0)
        self.name.set("")
        self.age.set("")

    def store(self):
        name = self.name.get()
        age = self.age.get()
        if self.loantype.get() == 1:
            loan = "Car"
        elif self.loantype.get() == 2:
            loan = "House"
        elif self.loantype.get() == 3:
            loan = "Personal"
        else:
            loan = "None"
        try:
            favorite_ice_cream_txt = open("credit_application.txt", "a")
            favorite_ice_cream_txt.write("\n\nType of loan: %s \nName: %s \nAge: %s" % (loan, name, age))
            favorite_ice_cream_txt.close()
        except FileNotFoundError:
            favorite_ice_cream_txt = open("credit_application.txt", "w")
            favorite_ice_cream_txt.write("\n\nType of loan: %s \nName: %s \nAge: %s" % (loan, name, age))
            favorite_ice_cream_txt.close()

        self.clear()





app = App(root)
root.geometry('280x130')
root.mainloop()