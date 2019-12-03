#!/usr/bin/python3
#LaneDoyle
#12/3/19

import tkinter as tk
import sys as sys

DEFAULT = ('Times New Roman', 30)

class Main_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_main_label = tk.Label(self, text = "Main Menu", 
                                       font = DEFAULT)
        self.lbl_main_label.grid(row = 0, column = 0)
        
        self.btn_classes_button = tk.Button(self, text = "START!",
                                            font = DEFAULT)
        self.btn_classes_button.grid(row = 1, column = 0)
        
        self.btn_classes_button = tk.Button(self, text = "Available Races",
                                            font = DEFAULT, command =
                                            self.raise_races)
        self.btn_classes_button.grid(row = 2, column = 0)   
        
        self.btn_classes_button = tk.Button(self, text = "Available Classes",
                                            font = DEFAULT, command =
                                            self.raise_class)
        self.btn_classes_button.grid(row = 3, column = 0) 
        
        self.btn_classes_button = tk.Button(self, text = "Help",
                                            font = DEFAULT)
        self.btn_classes_button.grid(row = 4, column = 0)          
        
        self.btn_classes_button = tk.Button(self, text = "Dice",
                                            font = DEFAULT)
        self.btn_classes_button.grid(row = 5, column = 0) 
        
        self.btn_classes_button = tk.Button(self, text = "Exit",
                                            font = DEFAULT, command = self.cancel)
        self.btn_classes_button.grid(row = 6, column = 0) 
        
    def cancel(self):
        sys.exit()
    
    def raise_races(self):
        available_race.tkraise()
        
    def raise_class(self):
        available_class.tkraise()  
    
    def raise_start(self):
        start.tkraise()
    
    def raise_help(self):
        help.tkraise()    
    
    def raise_dice(self):
        dice.tkraise()
        
class Race_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_main_label = tk.Label(self, text = "Races", 
                                       font = DEFAULT)
        self.lbl_main_label.grid(row = 0, column = 0)
        
        self.lbl_main_label = tk.Label(self, text = ''' 
        Available races: 
        Dwarf, Elf, Halfling, Human, 
        Dragonborn, Gnomes, Half-Elf, 
        Half-Orc, and Tiefling''', 
        font = DEFAULT)
        self.lbl_main_label.grid(row = 1, column = 0)        
        
        self.btn_classes_button = tk.Button(self, text = "Back",
                                            font = DEFAULT, command = 
                                            self.raise_menu)
        self.btn_classes_button.grid(row = 2, column = 0)
    
    def raise_menu(self):
        frame_menu.tkraise()
        
class Class_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_main_label = tk.Label(self, text = "Classes", 
                                       font = DEFAULT)
        self.lbl_main_label.grid(row = 0, column = 0)
        
        self.lbl_main_label = tk.Label(self, text = ''' 
        Available classes: 
        Barbarian
        Bard
        Cleric
        Druid
        Fighter
        Monk
        Paladin
        Ranger
        Rogue
        Sorcerer
        Warlock
        Wizard''', 
        font = DEFAULT)
        self.lbl_main_label.grid(row = 1, column = 0)        
        
        self.btn_classes_button = tk.Button(self, text = "Back",
                                            font = DEFAULT, command = 
                                            self.raise_menu)
        self.btn_classes_button.grid(row = 2, column = 0)
    
    def raise_menu(self):
        frame_menu.tkraise()
         
    
#Creating the frames
root = tk.Tk()
root.title("DND Character Creator")

frame_menu = Main_Menu()
frame_menu.grid(row = 0, column = 0, sticky = "news")

available_race = Race_Menu()
available_race.grid(row = 0, column = 0, sticky = "news")

available_class = Class_Menu()
available_class.grid(row = 0, column = 0, sticky = "news")


frame_menu.tkraise()
root.mainloop()