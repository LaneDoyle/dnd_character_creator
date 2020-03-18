#!/usr/bin/python3
#LaneDoyle
#12/3/19

import tkinter as tk
import dieroller as dr
from tkinter.scrolledtext import ScrolledText

#Styles Constants
DEFAULT = ('Arial', 25)
FRMBACKGROUND = "PaleTurquoise1"
BTNBACKGROUNDSTATIC = "LightCyan2"
BTNBACKGROUNDACTIVE = "LightCyan3"

#Lists
available_races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", 
                  "Gnome", "Half-Elf", "Orc", "Tiefling"]

available_classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", 
                     "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", 
                     "Warlock", "Wizard"]

race_index = 0
class_index = 0



class MainScreens(tk.Frame):
    current = 0 
    def __init__(self):
        tk.Frame.__init__(self, bg = FRMBACKGROUND)
    
    def switch_frame():
        mainscreens[MainScreens.current].tkraise()
        
class GenericPopup(tk.Frame):
    def __init__(self, parent, msg =  "generic"):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        self.lbl_continue = tk.Label(self, text = msg, bg = FRMBACKGROUND)
        self.lbl_continue.grid(row = 0, column = 0)
        
        self.btn_ok = tk.Button(self, text = "Ok", 
                                command = self.parent.destroy,
                                bg = BTNBACKGROUNDSTATIC,
                                activebackground = BTNBACKGROUNDACTIVE)
        self.btn_ok.grid(row = 1, column = 0)
        
class YesNoPopup(tk.Frame):
    def __init__(self, parent, msg =  "generic"):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        self.lbl_continue = tk.Label(self, text = msg, bg = FRMBACKGROUND)
        self.lbl_continue.grid(row = 0, column = 0, columnspan = 2)
        
        self.btn_ok = tk.Button(self, text = "Yes", 
                                command = self.yes,
                                bg = BTNBACKGROUNDSTATIC,
                                activebackground = BTNBACKGROUNDACTIVE)
        self.btn_ok.grid(row = 1, column = 0)  
        
        self.btn_ok = tk.Button(self, text = "No", 
                                command = self.no,
                                bg = BTNBACKGROUNDSTATIC,
                                activebackground = BTNBACKGROUNDACTIVE)
        self.btn_ok.grid(row = 1, column = 1)  
        
    def yes(self):
        self.decision = True
        self.parent.destroy()

    def no(self):
        self.decision = False
        self.parent.destroy()
            
        
class MainMenu(MainScreens):
    def __init__(self):
        MainScreens.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        self.volos = ""
        self.lbl_main = tk.Label(self, text = "Main Menu", 
                                       font = DEFAULT, bg = FRMBACKGROUND)
        self.lbl_main.grid(row = 0, column = 0)
        
        self.btn_start = tk.Button(self, text = "START!",
                                            font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE,
                                            command = self.raise_start)
        self.btn_start.grid(row = 1, column = 0)
        
        self.btn_races = tk.Button(self, text = "Available Races",
                                            font = DEFAULT, command =
                                            self.raise_races, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE)
        self.btn_races.grid(row = 2, column = 0)   
        
        self.btn_classes = tk.Button(self, text = "Available Classes",
                                            font = DEFAULT, command =
                                            self.raise_class, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE)
        self.btn_classes.grid(row = 3, column = 0)          
        
        self.btn_exit = tk.Button(self, text = "Exit",
                                            font = DEFAULT, command = self.cancel, 
                                            bg = BTNBACKGROUNDSTATIC, 
                                            activebackground = BTNBACKGROUNDACTIVE)
        self.btn_exit.grid(row = 4, column = 0) 
        
    def cancel(self):
        exit()
    
    def raise_races(self):
        MainScreens.current = 1
        MainScreens.switch_frame()       
        
    def raise_class(self):
        MainScreens.current = 2
        MainScreens.switch_frame()

    def raise_start(self):
        RaceScreens.current = 0
        RaceScreens.switch_frame()        

