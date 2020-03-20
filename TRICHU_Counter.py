""" a score counter for trichu game """
from tkinter import Tk, Button, Menu
from tkinter import messagebox as msg
from tkinter import simpledialog
import random
import os 
import csv
import pandas as pd
def helpmenu():
    """ help menu function """
    msg.showinfo("TRICHU COUNTER HELP", "A Counter for trichu game. Enter the name of the players and the ending score")
def aboutmenu():
    """ about menu function """
    msg.showinfo("TRICHU COUNTER ABOUT", "Version 1.0")
class TRICHU_Counter():
    """ Trichu counter class"""
    def __init__(self, master):
        self.nameoftheplayers = ["", "", ""] # names
        self.totalscores = [0, 0, 0] #scores
        self.gamestate = "no end"
        self.filename = ""
        self.master = master
        self.master.title("TRICHU Counter")
        self.master.geometry("200x200")
        self.master.resizable(False, False)
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="New Game", accelerator='ctrl+O', command=self.newgame)
        self.file_menu.add_command(label="Load Game", accelerator='ctrl+l', command=self.loadgame)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.scoremenu = Menu(self.menu, tearoff=0)
        self.scoremenu.add_command(label="Player 1 Total", accelerator='Ctrl+p', command=self.player1score)
        self.scoremenu.add_command(label="Player 2 Total", accelerator='Ctrl+t', command=self.player2score)
        self.scoremenu.add_command(label="Player 3 Total", accelerator='Ctrl+j', command=self.player3score)
        self.scoremenu.add_command(label="Every Round", accelerator='Ctrl+R', command=self.everyround)
        self.menu.add_cascade(label="Score", menu=self.scoremenu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-r>', lambda event: self.everyround())
        self.master.bind('<Control-p>', lambda event: self.player1score())
        self.master.bind('<Control-t>', lambda event: self.player2score())
        self.master.bind('<Control-j>', lambda event: self.player3score())
        self.master.bind('<Control-o>', lambda event: self.newgame())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Control-l>', lambda event: self.loadgame())
    def everyround(self):
        """ shows the score of every round"""
        if self.filename == "":
            msg.showerror("ERROR", "No game created")
        elif self.totalscores[0] == 0 & self.totalscores[1] == 0 & self.totalscores[2] == 0:
            msg.showinfo("GAMES", "NO GAMES PLAYED")
        elif self.gamestate == "Winner":
            msg.showinfo("END", "THERE IS A WINNER")
        else:
            df = pd.read_csv('game'+self.filename+'.csv')
            msg.showinfo("SCORE", str(df))
    def player3score(self):
        """ shows player 3 score """
        if self.filename == "":
            msg.showerror("ERROR", "No game created")
        elif self.totalscores[0] == 0 & self.totalscores[1] == 0 & self.totalscores[2] == 0:
            msg.showinfo("GAMES", "NO GAMES PLAYED")
        elif self.gamestate == "Winner":
            msg.showinfo("END", "THERE IS A WINNER")
        else:
            msg.showinfo("Player 3 score", str(self.totalscores[2]))
    def player2score(self):
        """ shows player 2 score """
        if self.filename == "":
            msg.showerror("ERROR", "No game created")
        elif self.totalscores[0] == 0 & self.totalscores[1] == 0 & self.totalscores[2] == 0:
            msg.showinfo("GAMES", "NO GAMES PLAYED")
        elif self.gamestate == "Winner":
            msg.showinfo("END", "THERE IS A WINNER")
        else:
            msg.showinfo("Player 2 score", str(self.totalscores[1]))
    def player1score(self):
        """ shows player 1 score """
        if self.filename == "":
            msg.showerror("ERROR", "No game created")
        elif self.totalscores[0] == 0 & self.totalscores[1] == 0 & self.totalscores[2] == 0:
            msg.showinfo("GAMES", "NO GAMES PLAYED")
        elif self.gamestate == "Winner":
            msg.showinfo("END", "THERE IS A WINNER")
        else:
            msg.showinfo("Player 1 score", str(self.totalscores[0]))
    def loadgame(self):
        pass
    def newgame(self):
        """ creates a new game"""
        if not os.path.exists("Games"):
            os.mkdir("Games")
        while self.nameoftheplayers[0] is None or self.nameoftheplayers[0] == "":
            self.nameoftheplayers[0] = simpledialog.askstring("Player 1 ", "What is your name?", parent=self.master)    
        while self.nameoftheplayers[1] is None or self.nameoftheplayers[1] == "" or self.nameoftheplayers[1] == self.nameoftheplayers[0]:
            self.nameoftheplayers[1] = simpledialog.askstring("Player 2 ", "What is your name?", parent=self.master)
        while (self.nameoftheplayers[2] is None or self.nameoftheplayers[2] == "" or self.nameoftheplayers[2] == self.nameoftheplayers[1] or self.nameoftheplayers[0] == self.nameoftheplayers[2]):
            self.nameoftheplayers[2] = simpledialog.askstring("Player 3 ", "What is your name?", parent=self.master)
        self.finalscore = simpledialog.askinteger("Winning Score", "What is the winning score?", parent=self.master, minvalue=0, maxvalue=20)
        print(self.nameoftheplayers[0], self.nameoftheplayers[1], self.nameoftheplayers[2])
        while self.finalscore is None:
            self.finalscore = simpledialog.askinteger("Winning Score", "What is the winning score?", parent=self.master, minvalue=0, maxvalue=20)
        self.addround = Button(self.master, text="Add a round", command=self.addr)
        self.addround.pack()
        self.file_menu.entryconfig("New Game", state="disabled")
        msg.showinfo("Game Created", "Game Created")
        os.chdir("Games")
        self.filename = self.nameoftheplayers[0] + str(random.randrange(20, 40))
        with open('game'+str(self.filename)+str('.csv'), 'a+') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([str(self.nameoftheplayers[0]), str(self.nameoftheplayers[1]), str(self.nameoftheplayers[2]), "gamestate"])
    def addr(self):
        """ adds a new round"""
        if self.gamestate == "Winner":
            msg.showinfo("END", "THERE IS A WINNER")
        else: 
            player1score = simpledialog.askinteger("Player1score", "What is the player1score", parent=self.master, minvalue=-2, maxvalue=4)
            while player1score is None:
                player1score = simpledialog.askinteger("Player1score", "What is the player1score", parent=self.master, minvalue=-2, maxvalue=4)
            if player1score >= 2:
                player2score = simpledialog.askinteger("Player2score", "What is the player2score", parent=self.master, minvalue=-2, maxvalue=1)
                while player2score is None:
                    player2score = simpledialog.askinteger("Player2score", "What is the player2score", parent=self.master, minvalue=-2, maxvalue=1)
            else:
                player2score = simpledialog.askinteger("Player2score", "What is the player2score", parent=self.master, minvalue=-2, maxvalue=4)
                while player2score is None:
                    player2score = simpledialog.askinteger("Player2score", "What is the player2score", parent=self.master, minvalue=-2, maxvalue=4)
            if (player2score == 1 or player1score == 1):
                player3score = simpledialog.askinteger("Player3", "What is the player 3 score", parent=self.master, minvalue=-2, maxvalue=0)
                while player3score is None:
                    player3score = simpledialog.askinteger("Player3", "What is the player 3 score", parent=self.master, minvalue=-2, maxvalue=0)
            elif (player1score == 0 or player2score == 0):
                player3score = simpledialog.askinteger("Player 3", "What is the player 3 score ", parent=self.master, minvalue=-2, maxvalue=1)
                while player3score is None:
                    player3score = simpledialog.askinteger("Player 3", "What is the player 3 score ", parent=self.master, minvalue=-2, maxvalue=1)
            else:
                player3score = simpledialog.askinteger("Player 3", "What is the player 3 score ", parent=self.master, minvalue=2, maxvalue=4)
                while player3score is None:
                    player3score = simpledialog.askinteger("Player 3", "What is the player 3 score ", parent=self.master, minvalue=2, maxvalue=4)
            self.totalscores[0] += player1score
            self.totalscores[1] += player2score
            self.totalscores[2] += player3score
            if self.totalscores[0] >= self.finalscore:
                msg.showinfo("WINNER", "WINNER PLAYER 1")
                self.gamestate = "Winner"
            elif self.totalscores[1] >= self.finalscore:
                msg.showinfo("WINNER", "WINNER PLAYER 2")
                self.gamestate = "Winner"
            elif self.totalscores[2] >= self.finalscore:
                msg.showinfo("WINNER", "WINNER PLAYER 3")
                self.gamestate = "Winner"
            with open('game'+str(self.filename)+str('.csv'), 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([str(self.totalscores[0]), str(self.totalscores[1]), str(self.totalscores[2]), self.gamestate])
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main function """
    root = Tk()
    TRICHU_Counter(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
