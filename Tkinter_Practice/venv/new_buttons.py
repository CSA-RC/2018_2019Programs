from tkinter import *

root = Tk()

class App:

    def __init__(self, master):

        master.title("The colored buttons window!")

        self.textframe = Frame(master)
        self.textframe.pack()

        bluebuttonframe = Frame(master, width=100, height=100)
        bluebuttonframe.pack_propagate(0)
        bluebuttonframe.pack()

        redbuttonframe = Frame(master, width=100, height=100)
        redbuttonframe.pack_propagate(0)
        redbuttonframe.pack()

        label = Label(self.textframe, text="The colored buttons window!")
        label.pack()

        self.button1 = Button(bluebuttonframe, text="BLUE", command=self.button1change, fg="blue", bg="red")
        self.button1.pack(fill=BOTH, expand=1)
        self.b1fg = "blue"
        self.b1bg = "red"

        self.button2 = Button(redbuttonframe, text="RED", command=self.button2change, fg="red", bg="blue")
        self.button2.pack(fill=BOTH, expand=1)
        self.b2fg = "red"
        self.b2bg = "blue"

        master.bind("<Button-1>", lambda x: [
            Label(self.textframe, text="Oh no! You've got a Virus!").pack(),
            master.unbind("<Button-1>")
        ])

    def button1change(self):
        if self.b1fg == "blue":
            self.b1fg = "red"
            self.b1bg = "blue"
            self.button1.config(fg=self.b1fg, bg=self.b1bg)
        elif self.b1fg == "red":
            self.b1fg = "blue"
            self.b1bg = "red"
            self.button1.config(fg=self.b1fg, bg=self.b1bg)


    def button2change(self):
        if self.b2fg == "blue":
            self.b2fg = "red"
            self.b2bg = "blue"
            self.button2.config(fg=self.b2fg, bg=self.b2bg)
        elif self.b2fg == "red":
            self.b2fg = "blue"
            self.b2bg = "red"
            self.button2.config(fg=self.b2fg, bg=self.b2bg)

app = App(root)

root.mainloop()