class RaceMenu(MainScreens):
    def __init__(self):
        MainScreens.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        self.lbl_races = tk.Label(self, text = "Available Races", 
                                       font = DEFAULT, bg = FRMBACKGROUND)
        self.lbl_races.grid(row = 0, column = 0)
        
        self.scr_races = ScrolledText(self, height = 8, width = 40, font = DEFAULT, wrap = 'word')
        self.scr_races.grid(row = 1, column = 0, columnspan = 2, sticky = "news")        
                
        self.btn_back = tk.Button(self, text = "Back",
                                            font = DEFAULT, command = 
                                            self.raise_main, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE)
        self.btn_back.grid(row = 2, column = 0)
        
        for race in available_races:  
            global race_index
            self.scr_races.insert("insert", available_races[race_index] + "\n")
            race_index += 1
        race_index = 0
            
    def raise_main(self):
        MainScreens.current = 0
        MainScreens.switch_frame()  
        
class ClassMenu(MainScreens):
    def __init__(self):
        MainScreens.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        self.lbl_classes_label = tk.Label(self, text = "Available Classes", 
                                       font = DEFAULT, 
                                       bg = FRMBACKGROUND)
        self.lbl_classes_label.grid(row = 0, column = 0)
        
        self.scr_classes = ScrolledText(self, height = 8, width = 40, font = DEFAULT, wrap = 'word')
        self.scr_classes.grid(row = 1, column = 0, columnspan = 2, sticky = "news")          

        
        self.btn_back_button = tk.Button(self, text = "Back",
                                            font = DEFAULT, command = 
                                            self.raise_menu, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE)
        self.btn_back_button.grid(row = 2, column = 0)
        
        for race in available_classes:  
            global class_index
            self.scr_classes.insert("insert", available_classes[class_index] + "\n")
            class_index += 1        
    
    def raise_menu(self):
        MainScreens.current = 0
        MainScreens.switch_frame()
            
            
class RaceScreens(tk.Frame):
    current = 0 
    def __init__(self):
        tk.Frame.__init__(self, bg = FRMBACKGROUND)
    
    def switch_frame():
        racescreens[RaceScreens.current].tkraise()

