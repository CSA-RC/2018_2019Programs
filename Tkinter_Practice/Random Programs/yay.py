from tkinter import *

root = Tk()

class App:

    def __init__(self, master):

        master.title("Yay! Program")

        textframe = Frame(master)
        textframe.pack()

        buttframe = Frame(master, width=100, height=300)
        buttframe.pack_propagate(0)
        buttframe.pack(side=LEFT)


        self.text = StringVar()
        self.text.set("Hello")

        self.label = Label(textframe, textvariable=self.text, width=40)
        self.label.pack()

        self.yay = Button(buttframe, text="Yay", command=self.yaytext)
        self.yay.pack(fill=BOTH, expand=1)

        self.boo = Button(buttframe, text="Boo", command=self.bootext)
        self.boo.pack(fill=BOTH, expand=1)

        self.happy = Button(buttframe, text="I'm Happy", command=self.happytext)
        self.happy.pack(fill=BOTH, expand=1)

    def yaytext(self):
        self.text.set("Yay!")

    def bootext(self):
        self.text.set("Boo!")

    def happytext(self):
        self.text.set("My name is Ryan, I'm really, really, really happy!!!!!!!!")


app = App(root)
root.mainloop()