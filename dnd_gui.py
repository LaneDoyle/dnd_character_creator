#!/usr/bin/python3
#LaneDoyle
#12/3/19

import tkinter as tk
import sys as sys

#Global Variables
#Font type and size
DEFAULT = ('Arial', 25)
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
LANGUAGES = ''
SUBCLASS = ''
PROFICIENCY = ''




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
        
        self.btn_back_button = tk.Button(self, text = "Continue",
                                            font = DEFAULT, command = self.raise_traits, 
                                            bg = 'ivory', 
                                            activebackground = 'MistyRose2')
        self.btn_back_button.grid(row = 4, column = 0, columnspan = 2)        
        
        self.btn_back_button = tk.Button(self, text = "Back",
                                            font = DEFAULT, command = self.raise_menu, 
                                            bg = 'ivory', 
                                            activebackground = 'MistyRose2')
        self.btn_back_button.grid(row = 5, column = 0, columnspan = 2)        
        
        self.btn_exit_button = tk.Button(self, text = "Exit",
                                            font = DEFAULT, command = self.cancel, 
                                            bg = 'ivory', 
                                            activebackground = 'MistyRose2')
        self.btn_exit_button.grid(row = 6, column = 0, columnspan = 2) 
        
    def cancel(self):
        sys.exit()    
        
    def raise_races(self):
        race_info.tkraise()
        
    def raise_menu(self):
        frame_menu.tkraise()
        
    def raise_traits(self):
        race_traits_dwarf.tkraise()        
    