class Start(RaceScreens):
    def __init__(self):
        RaceScreens.__init__(self)
        
        self.race_chosen = tk.IntVar()
        self.strength = 0
        self.dex = 0
        self.con = 0
        self.intelligence = 0
        self.wis = 0
        self.cha = 0
        self.languages_known = ""
        self.proficiency = ""
        self.advantages = ""
        self.speed = 0
        
        self.grid_columnconfigure(0, weight=1)
        self.lbl_main = tk.Label(self, text = "Pick a Race:", 
                                       font = DEFAULT, bg = FRMBACKGROUND)
        self.lbl_main.grid(row = 0, column = 0)
        
        self.rad_dwarf = tk.Radiobutton(self, text = "Dwarf", 
                                           bg = FRMBACKGROUND, value = 0, 
                                           variable = self.race_chosen)
        self.rad_dwarf.grid(row = 1, column = 0)
        
        self.rad_elf = tk.Radiobutton(self, text = "Elf", 
                                           bg = FRMBACKGROUND, value = 1, 
                                           variable = self.race_chosen)
        self.rad_elf.grid(row = 2, column = 0)
        
        self.rad_halfling = tk.Radiobutton(self, text = "Halfing", 
                                           bg = FRMBACKGROUND, value = 2,
                                           variable = self.race_chosen)
        self.rad_halfling.grid(row = 3, column = 0)
        
        self.rad_human = tk.Radiobutton(self, text = "Human", 
                                           bg = FRMBACKGROUND, value = 3,
                                           variable = self.race_chosen)
        self.rad_human.grid(row = 4, column = 0)
        
        self.rad_dg = tk.Radiobutton(self, text = "Dragonborn", 
                                           bg = FRMBACKGROUND, value = 4,
                                           variable = self.race_chosen)
        self.rad_dg.grid(row = 5, column = 0)
        
        self.rad_gnome = tk.Radiobutton(self, text = "Gnome", 
                                           bg = FRMBACKGROUND, value = 5,
                                           variable = self.race_chosen)
        self.rad_gnome.grid(row = 6, column = 0)
        
        self.rad_he = tk.Radiobutton(self, text = "Half-Elf", 
                                           bg = FRMBACKGROUND, value = 6,
                                           variable = self.race_chosen)
        self.rad_he.grid(row = 7, column = 0)
        
        self.rad_orc = tk.Radiobutton(self, text = "Orc", 
                                           bg = FRMBACKGROUND, value = 7,
                                           variable = self.race_chosen)
        self.rad_orc.grid(row = 8, column = 0)
        
        self.rad_tief = tk.Radiobutton(self, text = "Tiefling", 
                                           bg = FRMBACKGROUND, value = 8,
                                           variable = self.race_chosen)
        self.rad_tief.grid(row = 9, column = 0)
        
        self.btn_ok = tk.Button(self, text = "OK",
                                            font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE,
                                            command = self.raise_races)
        self.btn_ok.grid(row = 10, column = 0)
        
    def raise_races(self):
        if self.race_chosen.get() == 0:
            self.speed += 25
            self.con += 2
            self.advantages += 'poison, '
            self.proficiency+= 'battleaxe, handaxe, throwing hammer, warhammer, '
            self.proficiency += "smith's tools, brewer's supplies, OR mason's tools, "
            self.proficiency += "History of stonework checks, "
            self.languages_known = 'Dwarven, Common, '
            
            RaceScreens.current = 1
            RaceScreens.switch_frame()
           
            racescreens[1].scr_dwarf.delete(0.0, "end")
            racescreens[1].scr_dwarf.insert("end", "Your Racial Traits:")           
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "\n")            
            racescreens[1].scr_dwarf.insert("end", "Speed: ")
            racescreens[1].scr_dwarf.insert("end", self.speed)
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "Constitution Score: ")
            racescreens[1].scr_dwarf.insert("end", self.con)
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "Advantages: ")
            racescreens[1].scr_dwarf.insert("end", self.advantages)
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "Proficiency: ")
            racescreens[1].scr_dwarf.insert("end", self.proficiency)
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "Languages Known: ")
            racescreens[1].scr_dwarf.insert("end", self.languages_known)
            
        elif self.race_chosen.get() == 1:
            self.dex += 2
            self.speed += 30
            self.proficiency += 'The perception skill'
            self.advantages += 'Charmed, '
            self.languages_known += 'Elvish, Common, '
            
            RaceScreens.current = 2
            RaceScreens.switch_frame()
            
            racescreens[2].scr_elf.delete(0.0, "end")
            racescreens[2].scr_elf.insert("end", "Your Racial Traits:")           
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "\n")            
            racescreens[2].scr_elf.insert("end", "Dexterity Score: ")
            racescreens[2].scr_elf.insert("end", self.dex)
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "Speed: ")
            racescreens[2].scr_elf.insert("end", self.speed)
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "Advantages: ")
            racescreens[2].scr_elf.insert("end", self.advantages)
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "Proficiency: ")
            racescreens[2].scr_elf.insert("end", self.proficiency)
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "Languages Known: ")
            racescreens[2].scr_elf.insert("end", self.languages_known)
            
        elif self.race_chosen.get() == 2:
            self.dex += 1
            self.speed += 25
            self.advantages += 'Fear, '
            self.languages_known += 'Halfling, Common, ' 
            
            RaceScreens.current = 3
            RaceScreens.switch_frame()
            
            racescreens[3].scr_halfling.delete(0.0, "end")
            racescreens[3].scr_halfling.insert("end", "Your Racial Traits:")           
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "\n")            
            racescreens[3].scr_halfling.insert("end", "Dexterity Score: ")
            racescreens[3].scr_halfling.insert("end", self.dex)
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "Speed: ")
            racescreens[3].scr_halfling.insert("end", self.speed)
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "Advantages: ")
            racescreens[3].scr_halfling.insert("end", self.advantages)
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "Languages Known: ")
            racescreens[3].scr_halfling.insert("end", self.languages_known)
        
        elif self.race_chosen.get() == 3:
            RaceScreens.current = 4
            RaceScreens.switch_frame()
            
            self.languages_known += 'Common, One of your choice, '
            self.speed += 30
            
        elif self.race_chosen.get() == 4:
            RaceScreens.current = 4
            RaceScreens.switch_frame()        
            
            
