from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
from tkinter import simpledialog

import os 
import csv
class TRICHU_Counter():
    def __init__(self,master):
        self.loserflag = 0
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
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        
        self.master.bind('<Control-o>',lambda event:self.newgame())
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        self.master.bind('<Control-l>',lambda event:self.loadgame())
    
    def loadgame(self):
        '''
        after succ load
        '''
        self.addround = Button(self.master,text = "Add a round")
        self.addround.pack()
    
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
            
        finalscore = simpledialog.askinteger("Winning Score","What is the winning score?",parent = self.master,minvalue = 0,maxvalue =20)
        while finalscore == None:
            finalscore = simpledialog.askinteger("Winning Score","What is the winning score?",parent = self.master,minvalue = 0,maxvalue =20)
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
            self.loserflag = 1
        
        if self.winnerflag == 1:
            player2score = simpledialog.askinteger("Player2score","What is the player2score",parent = self.master,minvalue = -2,maxvalue=1)
            while player2score == None:
                player2score = simpledialog.askinteger("Player2score","What is the player2score",parent = self.master,minvalue = -2,maxvalue=1)
        else:
             player2score = simpledialog.askinteger("Player2score","What is the player2score",parent = self.master,minvalue = -2,maxvalue=4)
             while player2score == None:
                 player2score = simpledialog.askinteger("Player2score","What is the player2score",parent = self.master,minvalue = -2,maxvalue=4)
        if player2score >= 2:
            self.winnerflag = 1
        if self.winnerflag == 1 and(player2score == 1 or player1score ==1):
            player3score = simpledialog.askinteger("Player3","What is the player 3 score",parent = self.master,minvalue = -2,maxvalue = 0)
            while player3score == None:
                player3score = simpledialog.askinteger("Player3","What is the player 3 score",parent = self.master,minvalue = -2,maxvalue = 0)
        else:
            player3score = simpledialog.askinteger("Player 3","What is the player 3 score ", parent = self.master,minvalue = 2 ,maxvalue = 4)
            while player3score == None:
                player3score = simpledialog.askinteger("Player 3","What is the player 3 score ", parent = self.master,minvalue = 2 ,maxvalue = 4)
                    
                
            
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