class Race_Info(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
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
                                       font = ('Arial', 15),
                                       bg = 'mint cream')  
        self.lbl_race_dwarf.grid(row = 2, column = 0)
        
        self.lbl_race_dwarf = tk.Label(self, text = '''Elf: Elves are graceful creatures. 
        They live for centuries and hold 
        vast knowledge of the world around them. 
        Elves can live to be 750 years old. 
        They are, on average, 5 or over 6 ft
        tall. Their weight is similar to a human's. 
        As an elf your dexterity (agility) increases by 2.''', 
                                       font = ('Arial', 15),
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
                                       font = ('Arial', 15),
                                       bg = 'mint cream')  
        self.lbl_race_halfling.grid(row = 4, column = 0) 
        
        self.lbl_race_human= tk.Label(self, text = '''Human: The most recognizable race, humans are adaptable 
        and ambitious. Because of their shorter
        life spans, they do not hesitate to seize the moment. 
        Humans live less than a century. Their height
        and weight vary greatly, from being 5 to over 6 ft tall 
        and 100 to 200 pounds or more. As a human,
        each of your ability scores increase by one.''', 
                                       font = ('Arial', 15),
                                       bg = 'mint cream')  
        self.lbl_race_human.grid(row = 5, column = 0)
        
        self.btn_continue= tk.Button(self, text = "Continue",
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
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Race Information Cont.", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0) 
        #dg = Dragonborn
        self.lbl_race_dg = tk.Label(self, text = '''Dragonborn: The kin of dragons, dragonborn 
        resemble a dragon-like humanoid, 
        although they have no tail
        or wings. Their scale color can range 
        from blue to gold. Their clans are the most 
        important thing in their
        lives. Dragonborn usually live to around 80 years old. 
        On average they are well over 6 ft tall and are around
        250 pounds. As a dragonborn, your strength score increases 
        by 2 and your charisma (confidence, charm, etc.) 
        score increases by 1. ''', 
                                       font = ('Arial', 15),
                                       bg = 'mint cream')  
        self.lbl_race_dg.grid(row = 2, column = 0)
        
        self.lbl_race_gnome = tk.Label(self, text = '''Gnome: About the size of a halfling, 
        the gnome has a delightful energy about them, 
        greatly enjoying the life
        they lead. A gnome's appearance generally tells all you need 
        to know about their personality. They are curious
        people, and enjoy each and every moment. Gnomes can 
        live to almost 500 years old and are, on average, 3 to 4 ft 
        tall and 40 pounds. As a gnome, your intelligence score 
        increases by 2.  ''', 
                                       font = ('Arial', 15),
                                       bg = 'mint cream')  
        self.lbl_race_gnome.grid(row = 3, column = 0) 
        #he = Half Elf
        self.lbl_race_he= tk.Label(self, text = '''Half-Elf: A mix of human and elf, 
        half-elves are usually curious adventurers 
        are quick talking diplomats. They 
        appear to be human, except their ears 
        are pointy and they have the eyes of their elven parents. They live to 
        be around 180 years old and average a height of 5 to 6 
        ft tall. They have about the same weight as a human. As
        a half-elf, your charisma (confidence, charm, etc.) 
        score increases by two and two other ability scores of your 
        choice increase by 1. ''', 
                                       font = ('Arial', 15),
                                       bg = 'mint cream')  
        self.lbl_race_he.grid(row = 4, column = 0)
 
        self.btn_continue= tk.Button(self, text = "Continue",
                                        font = DEFAULT, 
                                        command = self.raise_races_3, 
                                        bg = 'ivory', 
                                        activebackground = 'MistyRose2')  
        self.btn_continue.grid(row = 6, column = 0)        
        
    def raise_races_3(self):
        race_info3.tkraise()
        
class Race_Info3(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Race Information Cont.", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0) 
        #ho = Half Orc
        self.lbl_race_ho= tk.Label(self, text = '''Half-Orc: A mix of human and orc, 
        half-orcs are more than intimidating. 
        Their large figures, jutting jaws, and sharp 
        teeth, can be seen are terrifying by others. 
        Most have scars they collected from battle, while some have scars which
        mark them as an exile. Regardless of the meaning, most half-orcs 
        are marked by at least one scar. However, they rarely
        live longer than 75 years old. They average around 5 
        to well over 6 ft tall and can be around 200 pounds or more. As 
        a half-orc, your strength score increases by 2, and 
        your constitution (vitality) score increases by 1. ''', 
                                       font = ('Arial', 15),
                                       bg = 'mint cream')  
        self.lbl_race_ho.grid(row = 2, column = 0)
        
        self.lbl_race_tiefling= tk.Label(self, text = '''Tiefling: Although appearing similar to 
        humans, tieflings have large horns which 
        take a variety of shapes. Their skin
        color is the same as a human's except some have various 
        shades of red as their skin color. They also have thick tails
        which are around 4 or 5 ft long and solid-colored eyes. 
        They believe trust is earned, not given freely. They live about
        the same length as a human, plus a few years. 
        They have the same average height and weight of a human. As a tiefling,
        your intelligence score increases by 1 and your 
        charisma (confidence, charm, etc.) increases by 2.''', 
                                       font = ('Arial', 15),
                                       bg = 'mint cream')  
        self.lbl_race_tiefling.grid(row = 3, column = 0)  
        
        
        self.btn_cont_button = tk.Button(self, text = "Back",
                                            font = DEFAULT, command = self.raise_start, 
                                            bg = 'ivory', 
                                            activebackground = 'MistyRose2')
        self.btn_cont_button.grid(row = 4, column = 0, columnspan = 2)        
               
        
    def raise_start(self):
        start.tkraise()
        
#Each race will have its own frame and will use an if statement to decide what frame to use in the Start frame
class Race_Traits_Dwarf(tk.Frame):
    def __init__(self):       
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_dwarf_lbl = tk.Label(self, text = "Your Racial Traits (Dwarf):", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_dwarf_lbl.grid(row = 1, column = 0)
        self.lbl_warning_lbl = tk.Label(self, text = ''' Make sure to write all the information 
        you are given on either a piece of paper or a character sheet.''', 
                                              font = ('Arial', 20), fg = 'red',
                                              bg = 'mint cream')
        self.lbl_warning_lbl.grid(row = 2, column = 0)        
        
        self.lbl_traits_dwarf = tk.Label(self, text = ''' o Your Constitution increase by 2.
            o Your speed is 25 ft per turn.
            o You can see in dim light within 60 ft of you as if it were bright light and in darkness
            as if it were dim light.
            o You have advantage on saving throws against poison and resistance to poison damage.
            o You have proficiency with the battleaxe, handaxe, throwing hammer, and warhammer.
            o You have proficiency with one set of tools of your choice: smith's tools, brewer's supplies, or
            mason's tools. 
            o Whenever you make a history check related to the origin of stonework, you can add your proficiency
            bonus to the check and double it.
            o You can speak, read, and write Dwarvish. ''', font = ('Arial', 18), bg = 'mint cream')
        self.lbl_traits_dwarf.grid(row = 3, column = 0)
        
        self.lbl_sub_lbl = tk.Label(self, text = ''' Some classes have subclasses,
        which give additional traits. There are two subclasses of dwarf, the Hill
        Dwarf and the Mountain Dwarf. Hill dwarves increase your health and wisdom.
        Mountain dwarves increases strength and adds proficiencies. Proficiencies
        allow you to use more equipment, like martial weapons.''', 
                                              font = ('Arial', 20), fg = 'blue',
                                              bg = 'mint cream')
        self.lbl_sub_lbl.grid(row = 4, column = 0)
        
        self.btn_hill_btn = tk.Button(self, text = "Hill Dwarf", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_hill)
        self.btn_hill_btn.grid(row = 5, column = 0)
        
        self.btn_mtn_btn = tk.Button(self, text = "Mountain Dwarf", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_mtn)
        self.btn_mtn_btn.grid(row = 6, column = 0)
        
    def raise_hill(self): 
        global WIS
        global HP
        global SUBCLASS         
        hill_dwarf.tkraise()
        WIS += 1
        print(WIS)
        HP += 1
        print(HP)
        SUBCLASS = 'Hill Dwarf'
        print(SUBCLASS)        
            
    def raise_mtn(self):
        global SUBCLASS 
        global STR
        global PROFICIENCY         
        mtn_dwarf.tkraise()
        STR += 2
        print(STR)
        PROFICIENCY += 'Medium armor, '
        PROFICIENCY += 'Light armor, '
        print(PROFICIENCY)
        SUBCLASS = 'Mountain Dwarf'
        print(SUBCLASS)        
        



class Race_Dwarf_Hill(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Hill Dwarf", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_hill = tk.Label(self, text = '''Hill dwarves have keen senses, incredible intuition and unbeatable
            resilience. As a hill dwarf, your wisdom score increases by 1 and your maximum health 
            increases by 1, and it continues to increase by 1 everytime you level up.''', font = ('Arial', 18), bg = 'mint cream')
        self.lbl_traits_hill.grid(row = 2, column = 0)
        
class Race_Dwarf_Mtn(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Mountain Dwarf", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)
        
        self.lbl_traits_mtn = tk.Label(self, text = '''Mountain dwarves are hardy creatures used to rough terrain. They
            are a little taller than a hill dwarf and have a lighter skin color. As a mountain dwarf, your
            strength score increases by 2 and you have proficiency using medium and light armor.''', font = ('Arial', 18), bg = 'mint cream')
        self.lbl_traits_mtn.grid(row = 2, column = 0) 
        
        


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

race_info3 = Race_Info3()
race_info3.grid(row = 0, column = 0, sticky = "news")

race_traits_dwarf = Race_Traits_Dwarf()
race_traits_dwarf.grid(row = 0, column = 0, sticky = "news")

hill_dwarf = Race_Dwarf_Hill()
hill_dwarf.grid(row = 0, column = 0, sticky = "news")

mtn_dwarf = Race_Dwarf_Mtn()
mtn_dwarf.grid(row = 0, column = 0, sticky = "news")

frame_menu.tkraise()
root.mainloop()