class Dwarf(RaceScreens):
    def __init__(self):
        RaceScreens.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        
        self.lbl_dwarf = tk.Label(self, text = "Dwarf:", 
                                       font = DEFAULT, bg = FRMBACKGROUND)
        self.lbl_dwarf.grid(row = 0, column = 0, columnspan = 3)  
        
        self.scr_dwarf = ScrolledText(self, height = 8, width = 40, font = DEFAULT, wrap = 'word')
        self.scr_dwarf.grid(row = 1, column = 0, columnspan = 3, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel",
                                            font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE,
                                            command = self.cancel)
        self.btn_cancel.grid(row = 2, column = 1, sticky = "news")
        
        self.btn_ok = tk.Button(self, text = "Ok",
                                            font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE,
                                            command = self.raise_subtype)
        self.btn_ok.grid(row = 2, column = 0, sticky = "news")
    
    def cancel(self):
        global CON 
        global SPEED
        global ADVANTAGES
        global PROFICIENCY
        global LANGUAGES_KNOWN
        global DEX
        global STR
        global CHA
        global INT
        CON = 0
        SPEED = 0
        ADVANTAGES = ""
        PROFICIENCY = ""
        LANGUAGES_KNOWN = ""
        DEX = 0
        STR = 0
        CHA = 0
        INT = 0
        RaceScreens.current = 0
        RaceScreens.switch_frame()
    
    def raise_subtype(self):
        pass

class Elf(RaceScreens):
    def __init__(self):
        RaceScreens.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        
        self.lbl_elf = tk.Label(self, text = "Elf:", 
                                       font = DEFAULT, bg = FRMBACKGROUND)
        self.lbl_elf.grid(row = 0, column = 0, columnspan = 3)  
        
        self.scr_elf = ScrolledText(self, height = 8, width = 40, font = DEFAULT, wrap = 'word')
        self.scr_elf.grid(row = 1, column = 0, columnspan = 3, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel",
                                            font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE,
                                            command = self.cancel)
        self.btn_cancel.grid(row = 2, column = 1, sticky = "news")
        
        self.btn_ok = tk.Button(self, text = "Ok",
                                            font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE,
                                            command = self.raise_subtype)
        self.btn_ok.grid(row = 2, column = 0, sticky = "news")
    
    def cancel(self):
        global CON 
        global SPEED
        global ADVANTAGES
        global PROFICIENCY
        global LANGUAGES_KNOWN
        global DEX
        global STR
        global CHA
        global INT
        CON = 0
        SPEED = 0
        ADVANTAGES = ""
        PROFICIENCY = ""
        LANGUAGES_KNOWN = ""
        DEX = 0
        STR = 0
        CHA = 0
        INT = 0
        RaceScreens.current = 0
        RaceScreens.switch_frame()
        
    def raise_subtype(self):
        pass    

