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
        self.grid_columnconfigure(0, weight=1)
        self.lbl_title_race_pick_label = tk.Label(self, text = "Choosing a Race", 
                                       font = DEFAULT,
                                       bg = 'mint cream')  
        self.lbl_title_race_pick_label.grid(row = 1, column = 0, 
                                            columnspan = 2)
        
        self.btn_race_info = tk.Button(self, text = "Race Information",
                                       font = DEFAULT,
                                       bg = 'ivory',
                                       activebackground = 'MistyRose2',
                                       command = self.raise_races)
        self.btn_race_info.grid(row = 2, column = 0, columnspan = 2)
        
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
        
    def raise_races(self):
        race_info.tkraise()        
    
class Race_Info(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.lbl_race_lbl = tk.Label(self, text = "Race Information", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)
        
        self.lbl_race_dwarf = tk.Label(self, text = '''Dwarf: Dwarves have an appearance similar to humans, 
        if humans were all naturally under 5ft. 
        Dwarves can live over 400 years old. Tiny but mighty, 
        they are skilled warriors in battle. They stand around 4 to  
        5ft tall and weigh around 150. Hardy 
        creatures, your constitution (vitality) score increases by 2 
        when you are a dwarf.''', 
                                       font = ('Arial', 18),
                                       bg = 'mint cream')  
        self.lbl_race_dwarf.grid(row = 2, column = 0)
        
        self.lbl_race_dwarf = tk.Label(self, text = '''Elf: Elves are graceful creatures. 
        They live for centuries and hold 
        vast knowledge of the world around them. 
        Elves can live to be 750 years old. 
        They are, on average, 5 or over 6 ft
        tall. Their weight is similar to a human's. 
        As an elf your dexterity (agility) increases by 2.''', 
                                       font = ('Arial', 18),
                                       bg = 'mint cream')  
        self.lbl_race_dwarf.grid(row = 3, column = 0) 
        
        self.lbl_race_halfling= tk.Label(self, text = '''Halfling: Halflings are shorter than dwarves. 
        They are skilled in fitting into communities and
        are fiercely loyal to their allies. 
        They reach adulthood around the age of 20 
        and live into the
        middle of their second century. 
        On average halflings stand about 
        3 ft tall and weigh 40 pounds.
        As a halfling your dexterity (agility) increases by 2. ''', 
                                       font = ('Arial', 18),
                                       bg = 'mint cream')  
        self.lbl_race_halfling.grid(row = 4, column = 0) 
        
        self.lbl_race_human= tk.Label(self, text = '''Human: The most recognizable race, humans are adaptable 
        and ambitious. Because of their shorter
        life spans, they do not hesitate to seize the moment. 
        Humans live less than a century. Their height
        and weight vary greatly, from being 5 to over 6 ft tall 
        and 100 to 200 pounds or more. As a human,
        each of your ability scores increase by one.''', 
                                       font = ('Arial', 18),
                                       bg = 'mint cream')  
        self.lbl_race_human.grid(row = 5, column = 0)
        
        self.btn_continue= tk.Label(self, text = "Continue",
                                        font = DEFAULT, 
                                        command = self.raise_races_2, 
                                        bg = 'ivory', 
                                        activebackground = 'MistyRose2')  
        self.btn_continue.grid(row = 6, column = 0)
              

        def raise_races_2(self):
            race_info2.tkraise()
            
        
class Race_Info2(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.lbl_race_lbl = tk.Label(self, text = "Race Information Cont.", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)        
        
    
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

race_info = Race_Info()
race_info.grid(row = 0, column = 0, sticky = "news")

race_info2 = Race_Info2()
race_info2.grid(row = 0, column = 0, sticky = "news")


frame_menu.tkraise()
root.mainloop()