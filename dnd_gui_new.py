#!/usr/bin/python3
#LaneDoyle
#12/3/19

import tkinter as tk
import dieroller as dr
from tkinter.scrolledtext import ScrolledText

#Global Variables
#Armor class and hit points
AC = 0
HP = 0
HIT_DIE = ''
#Attributes
STR = 0
DEX = 0
CON = 0
INT = 0
WIS = 0
CHA = 0
#Proficiency bonus
PROF_BONUS = 0
#Saving Throw bonuses
SAVE_STR = 0
SAVE_DEX = 0
SAVE_CON = 0
SAVE_INT = 0
SAVE_WIS = 0
SAVE_CHA = 0
#Skill bonuses
ACROBATICS = 0
ANIMAL_HANDLING = 0
ARCANA = 0
ATHLETICS = 0
DECEPTION = 0
HISTORY = 0
INSIGHT = 0
INTIMIDATION = 0
INVESTIGATION = 0
MEDICINE = 0
NATURE = 0
PERCEPTION = 0
PERFORMANCE = 0
PERSUASION = 0
RELIGION = 0
SLEIGHT_OF_HAND = 0
STEALTH = 0
SURVIVAL = 0
#Equipment
WEAPON1 = ''
WEAPON2 = ''
ARMOR = ''
SPELL_SLOTS = ''
SPELLS = ''
#Misc
BACKGROUND = ''
ALIGNMENT = ''
SPEED = 0
LANGUAGES_KNOWN = ''
SUBCLASS = ''
PROFICIENCY = ''
ADVANTAGES = ''
RESISTANCE = ''
OTHER = ''

#Styles Constants
DEFAULT = ('Arial', 25)
FRMBACKGROUND = "mint cream"
BTNBACKGROUNDSTATIC = "ivory"
BTNBACKGROUNDACTIVE = "MistyRose2"

#Lists
available_races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", 
                  "Gnome", "Half-Elf", "Orc", "Tiefling"]

available_classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", 
                     "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", 
                     "Warlock", "Wizard"]
race_traits = []

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
        global CON 
        global SPEED
        global ADVANTAGES
        global PROFICIENCY
        global LANGUAGES_KNOWN
        global DEX
        global STR
        global CHA
        global INT
        if self.race_chosen.get() == 0:
            SPEED += 25
            CON += 2
            ADVANTAGES += 'poison, '
            PROFICIENCY += 'battleaxe, handaxe, throwing hammer, warhammer, '
            PROFICIENCY += "smith's tools, brewer's supplies, OR mason's tools, "
            PROFICIENCY += "History of stonework checks, "
            LANGUAGES_KNOWN = 'Dwarven, Common, '
            
            RaceScreens.current = 1
            RaceScreens.switch_frame()
           
            racescreens[1].scr_dwarf.delete(0.0, "end")
            racescreens[1].scr_dwarf.insert("end", "Your Racial Traits:")           
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "\n")            
            racescreens[1].scr_dwarf.insert("end", "Speed: ")
            racescreens[1].scr_dwarf.insert("end", SPEED)
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "Constitution Score: ")
            racescreens[1].scr_dwarf.insert("end", CON)
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "Advantages: ")
            racescreens[1].scr_dwarf.insert("end", ADVANTAGES)
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "Proficiency: ")
            racescreens[1].scr_dwarf.insert("end", PROFICIENCY)
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "\n")
            racescreens[1].scr_dwarf.insert("end", "Languages Known: ")
            racescreens[1].scr_dwarf.insert("end", LANGUAGES_KNOWN)
            
        elif self.race_chosen.get() == 1:
            DEX += 2
            SPEED += 30
            PROFICIENCY += 'The perception skill'
            ADVANTAGES += 'Charmed, '
            LANGUAGES_KNOWN += 'Elvish, Common, '
            
            RaceScreens.current = 2
            RaceScreens.switch_frame()
            
            racescreens[2].scr_elf.delete(0.0, "end")
            racescreens[2].scr_elf.insert("end", "Your Racial Traits:")           
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "\n")            
            racescreens[2].scr_elf.insert("end", "Dexterity Score: ")
            racescreens[2].scr_elf.insert("end", DEX)
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "Speed: ")
            racescreens[2].scr_elf.insert("end", SPEED)
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "Advantages: ")
            racescreens[2].scr_elf.insert("end", ADVANTAGES)
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "Proficiency: ")
            racescreens[2].scr_elf.insert("end", PROFICIENCY)
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "\n")
            racescreens[2].scr_elf.insert("end", "Languages Known: ")
            racescreens[2].scr_elf.insert("end", LANGUAGES_KNOWN)
            
        elif self.race_chosen.get() == 2:
            DEX += 1
            SPEED += 25
            ADVANTAGES += 'Fear, '
            LANGUAGES_KNOWN += 'Halfling, Common, ' 
            
            RaceScreens.current = 3
            RaceScreens.switch_frame()
            
            racescreens[3].scr_halfling.delete(0.0, "end")
            racescreens[3].scr_halfling.insert("end", "Your Racial Traits:")           
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "\n")            
            racescreens[3].scr_halfling.insert("end", "Dexterity Score: ")
            racescreens[3].scr_halfling.insert("end", DEX)
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "Speed: ")
            racescreens[3].scr_halfling.insert("end", SPEED)
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "Advantages: ")
            racescreens[3].scr_halfling.insert("end", ADVANTAGES)
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "\n")
            racescreens[3].scr_halfling.insert("end", "Languages Known: ")
            racescreens[3].scr_halfling.insert("end", LANGUAGES_KNOWN)        


            
            

            
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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("The DND Character Creator")    
    
    mainscreens = [MainMenu(), RaceMenu(), ClassMenu()]
    
    mainscreens[0].grid(row = 0, column = 0, sticky = "news")
    mainscreens[1].grid(row = 0, column = 0, sticky = "news")
    mainscreens[2].grid(row = 0, column = 0, sticky = "news")
    
    racescreens = [Start(), Dwarf(), Elf(), Halfling()]
    
    racescreens[0].grid(row = 0, column = 0, sticky = "news")
    racescreens[1].grid(row = 0, column = 0, sticky = "news")
    racescreens[2].grid(row = 0, column = 0, sticky = "news")
    racescreens[3].grid(row = 0, column = 0, sticky = "news")

    
    mainscreens[0].tkraise()
    root.grid_columnconfigure(0, weight = 1)
    root.mainloop()    