class Halfling(RaceScreens):
    def __init__(self):
        RaceScreens.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        
        self.lbl_halfling = tk.Label(self, text = "Halfling:", 
                                       font = DEFAULT, bg = FRMBACKGROUND)
        self.lbl_halfling.grid(row = 0, column = 0, columnspan = 3)  
        
        self.scr_halfling = ScrolledText(self, height = 8, width = 40, font = DEFAULT, wrap = 'word')
        self.scr_halfling.grid(row = 1, column = 0, columnspan = 3, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel",
                                            font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE,
                                            command = self.cancel)
        self.btn_cancel.grid(row = 2, column = 1, sticky = "news")
        
        self.btn_ok = tk.Button(self, text = "Ok",
                                            font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE,
                                            command = self.raise_subtype)
        self.btn_ok.grid(row = 2, column = 0, sticky = "news")
    
    def cancel(self):
        global CON 
        global SPEED
        global ADVANTAGES
        global PROFICIENCY
        global LANGUAGES_KNOWN
        global DEX
        global STR
        global CHA
        global INT
        CON = 0
        SPEED = 0
        ADVANTAGES = ""
        PROFICIENCY = ""
        LANGUAGES_KNOWN = ""
        DEX = 0
        STR = 0
        CHA = 0
        INT = 0
        RaceScreens.current = 0
        RaceScreens.switch_frame()
        
    def raise_subtype(self):
        pass

class HumanPick(RaceScreens):
    def __init__(self):
        RaceScreens.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        self.strength = 0
        self.dex = 0
        self.con = 0
        self.intelligence = 0
        self.wis = 0
        self.cha = 0

        self.sub_chosen = tk.IntVar()
        
        self.lbl_continue = tk.Label(self, text = "Please Pick:", bg = FRMBACKGROUND)
        self.lbl_continue.grid(row = 0, column = 0, columnspan = 2)
        
        self.rad_variant = tk.Radiobutton(self, text = "Variant Human", value = 0, 
                                           variable = self.sub_chosen)
        self.rad_variant.grid(row = 1, column = 0, sticky = "news")
        
        self.rad_regular = tk.Radiobutton(self, text = "Regular Human", value = 1, 
                                           variable = self.sub_chosen)
        self.rad_regular.grid(row = 2, column = 0, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel",
                                            font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE,
                                            command = self.cancel)
        self.btn_cancel.grid(row = 3, column = 1, sticky = "news")
        
        self.btn_ok = tk.Button(self, text = "Ok",
                                            font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE,
                                            command = self.confirmed)
        self.btn_ok.grid(row = 3, column = 0, sticky = "news")
        
    def cancel(self):
        self.strength = 0
        self.dex = 0
        self.con = 0
        self.intelligence = 0
        self.wis = 0
        self.cha = 0
        racescreens[0].speed = 0
        racescreens[0].languages_known = ""
        RaceScreens.current = 0
        RaceScreens.switch_frame()
        
    def confirmed(self):
        if self.sub_chosen.get() == 0:
            RaceScreens.current = 5
            RaceScreens.switch_frame()
        
        elif self.sub_chosen.get() == 1:
            self.strength += 1
            self.dex += 1
            self.con += 1
            self.intelligence += 1
            self.wis += 1
            self.cha += 1                

            racescreens[6].scr_halfling.delete(0.0, "end")
            racescreens[6].scr_halfling.insert("end", "Your Racial Traits:")           
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "\n")            
            racescreens[6].scr_halfling.insert("end", "Strength Score: ")
            racescreens[6].scr_halfling.insert("end", self.strength)
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "Dexterity Score: ")
            racescreens[6].scr_halfling.insert("end", self.dex)
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "Constitution Score: ")
            racescreens[6].scr_halfling.insert("end", self.con)
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "Intelligence Score: ")
            racescreens[6].scr_halfling.insert("end", self.intelligence) 
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "Wisdom Score: ")
            racescreens[6].scr_halfling.insert("end", self.wis) 
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "Charisma Score: ")
            racescreens[6].scr_halfling.insert("end", self.cha) 
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "Speed: ")
            racescreens[6].scr_halfling.insert("end", racescreens[0].speed) 
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "\n")
            racescreens[6].scr_halfling.insert("end", "Languages Known: ")
            racescreens[6].scr_halfling.insert("end", racescreens[0].languages_known)
            RaceScreens.current = 6
            RaceScreens.switch_frame()
    
