from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
from tkinter import simpledialog

import os 
import csv
class TRICHU_Counter():
    def __init__(self,master):
        self.totalscorep1 = 0
        self.totalscorep2 = 0
        self.totalscorep3 = 0
        
        self.winnerflag = 0
        
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
        self.scoremenu.add_command(label = "Player 1",accelerator = 'Ctrl+1',command = self.player1score)
        self.scoremenu.add_command(label = "Player 2",accelerator = 'Ctrl+2',command = self.player2score)
        self.scoremenu.add_command(label = "Player 3",accelerator = 'Ctrl+3',command = self.player3score)
        self.menu.add_cascade(label = "Score",menu = self.scoremenu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        
        self.master.bind('<Control-1>',lambda event:self.player1score())
        self.master.bind('<Control-2>',lambda event:self.player2score())
        self.master.bind('<Control-3>',lambda event:self.player3score())
        self.master.bind('<Control-o>',lambda event:self.newgame())
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        self.master.bind('<Control-l>',lambda event:self.loadgame())
   
    def player3score(self):
        msg.showinfo("Player 3 score",str(self.totalscorep3))
        
    def player2score(self):
        msg.showinfo("Player 2 score",str(self.totalscorep2))
    
    def player1score(self):
        msg.showinfo("Player 1 score",str(self.totalscorep1))
    
    def loadgame(self):
        pass
    
    def newgame(self):
        self.i = 0
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
        with open('game'+str(self.i)+str('.csv'), 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([str(player1name),str(player2name),str(player3name)])
                f.close()
        self.i =+1
    
    def addr(self):
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

        with open('game'+str(self.i-1   )+str('.csv'), 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([str(player1score),str(player2score),str(player3score)])
                f.close()
        self.totalscorep1 = self.totalscorep1 + player1score 
        self.totalscorep2 =self.totalscorep2 + player2score
        self.totalscorep3 =self.totalscorep3 + player3score
        
        if self.totalscorep1 >= self.finalscore:
            msg.showinfo("WINNER","WINNER PLAYER 1")
        elif self.totalscorep2 >= self.finalscore:
            msg.showinfo("WINNER","WINNER PLAYER 2")
        elif self.totalscorep3 >= self.finalscore:
            msg.showinfo("WINNER","WINNER PLAYER 3")
            
        
                
            
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        pass
   
    def aboutmenu(self):
        pass
    


def main():
    root=Tk()
    TC = TRICHU_Counter(root)
    root.mainloop()
    
if __name__=='__main__':
    main()