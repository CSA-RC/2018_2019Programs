from tkinter import *
from tkinter import ttk
root = Tk()

class App:

    def __init__(self, master):

        mframe = Frame(master, width = 300, height = 340)
        mframe.pack()

        self.username = StringVar()
        self.username.set("")
        self.password = StringVar()
        self.password.set("")

        self.gvar = IntVar()
        self.gvar.set(0)

        self.usertype = ["IT", "HR", "Sales", "Maintenance", "Other"]

        self.cvar = IntVar()
        self.cvar.set(0)

        self.usert = StringVar()
        self.usert.set("")

        self.label = Label(mframe, text="Create User\n-------------")
        self.label.grid(column=1, row=0)

        self.usernameentry = Entry(mframe, width=15, textvar=self.username)
        self.usernameentry.grid(column=1, row=1, sticky="w")
        self.usernamel = Label(mframe, text="Username:  ")
        self.usernamel.grid(column=0, row=1)

        self.passwordentry = Entry(mframe, width=15, show="*", textvar=self.password)
        self.passwordentry.grid(column=1, row=2, sticky="w")
        self.passwordl = Label(mframe, text="Password:  ")
        self.passwordl.grid(column=0, row=2, sticky='e')

        self.maleb = Radiobutton(mframe, text="Male", var=self.gvar, value=1)
        self.maleb.grid(column=0, row=4, sticky="w")

        self.femaleb = Radiobutton(mframe, text="Female", var=self.gvar, value=2)
        self.femaleb.grid(column=2, row=4, sticky="w")

        self.adminb = Checkbutton(mframe, text="Admin", variable=self.cvar, onvalue=1)
        self.adminb.grid(column=0, row=6)

        self.userb = Checkbutton(mframe, text="User", variable=self.cvar, onvalue=2)
        self.userb.grid(column=1, row=6)

        self.guestb = Checkbutton(mframe, text="Guest", variable=self.cvar, onvalue=3)
        self.guestb.grid(column=2, row=6)

        self.choicebox = ttk.Combobox(mframe, width=12, state='readonly', value=self.usertype)
        self.choicebox.grid(column=1, row=7, sticky='w')
        self.choicebox.bind('<<ComboboxSelected>>', self.usertupdate)

        self.choicel = Label(mframe, text="\nUser\n-----")
        self.choicel.grid(column=1, row=5)

        self.gl = Label(mframe, text="\nGender\n--------")
        self.gl.grid(column=1, row=3)

        self.space = Label(mframe, text="")
        self.space.grid(column=0, row=8)

        self.submitbutton = Button(mframe, text="SUBMIT", command=self.store)
        self.submitbutton.grid(column=0, row=10, sticky="w")

        self.clearbutton = Button(mframe, text="CLEAR", command=self.clear)
        self.clearbutton.grid(column=0, row=9, stick="w")

    def clear(self):
        self.usert.set("")
        self.username.set("")
        self.password.set("")
        self.gvar.set(0)
        self.cvar.set(0)
        self.choicebox.set("")




    def usertupdate(self, x):
        self.usert.set(self.choicebox.get())

    def labelupdate(self):
        if self.usert.get() == "" or self.username.get() == "" or self.password.get() == "" or self.gvar.get() == 0 or self.cvar.get() == 0:
            self.errtest = True
            self.label.config(text="ERROR\n-------")
        else:
            self.errtest = False
            self.label.config(text="User Created\n--------------")

    def store(self):
        self.labelupdate()
        if self.errtest == False:
            username = self.username.get()
            password = self.password.get()
            utype = self.usert.get()
            if self.gvar.get() == 1:
                gender = "Male"
            elif self.gvar.get() == 2:
                gender = "Female"
            else:
                gender = "ERROR"

            if self.cvar.get() == 1:
                uchoice = "Admin"
            elif self.cvar.get() == 2:
                uchoice = "User"
            elif self.cvar.get() == 3:
                uchoice = "Guest"
            else:
                uchoice = "ERROR"

            try:
                Database_txt = open("database.txt", "a")
                Database_txt.write("\n\nUsername: %s \nPassword: %s \nGender: %s\nUser Type: %s\nField: %s\n" % (username, password, gender, uchoice, utype))
                Database_txt.close()
            except FileNotFoundError:
                Database_txt = open("database.txt", "w")
                Database_txt.write("\n\nUsername: %s \nPassword: %s \nGender: %s\nUser Type: %s\nField: %s\n" % (username, password, gender, uchoice, utype))
                Database_txt.close()
        else:
            pass


        self.clear()

app = App(root)
root.geometry('300x330')
root.mainloop()