class ChooseTraits(RaceScreens):
    def __init__(self):
        RaceScreens.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        
        self.chosen = 0
        
        self.lbl_traits = tk.Label(self, text = "Please pick two traits to increase by one:", 
                                       font = DEFAULT, bg = FRMBACKGROUND)
        self.lbl_traits.grid(row = 0, column = 0, columnspan = 3)        
        
        self.btn_str = tk.Button(self, text = "Strength", font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE, command = self.disable_str)
        self.btn_str.grid(row = 1, column = 0) 
        
        self.btn_dex = tk.Button(self, text = "Dexterity", font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE, command = self.disable_dex)
        self.btn_dex.grid(row = 2, column = 0)
        
        self.btn_con = tk.Button(self, text = "Constitution", font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE, command = self.disable_con)
        self.btn_con.grid(row = 3, column = 0)
        
        self.btn_int = tk.Button(self, text = "Intelligence", font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE, command = self.disable_int)
        self.btn_int.grid(row = 4, column = 0) 
        
        self.btn_wis = tk.Button(self, text = "Wisdom", font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE, command = self.disable_wis)
        self.btn_wis.grid(row = 5, column = 0)
        
        self.btn_cha = tk.Button(self, text = "Charisma", font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE, command = self.disable_cha)
        self.btn_cha.grid(row = 6, column = 0)        
        
        self.btn_ok = tk.Button(self, text = "Ok", font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE, command = self.confirmed)
        self.btn_ok.grid(row = 7, column = 0)  
        
    def disable_str(self):
        racescreens[4].strength += 1
        self.btn_str.configure(state = "disabled")
        self.chosen += 1
        if self.chosen >= 2:
            self.btn_dex.configure(state = "disabled")
            self.btn_con.configure(state = "disabled")
            self.btn_int.configure(state = "disabled")
            self.btn_wis.configure(state = "disabled")
            self.btn_cha.configure(state = "disabled")

            
            
    
    def disable_dex(self):
        racescreens[4].dex += 1
        self.btn_dex.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_str.configure(state = "disabled")
            self.btn_con.configure(state = "disabled")
            self.btn_int.configure(state = "disabled")
            self.btn_wis.configure(state = "disabled")
            self.btn_cha.configure(state = "disabled")

               
    
    def disable_con(self):
        racescreens[4].con += 1
        self.btn_con.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_dex.configure(state = "disabled")
            self.btn_str.configure(state = "disabled")
            self.btn_int.configure(state = "disabled")
            self.btn_wis.configure(state = "disabled")
            self.btn_cha.configure(state = "disabled")
    
    def disable_int(self):
        racescreens[4].intelligence += 1
        self.btn_int.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_dex.configure(state = "disabled")
            self.btn_str.configure(state = "disabled")
            self.btn_con.configure(state = "disabled")
            self.btn_wis.configure(state = "disabled")
            self.btn_cha.configure(state = "disabled")
        
    def disable_wis(self):
        racescreens[4].wis += 1
        self.btn_wis.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_dex.configure(state = "disabled")
            self.btn_str.configure(state = "disabled")
            self.btn_int.configure(state = "disabled")
            self.btn_con.configure(state = "disabled")
            self.btn_cha.configure(state = "disabled")
        
    def disable_cha(self):
        racescreens[4].cha += 1
        self.btn_cha.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_dex.configure(state = "disabled")
            self.btn_str.configure(state = "disabled")
            self.btn_int.configure(state = "disabled")
            self.btn_wis.configure(state = "disabled")
            self.btn_con.configure(state = "disabled") 
        
    def confirmed(self):
        self.chosen = 0
        self.btn_str.configure(state = "normal")
        self.btn_dex.configure(state = "normal")
        self.btn_con.configure(state = "normal")
        self.btn_int.configure(state = "normal")
        self.btn_wis.configure(state = "normal")
        self.btn_cha.configure(state = "normal")
        racescreens[6].scr_human.delete(0.0, "end")
        racescreens[6].scr_human.insert("end", "Your Racial Traits:")           
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "\n")            
        racescreens[6].scr_human.insert("end", "Strength Score: ")
        racescreens[6].scr_human.insert("end", racescreens[4].strength)
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "Dexterity Score: ")
        racescreens[6].scr_human.insert("end", racescreens[4].dex)
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "Constitution Score: ")
        racescreens[6].scr_human.insert("end", racescreens[4].con)
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "Intelligence Score: ")
        racescreens[6].scr_human.insert("end", racescreens[4].intelligence) 
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "Wisdom Score: ")
        racescreens[6].scr_human.insert("end", racescreens[4].wis) 
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "Charisma Score: ")
        racescreens[6].scr_human.insert("end", racescreens[4].cha) 
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "Speed: ")
        racescreens[6].scr_human.insert("end", racescreens[0].speed) 
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "\n")
        racescreens[6].scr_human.insert("end", "Languages Known: ")
        racescreens[6].scr_human.insert("end", racescreens[0].languages_known)        
        RaceScreens.current = 6
        RaceScreens.switch_frame()        
    
