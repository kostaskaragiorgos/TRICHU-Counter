from tkinter import *
from tkinter import messagebox as msg
from tkinter import simpledialog
import random
import os 
import csv
import pandas as pd
class TRICHU_Counter():
    def __init__(self,master):
        self.totalscorep1 = 0
        self.totalscorep2 = 0
        self.totalscorep3 = 0
        self.gamestate = "no end"
        self.winnerflag = 0
        self.filename = ""
        self.master = master
        self.master.title("TRICHU Counter")
        self.master.geometry("200x200")
        self.master.resizable(False,False)
        
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "New Game",accelerator = 'ctrl+O',command = self.newgame)
        self.file_menu.add_command(label = "Load Game",accelerator = 'ctrl+l',command = self.loadgame)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.scoremenu = Menu(self.menu,tearoff = 0)
        self.scoremenu.add_command(label = "Player 1 Total",accelerator = 'Ctrl+p',command = self.player1score)
        self.scoremenu.add_command(label = "Player 2 Total",accelerator = 'Ctrl+t',command = self.player2score)
        self.scoremenu.add_command(label = "Player 3 Total",accelerator = 'Ctrl+j',command = self.player3score)
        self.scoremenu.add_command(label = "Every Round",accelerator = 'Ctrl+R',command = self.everyround)
        self.menu.add_cascade(label = "Score",menu = self.scoremenu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Control-r>',lambda event:self.everyround())
        self.master.bind('<Control-p>',lambda event:self.player1score())
        self.master.bind('<Control-t>',lambda event:self.player2score())
        self.master.bind('<Control-j>',lambda event:self.player3score())
        self.master.bind('<Control-o>',lambda event:self.newgame())
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        self.master.bind('<Control-l>',lambda event:self.loadgame())
        
   
    def everyround(self):
        if self.filename == "":
            msg.showerror("ERROR" , "No game created")
            
        elif self.totalscorep1 == 0 & self.totalscorep2 == 0 & self.totalscorep3 == 0:
            msg.showinfo("GAMES", "NO GAMES PLAYED")
        elif self.gamestate == "Winner":
            msg.showinfo("END","THERE IS A WINNER")
        else:
            df = pd.read_csv('game'+self.filename+'.csv')
            msg.showinfo("SCORE",str(df))
    
    def player3score(self):
        if self.filename == "":
            msg.showerror("ERROR" , "No game created")
        elif self.totalscorep1 == 0 & self.totalscorep2 == 0 & self.totalscorep3 == 0:
            msg.showinfo("GAMES", "NO GAMES PLAYED")
        elif self.gamestate == "Winner":
            msg.showinfo("END","THERE IS A WINNER")
        else:
            msg.showinfo("Player 3 score",str(self.totalscorep3))
        
    def player2score(self):
        if self.filename == "":
            msg.showerror("ERROR" , "No game created")
        elif self.totalscorep1 == 0 & self.totalscorep2 == 0 & self.totalscorep3 == 0:
            msg.showinfo("GAMES", "NO GAMES PLAYED")
        elif self.gamestate == "Winner":
            msg.showinfo("END","THERE IS A WINNER")
        else:
            msg.showinfo("Player 2 score",str(self.totalscorep2))
            
    def player1score(self):
        if self.filename == "":
            msg.showerror("ERROR" , "No game created")
        elif self.totalscorep1 == 0 & self.totalscorep2 == 0 & self.totalscorep3 == 0:
            msg.showinfo("GAMES", "NO GAMES PLAYED")
        elif self.gamestate == "Winner":
            msg.showinfo("END","THERE IS A WINNER")
        else:
            msg.showinfo("Player 1 score",str(self.totalscorep1))
        
        
    
    def loadgame(self):
        pass
    
    def newgame(self):
        if os.path.exists("Games") == False:
            os.mkdir("Games")
        player1name = simpledialog.askstring("Player 1 ","What is your name?",parent = self.master)
        
        while player1name == None or player1name == "":
            player1name = simpledialog.askstring("Player 1 ","What is your name?",parent = self.master)    
        
        player2name = simpledialog.askstring("Player 2 ","What is your name?",parent = self.master)
        
        while (player2name == None or player2name == "") or player2name == player1name :
            player2name = simpledialog.askstring("Player 2 ","What is your name?",parent = self.master)
            
        player3name = simpledialog.askstring("Player 3 ","What is your name?",parent = self.master)
       
        while (player3name == None or player3name == "") or (player3name == player2name or player1name == player3name):
            player3name = simpledialog.askstring("Player 3 ","What is your name?",parent = self.master)
            
        self.finalscore = simpledialog.askinteger("Winning Score","What is the winning score?",parent = self.master,minvalue = 0,maxvalue =20)
        while self.finalscore == None:
            self.finalscore = simpledialog.askinteger("Winning Score","What is the winning score?",parent = self.master,minvalue = 0,maxvalue =20)
        self.addround = Button(self.master,text = "Add a round",command= self.addr)
        self.addround.pack()
        self.file_menu.entryconfig("New Game", state="disabled")
        msg.showinfo("Game Created","Game Created")
        os.chdir("Games")
        self.filename = player1name + str(random.randrange(20, 40))
        with open('game'+str(self.filename)+str('.csv'), 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([str(player1name),str(player2name),str(player3name),"gamestate"])
    
    def addr(self):
        if self.gamestate == "Winner":
            msg.showinfo("END","THERE IS A WINNER")
        else: 
            player1score = simpledialog.askinteger("Player1score","What is the player1score",parent = self.master,minvalue = -2,maxvalue = 4)
            
            while player1score == None:
                player1score = simpledialog.askinteger("Player1score","What is the player1score",parent = self.master,minvalue = -2,maxvalue = 4)
            
            if player1score >= 2:
                self.winnerflag = 1
            else:
                self.winnerflag = 0
                    
            if self.winnerflag == 1:
                player2score = simpledialog.askinteger("Player2score","What is the player2score",parent = self.master,minvalue = -2,maxvalue=1)
                while player2score == None:
                    player2score = simpledialog.askinteger("Player2score","What is the player2score",parent = self.master,minvalue = -2,maxvalue=1)
            elif self.winnerflag == 0:
                player2score = simpledialog.askinteger("Player2score","What is the player2score",parent = self.master,minvalue = -2,maxvalue=4)
                while player2score == None:
                    player2score = simpledialog.askinteger("Player2score","What is the player2score",parent = self.master,minvalue = -2,maxvalue=4)
            if player2score >= 2:
                self.winnerflag = 1
                
            if self.winnerflag == 1 and(player2score == 1 or player1score ==1):
                player3score = simpledialog.askinteger("Player3","What is the player 3 score",parent = self.master,minvalue = -2,maxvalue = 0)
                while player3score == None:
                    player3score = simpledialog.askinteger("Player3","What is the player 3 score",parent = self.master,minvalue = -2,maxvalue = 0)
            elif self.winnerflag == 1 and(player1score == 0 or player2score == 0):
                player3score = simpledialog.askinteger("Player 3","What is the player 3 score ", parent = self.master,minvalue = -2 ,maxvalue = 1)
                while player3score == None:
                    player3score = simpledialog.askinteger("Player 3","What is the player 3 score ", parent = self.master,minvalue = -2 ,maxvalue = 1)
            else:
                player3score = simpledialog.askinteger("Player 3","What is the player 3 score ", parent = self.master,minvalue = 2 ,maxvalue = 4)
                while player3score == None:
                    player3score = simpledialog.askinteger("Player 3","What is the player 3 score ", parent = self.master,minvalue = 2 ,maxvalue = 4)
            with open('game'+str(self.filename)+str('.csv'), 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([str(player1score),str(player2score),str(player3score),self.gamestate])
                f.close()
            self.totalscorep1 = self.totalscorep1 + player1score 
            self.totalscorep2 =self.totalscorep2 + player2score
            self.totalscorep3 =self.totalscorep3 + player3score
            
            if self.totalscorep1 >= self.finalscore:
                msg.showinfo("WINNER","WINNER PLAYER 1")
                self.gamestate = "Winner"
                with open('game'+str(self.filename)+str('.csv'), 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow([str(self.totalscorep1),str(self.totalscorep2),str(self.totalscorep3),self.gamestate])
                    
            elif self.totalscorep2 >= self.finalscore:
                msg.showinfo("WINNER","WINNER PLAYER 2")
                self.gamestate = "Winner"
                with open('game'+str(self.filename)+str('.csv'), 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow([str(self.totalscorep1),str(self.totalscorep2),str(self.totalscorep3),self.gamestate])
                    
            elif self.totalscorep3 >= self.finalscore:
                msg.showinfo("WINNER","WINNER PLAYER 3")
                self.gamestate = "Winner"
                with open('game'+str(self.filename)+str('.csv'), 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow([str(self.totalscorep1),str(self.totalscorep2),str(self.totalscorep3),self.gamestate])

        
            
            
        
                
            
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        msg.showinfo("TRICHU COUNTER HELP","A Counter for trichu game. Enter the name of the players and the ending score")
   
    def aboutmenu(self):
        msg.showinfo("TRICHU COUNTER ABOUT","Version 1.0")
        
    


def main():
    root=Tk()
    TC = TRICHU_Counter(root)
    root.mainloop()
    
if __name__=='__main__':
    main()
