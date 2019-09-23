from tkinter import *

root = Tk()

class Game:

    def __init__(self, master):

        master.title("TIC-TAC-TOE")

        displayframe = Frame(master, width=70, height=100)
        displayframe.pack_propagate(0)
        displayframe.pack()

        playframe = Frame(master, width = 300, height = 300)
        playframe.pack_propagate(0)
        playframe.pack()

        self.counter = IntVar()
        self.counter.set(1)

        self.playturn = "none"

        self.displaytext = StringVar()
        self.displaytext.set("It is " + self.playturn +"'s turn.") """put in seperate method""""


        self.display = Label(displayframe, textvariable=self.displaytext)
        self.display.pack()

    def turncounter(self):
        self.counter += 1

    def getplayturn(self):
        countertest = self.counter.int
        if (countertest % 2)==1:
            self.playturn = "X"
        elif (countertest % 2)==0:
            self.playturn = "O"








game = Game(root)
root.mainloop()
root.destroy()