class Human(RaceScreens):
    def __init__(self):
        RaceScreens.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        
        self.lbl_human = tk.Label(self, text = "Human:", 
                                       font = DEFAULT, bg = FRMBACKGROUND)
        self.lbl_human.grid(row = 0, column = 0, columnspan = 3)  
        
        self.scr_human = ScrolledText(self, height = 8, width = 40, font = DEFAULT, wrap = 'word')
        self.scr_human.grid(row = 1, column = 0, columnspan = 3, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel",
                                            font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE,
                                            command = self.cancel)
        self.btn_cancel.grid(row = 2, column = 1, sticky = "news")
        
        self.btn_ok = tk.Button(self, text = "Ok",
                                            font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                            activebackground = BTNBACKGROUNDACTIVE,
                                            command = self.raise_subtype)
        self.btn_ok.grid(row = 2, column = 0, sticky = "news") 
        
    def cancel(self):
        racescreens[4].strength = 0
        racescreens[4].dex = 0
        racescreens[4].con = 0
        racescreens[4].intelligence = 0
        racescreens[4].wis = 0
        racescreens[4].cha = 0
        racescreens[0].speed = 0
        racescreens[0].languages_known = ""        
        RaceScreens.current = 0
        RaceScreens.switch_frame()
        
    def raise_subtype(self):
        pass 
    
