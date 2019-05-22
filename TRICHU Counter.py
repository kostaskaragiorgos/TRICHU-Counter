from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
from tkinter import simpledialog

class TRICHU_Counter():
    def __init__(self,master):
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
        self.addround = Button(self.master,text = "Add a round")
        self.addround.pack()
        
        msg.showinfo("Game Created","Game Created")
        
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