#!/usr/bin/python3
#LaneDoyle
#12/3/19

import tkinter as tk
import sys as sys

DEFAULT = ('Arial', 25)
#Creating Main Menu
class Main_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_main_label = tk.Label(self, text = "Main Menu", 
                                       font = DEFAULT, bg = 'mint cream')
        self.lbl_main_label.grid(row = 0, column = 0)
        
        self.btn_start_button = tk.Button(self, text = "START!",
                                            font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2',
                                            command = self.raise_start)
        self.btn_start_button.grid(row = 1, column = 0)
        
        self.btn_races_button = tk.Button(self, text = "Available Races",
                                            font = DEFAULT, command =
                                            self.raise_races, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_races_button.grid(row = 2, column = 0)   
        
        self.btn_classes_button = tk.Button(self, text = "Available Classes",
                                            font = DEFAULT, command =
                                            self.raise_class, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_classes_button.grid(row = 3, column = 0)          
        
        self.btn_dice_button = tk.Button(self, text = "Dice",
                                            font = DEFAULT, command =
                                            self.raise_dice, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_dice_button.grid(row = 4, column = 0) 
        
        self.btn_exit_button = tk.Button(self, text = "Exit",
                                            font = DEFAULT, command = self.cancel, 
                                            bg = 'ivory', 
                                            activebackground = 'MistyRose2')
        self.btn_exit_button.grid(row = 5, column = 0) 
        
    def cancel(self):
        sys.exit()
    
    def raise_races(self):
        available_race.tkraise()
        
    def raise_class(self):
        available_class.tkraise()  
    
    def raise_start(self):
        start.tkraise()    
    
    def raise_dice(self):
        dice.tkraise()
        
class Race_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_races_label = tk.Label(self, text = "Races", 
                                       font = DEFAULT, bg = 'mint cream')
        self.lbl_races_label.grid(row = 0, column = 0)
        
        self.lbl_race_label1 = tk.Label(self, text = "Dwarf, Elf, Halfling, Human,", 
                                       font = DEFAULT, bg = 'mint cream')
        self.lbl_race_label1.grid(row = 1, column = 0) 
        
        
        self.lbl_race_label2 = tk.Label(self, text = "Dragonborn, Gnomes, Half-Elf,", 
                                       font = DEFAULT, bg = 'mint cream')
        self.lbl_race_label2.grid(row = 2, column = 0) 
        
        
        self.lbl_race_label3 = tk.Label(self, text = "Half-Orc, and Tiefling", 
                                       font = DEFAULT, bg = 'mint cream')
        self.lbl_race_label3.grid(row = 3, column = 0) 
             
        self.btn_back_button = tk.Button(self, text = "Back",
                                            font = DEFAULT, command = 
                                            self.raise_menu, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_back_button.grid(row = 4, column = 0)
    
    def raise_menu(self):
        frame_menu.tkraise()
        
class Class_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_classes_label = tk.Label(self, text = "Classes", 
                                       font = DEFAULT, 
                                       bg = 'mint cream')
        self.lbl_classes_label.grid(row = 0, column = 0)
        
        self.lbl_class_label1 = tk.Label(self, text = "Available classes:",
                                         font = DEFAULT, bg = 'mint cream')
        self.lbl_class_label1.grid(row = 1, column = 0)
        
        
        self.lbl_class_label2 = tk.Label(self, text = "Barbarian, Bard, Cleric",
                                         font = DEFAULT, bg = 'mint cream')
        self.lbl_class_label2.grid(row = 2, column = 0)
        
        self.lbl_class_label3 = tk.Label(self, text = "Druid, Fighter, Monk",
                                         font = DEFAULT, bg = 'mint cream')
        self.lbl_class_label3.grid(row = 3, column = 0)
        
        self.lbl_class_label4 = tk.Label(self, text = "Paladin, Ranger, Rogue",
                                         font = DEFAULT, bg = 'mint cream')
        self.lbl_class_label4.grid(row = 4, column = 0)
        
        self.lbl_class_label5 = tk.Label(self, text = "Sorcerer, Warlock, Wizard",
                                         font = DEFAULT, bg = 'mint cream')
        self.lbl_class_label5.grid(row = 5, column = 0)
        
        self.btn_back_button = tk.Button(self, text = "Back",
                                            font = DEFAULT, command = 
                                            self.raise_menu, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_back_button.grid(row = 6, column = 0)
    
    def raise_menu(self):
        frame_menu.tkraise()
        
class Dice(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_title_dice_label = tk.Label(self, text = "Dice", 
                                       font = DEFAULT,
                                       bg = 'mint cream')
        self.lbl_title_dice_label.grid(row = 0, column = 0)
        
        self.lbl_dice_label1 = tk.Label(self, text = "1d4- a four sided die using 1-4.",
                                       font = DEFAULT, bg = 'mint cream')
        self.lbl_dice_label1.grid(row = 1, column = 0) 
        
        
        self.lbl_dice_label2 = tk.Label(self, text = "1d6- a six sided die using 1-6.",
                                       font = DEFAULT, bg = 'mint cream')
        self.lbl_dice_label2.grid(row = 2, column = 0) 
        
        
        self.lbl_dice_label3 = tk.Label(self, text = "1d8- an eight sided die using 1-8.",
                                       font = DEFAULT, bg = 'mint cream')
        self.lbl_dice_label3.grid(row = 3, column = 0) 
        
        
        self.lbl_dice_label4 = tk.Label(self, text = "1d12- a twelve sided die using 1-12.",
                                       font = DEFAULT, bg = 'mint cream')
        self.lbl_dice_label4.grid(row = 4, column = 0) 
        
        
        self.lbl_dice_label5 = tk.Label(self, text = " 1d20- a twenty sided die using 1-20.",
                                       font = DEFAULT, bg = 'mint cream')
        self.lbl_dice_label5.grid(row = 5, column = 0)         
        
        self.btn_back_button = tk.Button(self, text = "Back",
                                            font = DEFAULT, command = 
                                            self.raise_menu, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_back_button.grid(row = 6, column = 0)
    
    def raise_menu(self):
        frame_menu.tkraise()
#End of Main Menu

#BEGINNING OF ACTUAL PROGRAM        
class Start(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.lbl_title_race_pick_label = tk.Label(self, text = "Choosing a Race", 
                                       font = DEFAULT,
                                       bg = 'mint cream')  
        self.lbl_title_race_pick_label.grid(row = 1, column = 0,
                                            columnspan = 2)
        
        self.btn_race_info = tk.Button(self, text = "Race Information",
                                       font = DEFAULT,
                                       bg = 'ivory',
                                       activebackground = 'MistyRose2')
        self.btn_race_info.grid(row = 2, column = 0)
        self.lbl_race_pick = tk.Label(self, text = "Please enter your race:",
                                      font = DEFAULT, bg = 'mint cream')
        self.lbl_race_pick.grid(row = 3, column = 0)
        self.ent_race_pick = tk.Entry(self, font = DEFAULT)
        self.ent_race_pick.grid(row = 3, column = 1)
        self.btn_exit_button = tk.Button(self, text = "Exit",
                                            font = DEFAULT, command = self.cancel, 
                                            bg = 'ivory', 
                                            activebackground = 'MistyRose2')
        self.btn_exit_button.grid(row = 4, column = 0, columnspan = 2) 
        
    def cancel(self):
        sys.exit()        


    
#Creating the frames
root = tk.Tk()
root.title("DND Character Creator")

frame_menu = Main_Menu()
frame_menu.grid(row = 0, column = 0, sticky = "news")

available_race = Race_Menu()
available_race.grid(row = 0, column = 0, sticky = "news")

available_class = Class_Menu()
available_class.grid(row = 0, column = 0, sticky = "news")

dice = Dice()
dice.grid(row = 0, column = 0, sticky = "news")

start = Start()
start.grid(row = 0, column = 0, sticky = "news")



frame_menu.tkraise()
root.mainloop()