class DragonPick(RaceScreens):
    def __init__(self):
        RaceScreens.__init__(self)
        self.grid_columnconfigure(0, weight=1)

        self.breath_weapon = ""
        self.resistance = ""
    
        self.breath_type = tk.IntVar()
    
        self.lbl_continue = tk.Label(self, text = "Please pick what type of damage you will do with your breath weapon:", bg = FRMBACKGROUND)
        self.lbl_continue.grid(row = 0, column = 0, columnspan = 2)
    
        self.rad_black = tk.Radiobutton(self, text = "Black (Acid)", value = 0, 
                                              variable = self.breath_type)
        self.rad_black.grid(row = 1, column = 0, sticky = "news")
    
        self.rad_blue = tk.Radiobutton(self, text = "Blue (Lightning)", value = 1, 
                                              variable = self.breath_type)
        self.rad_blue.grid(row = 2, column = 0, sticky = "news")
        
        self.rad_brass = tk.Radiobutton(self, text = "Brass (Fire)", value = 2, 
                                              variable = self.breath_type)
        self.rad_brass.grid(row = 3, column = 0, sticky = "news")
        
        self.rad_bronze = tk.Radiobutton(self, text = "Bronze (Lightning)", value = 3, 
                                              variable = self.breath_type)
        self.rad_bronze.grid(row = 4, column = 0, sticky = "news")
        
        self.rad_copper = tk.Radiobutton(self, text = "Copper (Acid)", value = 4, 
                                              variable = self.breath_type)
        self.rad_copper.grid(row = 5, column = 0, sticky = "news")
        
        self.rad_gold = tk.Radiobutton(self, text = "Gold (Fire)", value = 5, 
                                              variable = self.breath_type)
        self.rad_gold.grid(row = 6, column = 0, sticky = "news")
        
        self.rad_green = tk.Radiobutton(self, text = "Green (Poison)", value = 6, 
                                              variable = self.breath_type)
        self.rad_green.grid(row = 7, column = 0, sticky = "news")
        
        self.rad_red = tk.Radiobutton(self, text = "Red (Fire)", value = 7, 
                                              variable = self.breath_type)
        self.rad_red.grid(row = 8, column = 0, sticky = "news")
        
        self.rad_silver = tk.Radiobutton(self, text = "Silver (Cold)", value = 8, 
                                              variable = self.breath_type)
        self.rad_silver.grid(row = 9, column = 0, sticky = "news")
        
        self.rad_white = tk.Radiobutton(self, text = "White (Cold)", value = 9, 
                                              variable = self.breath_type)
        self.rad_white.grid(row = 10, column = 0, sticky = "news")        
    
        self.btn_cancel = tk.Button(self, text = "Cancel",
                                        font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                                activebackground = BTNBACKGROUNDACTIVE,
                                                command = self.cancel)
        self.btn_cancel.grid(row = 11, column = 1, sticky = "news")
    
        self.btn_ok = tk.Button(self, text = "Ok",
                                    font = DEFAULT, bg = BTNBACKGROUNDSTATIC,
                                                activebackground = BTNBACKGROUNDACTIVE,
                                                command = self.confirmed)
        self.btn_ok.grid(row = 12, column = 0, sticky = "news")    
        
    def cancel(self):
        self.strength = 0
        self.dex = 0
        self.con = 0
        self.intelligence = 0
        self.wis = 0
        self.cha = 0
        racescreens[0].speed = 0
        racescreens[0].languages_known = ""
        RaceScreens.current = 0
        RaceScreens.switch_frame()
        
    def confirmed(self):
        if self.breath_type.get() == 0:
            self.breath_weapon = "Black (Acid)"
            self.resistance = "Acid"
            
        elif self.breath_type.get() == 1:
            self.breath_weapon = "Blue (Lightning)"
            self.resistance = "Lightning"
            
        
  

if __name__ == "__main__":
    root = tk.Tk()
    root.title("The DND Character Creator")    
    
    mainscreens = [MainMenu(), RaceMenu(), ClassMenu()]
    
    mainscreens[0].grid(row = 0, column = 0, sticky = "news")
    mainscreens[1].grid(row = 0, column = 0, sticky = "news")
    mainscreens[2].grid(row = 0, column = 0, sticky = "news")
    
    racescreens = [Start(), Dwarf(), Elf(), Halfling(), HumanPick(), ChooseTraits(), Human(), DragonPick()]
    
    racescreens[0].grid(row = 0, column = 0, sticky = "news")
    racescreens[1].grid(row = 0, column = 0, sticky = "news")
    racescreens[2].grid(row = 0, column = 0, sticky = "news")
    racescreens[3].grid(row = 0, column = 0, sticky = "news")
    racescreens[4].grid(row = 0, column = 0, sticky = "news")
    racescreens[5].grid(row = 0, column = 0, sticky = "news")
    racescreens[6].grid(row = 0, column = 0, sticky = "news")
    racescreens[7].grid(row = 0, column = 0, sticky = "news")

    
    mainscreens[0].tkraise()
    root.grid_columnconfigure(0, weight = 1)
    root.mainloop()    