#!/usr/bin/python3
#LaneDoyle
#12/3/19

import tkinter as tk
import sys as sys
import dieroller as dr

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
LANGUAGES_KNOWN = ''
SUBCLASS = ''
PROFICIENCY = ''
ADVANTAGES = ''
RESISTANCE = ''
OTHER = ''




#Creating Main Menu
class MainMenu(tk.Frame):
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
        
class RaceMenu(tk.Frame):
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
        
class class_Menu(tk.Frame):
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
        
        self.lbl_race_pick = tk.Label(self, text = "Please enter your race in lowercase:",
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
        global CON 
        global SPEED
        global ADVANTAGES
        global PROFICIENCY
        global LANGUAGES_KNOWN
        global DEX
        global STR
        global CHA
        global INT
        
        if self.ent_race_pick.get() == "dwarf":
            SPEED += 25
            CON += 2
            ADVANTAGES += 'poison, '
            PROFICIENCY += 'battleaxe, handaxe, throwing hammer, warhammer, '
            PROFICIENCY += "smith's tools, brewer's supplies, OR mason's tools, "
            PROFICIENCY += "History of stonework checks, "
            LANGUAGES_KNOWN = 'Dwarven, Common, '
            print(SPEED, CON, ADVANTAGES, PROFICIENCY, LANGUAGES_KNOWN)
            race_traits_dwarf.tkraise()
        elif self.ent_race_pick.get() =="elf":
            DEX += 2
            SPEED += 30
            PROFICIENCY += 'The perception skill'
            ADVANTAGES += 'Charmed, '
            LANGUAGES_KNOWN += 'Elvish, Common, '
            print(DEX, SPEED, PROFICIENCY, ADVANTAGES, LANGUAGES_KNOWN) 
            race_traits_elf.tkraise()
        elif self.ent_race_pick.get() == "halfling":
            DEX += 1
            SPEED += 25
            ADVANTAGES += 'Fear, '
            LANGUAGES_KNOWN += 'Halfling, Common, ' 
            race_traits_halfling.tkraise()
        elif self.ent_race_pick.get() == "human":
            race_traits_human.tkraise()
        elif self.ent_race_pick.get() == "dragonborn":
            STR += 2
            CHA += 1
            SPEED += 30
            LANGUAGES_KNOWN += 'Common, Draconic, '
            race_traits_dragonborn.tkraise()
        elif self.ent_race_pick.get() == "gnome":
            INT += 2
            SPEED += 25
            ADVANTAGES += 'Intelligence, wisdom, and charisma saving throws against magic, '
            LANGUAGES_KNOWN += 'Common, Gnomish, '
            race_traits_gnome.tkraise()
        elif self.ent_race_pick.get() == "half-elf" or self.ent_race_pick.get() == "half elf":
            CHA += 2
            SPEED += 30
            ADVANTAGES += "Saving throws against being charmed, "
            PROFICIENCY += 'Two skills of your choice, '
            LANGUAGES_KNOWN += 'Common, Elvish, '
            race_traits_he.tkraise()
        elif self.ent_race_pick.get() == "half-orc" or self.ent_race_pick.get() == "half orc":
            race_traits_orc.tkraise()
        elif self.ent_race_pick.get() == "tiefling" or self.ent_race_pick.get() == "tief":
            race_traits_tief.tkraise()        
        else: 
            pass
    
class race_Info(tk.Frame):
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
            
        
class race_Info2(tk.Frame):
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
        
class race_Info3(tk.Frame):
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
#Dwarf
class race_Traits_Dwarf(tk.Frame):
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
        allow you to use more equipment or skills, like martial weapons or perception.
        Choose wisely as you can not go back...''', 
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
        



class race_Dwarf_Hill(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Hill Dwarf", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_hill = tk.Label(self, text = '''Hill dwarves have keen senses, incredible intuition and unbeatable
            resilience. As a hill dwarf, your wisdom score increases by 1 and your maximum health 
            increases by 1, and it continues to increase by 1 everytime you level up.''', font = DEFAULT, bg = 'mint cream')
        self.lbl_traits_hill.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_cont_btn.grid(row = 3, column = 0)
        
class race_Dwarf_Mtn(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Mountain Dwarf", font = DEFAULT, 
                                     bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)
        
        self.lbl_traits_mtn = tk.Label(self, text = '''Mountain dwarves are hardy creatures used to rough terrain. They
            are a little taller than a hill dwarf and have a lighter skin color. As a mountain dwarf, your
            strength score increases by 2 and you have proficiency using medium and light armor.''', font = DEFAULT, bg = 'mint cream')
        self.lbl_traits_mtn.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_cont_btn.grid(row = 3, column = 0)        
        
        




#Elf
class race_Traits_Elf(tk.Frame):
    def __init__(self):       
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_elf_lbl = tk.Label(self, text = "Your Racial Traits (Elf):", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_elf_lbl.grid(row = 1, column = 0)
        
        self.lbl_warning_lbl = tk.Label(self, text = ''' Make sure to write all the information 
        you are given on either a piece of paper or a character sheet.''', 
                                              font = ('Arial', 20), fg = 'red',
                                              bg = 'mint cream')
        self.lbl_warning_lbl.grid(row = 2, column = 0) 
        
        self.lbl_traits_elf = tk.Label(self, text = '''o Your dexterity score increases by 2.
            o Your walking speed is 30 ft per turn.
            o You can see in dim light within 60 ft of you as if it were bright light and in darkness
            as if it were dim light.
            o You have proficiency in the perception skill.
            o You have advantage on saving throws against being charmed, and magic can't put you to
            sleep.
            o Elves do not require sleep, instead they meditate deeply for 4 hours a day.
            o You can speak, read, and write Elvish.''', font = ('Arial', 18), bg = 'mint cream')
        self.lbl_traits_elf.grid(row = 3, column = 0)
        
        self.lbl_sub_lbl = tk.Label(self, text = ''' Some classes have subclasses,
        which give additional traits. There are three wubclasses of elves, high elves,
        wood elves, and drow. Being a high elf increases your intelligence, gives
        you proficiencies, one extra spell, and one extra language to know. Wood elves
        give you an increase to your wisdom, proficiencies, makes you faster, and
        gives you advantages to using stealth. Being a drow gives you an increase to
        your charisma, darkvision extended to 120ft, one extra spell, and proficiencies.
        However, being a drow makes it harder for you to attack in sunlight, as they are from
        underground. Proficiencies allow you to use more equipment or skills, like martial 
        weapons or perception. Choose wisely as you can not go back...''', 
                                              font = ('Arial', 20), fg = 'blue',
                                              bg = 'mint cream')
        self.lbl_sub_lbl.grid(row = 4, column = 0)
        
        self.btn_high_btn = tk.Button(self, text = "High Elf", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_high)
        self.btn_high_btn.grid(row = 5, column = 0)
        
        self.btn_wood_btn = tk.Button(self, text = "Wood Elf", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_wood)
        self.btn_wood_btn.grid(row = 6, column = 0)  
        
        self.btn_drow_btn = tk.Button(self, text = "Dark Elf (Drow)", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_drow)
        self.btn_drow_btn.grid(row = 7, column = 0)
        
    def raise_high(self):
        global INT
        global PROFICIENCY
        global LANGUAGES_KNOWN
        global SPELLS
        high_elf.tkraise()
        INT += 1
        print(INT)
        PROFICIENCY += 'Longsword, '
        PROFICIENCY += 'Shortbow, '
        PROFICIENCY += 'Longbow, '
        print(PROFICIENCY)
        LANGUAGES_KNOWN += 1
        print(LANGUAGES_KNOWN)
        SPELLS += 'One wizard cantrip of your choice, '
        print(SPELLS)
        
        
    def raise_wood(self):
        global PROFICIENCY
        global WIS
        global SPEED
        wood_elf.tkraise()
        PROFICIENCY += 'Longsword, '
        PROFICIENCY += 'Shortsword, '
        PROFICIENCY += 'Shortbow, '
        PROFICIENCY += 'Longbow, '
        print(PROFICIENCY)
        WIS += 1
        print(WIS)
        SPEED = 35
        print(SPEED)
        
    def raise_drow(self):
        global CHA
        global SPELLS
        global PROFICIENCY
        drow_elf.tkraise()
        CHA += 1
        print(CHA)
        SPELLS += 'Dancing Lights, '
        print(SPELLS)
        PROFICIENCY += 'Rapier, '
        PROFICIENCY += 'Shortsword, '
        PROFICIENCY += 'Hand Crossbow, '
        print(PROFICIENCY)        
        
        
        

class race_Elf_High(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "High Elf", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_high = tk.Label(self, text = '''A master of magic, the high elf is a very intelligent being. As a 
            high elf your intelligence increases by 1 and you are proficient with the longsword,
            shortbow, and longbow. You also know one cantrip of your choice from the wizard spell
            list, using intelligence as your spellcasting ability. You can also speak, read, and write
            one extra language.''', font = DEFAULT, bg = 'mint cream')
        self.lbl_traits_high.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_cont_btn.grid(row = 3, column = 0)    

class race_Elf_Wood(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Wood Elf", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_wood = tk.Label(self, text = '''The wood elf is a stealthy and quick individual. They have copperish skin with 
            copper colored hair and green/brown/hazel eyes.As a wood elf your wisdom increases by 1 and you are 
            proficient with the longsword, shortsword, shortbow, and longbow. Your base walking speed increases 
            to 35 ft anf you can attempt to hide even when you are only lightly obscured by foliage, heavy rain, 
            falling snow, mist, etc.''', font = DEFAULT, bg = 'mint cream')
        self.lbl_traits_wood.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_cont_btn.grid(row = 3, column = 0)    
    
class race_Elf_Drow(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Dark Elf (Drow)", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_drow = tk.Label(self, text = '''Banished from the surface, the drow now call the Underdark their home.
            They usually have very dark skin and pale eyes with white or yellow hair. Your charisma score 
            increases by one and your darkvision extends to 120 ft. Drow, being from underground, have
            disadvantage on attack rolls and on wisdom checks that rely on sight when you, your target,
            or whatever you are trying to see is in sunlight. You know the dancing lights cantrip, and are
            profiecient with rapiers, shortswords, and hand crossbows.''', font = DEFAULT, bg = 'mint cream')
        self.lbl_traits_drow.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_cont_btn.grid(row = 3, column = 0)    

#Halfiling
class race_Traits_Halfling(tk.Frame):
    def __init__(self):       
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_halfling_lbl = tk.Label(self, text = "Your Racial Traits (Halfling):", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_halfling_lbl.grid(row = 1, column = 0)
        
        self.lbl_warning_lbl = tk.Label(self, text = ''' Make sure to write all the information 
        you are given on either a piece of paper or a character sheet.''', 
                                              font = ('Arial', 20), fg = 'red',
                                              bg = 'mint cream')
        self.lbl_warning_lbl.grid(row = 2, column = 0) 
        
        self.lbl_traits_halfling = tk.Label(self, text = ''' o Your dexterity score increases by 2.
        o Your base walking speed is 25 ft per turn.
        o When you roll a 1 on an attack roll, skill check, or saving throw, you can reroll the die and
        must use the new roll.
        o You have advantage on saving throws against being frightened.
        o You can move through the space of any creature that is of a size larger than yours.
        o You can speak, read, and write Common and Halfling''', font = ('Arial', 18), bg = 'mint cream')
        self.lbl_traits_halfling.grid(row = 3, column = 0)
        
        self.lbl_sub_lbl = tk.Label(self, text = ''' Some classes have subclasses,
        which give additional traits. There are two subclasses of halfling, lightfoot 
        halflings and stout halflings. As a lightfoot halfling, your charisma score increases and 
        hiding is easier for you.  As a stout halfling your constitution score increases and it
        is harder for you to be poisoned. Choose wisely as you can not go back...''', 
                                              font = ('Arial', 20), fg = 'blue',
                                              bg = 'mint cream')
        self.lbl_sub_lbl.grid(row = 4, column = 0)
        
        self.btn_light_btn = tk.Button(self, text = "Lightfoot Halfling", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_light)
        self.btn_light_btn.grid(row = 5, column = 0)
        
        self.btn_stout_btn = tk.Button(self, text = "Stout Halfing", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_stout)
        self.btn_stout_btn.grid(row = 6, column = 0)
        
  
    def raise_light(self):
        global CHA
        CHA += 1
        print(CHA)
        half_light.tkraise()
        
        
    def raise_stout(self):
        global CON
        global RESISTANCE 
        global ADVANTAGES 
        CON += 1
        RESISTANCE += 'Poison, '
        ADVANTAGES += 'Poison, '
        print(CON, RESISTANCE, ADVANTAGES)
        half_stout.tkraise()

class race_Halfling_Light(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Lightfoot Halfling", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_light = tk.Label(self, text = '''Silent creatures, lightfoot halflings can easily hide from sight.
        As a lightfoot halfling your charisma score increases by 1 and you can attempt to hide even when
        you are obscured only by a creature that is at least one size larger than you.''', 
                                              font = DEFAULT, bg = 'mint cream')
        self.lbl_traits_light.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_cont_btn.grid(row = 3, column = 0) 
        
class race_Halfling_Stout(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Stout Halfling", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_stout = tk.Label(self, text = '''Stout Halflings are hardier creatures that are rumored to have dwarven
        blood. As a stout halfling your constitution score increases by 1 and you have advantage on saving
        throws against poison, and you have resistance against poison damage. More
        on resistance and saving throws later.''', 
                                              font = DEFAULT, bg = 'mint cream')
        self.lbl_traits_stout.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2')
        self.btn_cont_btn.grid(row = 3, column = 0)

#Human
class race_Traits_Human(tk.Frame):
    def __init__(self):       
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_human_lbl = tk.Label(self, text = "Your Racial Traits (Human):", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_human_lbl.grid(row = 1, column = 0)
        
        self.lbl_warning_lbl = tk.Label(self, text = ''' Make sure to write all the information 
        you are given on either a piece of paper or a character sheet.''', 
                                              font = ('Arial', 20), fg = 'red',
                                              bg = 'mint cream')
        self.lbl_warning_lbl.grid(row = 2, column = 0) 
        
        self.lbl_traits_human = tk.Label(self, text = '''o Your ability scores each increase by 1.
        o Your base walking speed is 30 ft per turn.
        o You can speak, read, and write Common and one extra language of your choice.''', font = ('Arial', 18), bg = 'mint cream')
        self.lbl_traits_human.grid(row = 3, column = 0)
        
        self.lbl_sub_lbl = tk.Label(self, text = ''' Some classes have subclasses,
        which give additional traits. There is technically two subclasses of human.
        Variant human and regular human. Variant human gives you extra bonuses and skills,
        however, confirm with your DM before choosing this subclass.  Choose wisely as you can 
        not go back...''', 
                                              font = ('Arial', 20), fg = 'blue',
                                              bg = 'mint cream')
        self.lbl_sub_lbl.grid(row = 4, column = 0)
        
        self.btn_var_btn = tk.Button(self, text = "Variant Human", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_variant)
        self.btn_var_btn.grid(row = 5, column = 0)
        
        self.btn_reg_btn = tk.Button(self, text = "Regular Human", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_regular)
        self.btn_reg_btn.grid(row = 6, column = 0)        
        
    def raise_variant(self):
        global SPEED
        global LANGUAGES_KNOWN
        SPEED += 30
        LANGUAGES_KNOWN += 'Common, One of your choice, '
        print(SPEED, LANGUAGES_KNOWN)
        human_variant.tkraise()
        
   
    def raise_regular(self):
        global STR
        global DEX
        global CON
        global INT
        global WIS
        global CHA
        global SPEED
        global LANGUAGES_KNOWN
        STR += 1
        DEX += 1
        CON += 1
        INT += 1
        WIS += 1
        CHA += 1
        SPEED += 30
        LANGUAGES_KNOWN += 'Common, One of your choice, '
        print(STR, DEX, CON, INT, WIS, CHA, SPEED, LANGUAGES_KNOWN)
        human_regular.tkraise()
          
    
class race_Human_Variant(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Variant Human", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_var = tk.Label(self, text = '''As a variant human, you have special
        race features different from a regular human. Instead of having every ability score increase 
        by one, as a  variant, you can choose two abilities to increase by one. You have one skill 
        to have proficiency in one skill. You also have one feat of your choice.''', 
                                              font = DEFAULT, bg = 'mint cream')
        self.lbl_traits_var.grid(row = 2, column = 0)
        
        self.lbl_traits_pick = tk.Label(self, text = '''Please pick two attributes to increase by one. ''', 
                                              font = DEFAULT, bg = 'mint cream', fg = 'red')
        self.lbl_traits_pick.grid(row = 3, column = 0)        
        
        self.btn_str_btn = tk.Button(self, text = "Strength", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = self.disable_str)
        self.btn_str_btn.grid(row = 4, column = 0) 
        
        self.btn_dex_btn = tk.Button(self, text = "Dexterity", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = self.disable_dex)
        self.btn_dex_btn.grid(row = 5, column = 0)
        
        self.btn_con_btn = tk.Button(self, text = "Constitution", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = self.disable_con)
        self.btn_con_btn.grid(row = 6, column = 0)
        
        self.btn_int_btn = tk.Button(self, text = "Intelligence", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = self.disable_int)
        self.btn_int_btn.grid(row = 7, column = 0) 
        
        self.btn_wis_btn = tk.Button(self, text = "Wisdom", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = self.disable_wis)
        self.btn_wis_btn.grid(row = 8, column = 0)
        
        self.btn_cha_btn = tk.Button(self, text = "Charisma", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = self.disable_cha)
        self.btn_cha_btn.grid(row = 9, column = 0)        
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 10, column = 0)  
        
    def disable_str(self):
        global STR
        STR += 1
        print(STR)
        self.btn_str_btn.configure(state = "disabled")
        self.chosen += 1
        if self.chosen >= 2:
            self.btn_dex_btn.configure(state = "disabled")
            self.btn_con_btn.configure(state = "disabled")
            self.btn_int_btn.configure(state = "disabled")
            self.btn_wis_btn.configure(state = "disabled")
            self.btn_cha_btn.configure(state = "disabled")
            
            
    
    def disable_dex(self):
        global DEX
        DEX += 1
        print(DEX)
        self.btn_dex_btn.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_str_btn.configure(state = "disabled")
            self.btn_con_btn.configure(state = "disabled")
            self.btn_int_btn.configure(state = "disabled")
            self.btn_wis_btn.configure(state = "disabled")
            self.btn_cha_btn.configure(state = "disabled")
               
    
    def disable_con(self):
        global CON
        CON += 1
        print(CON)
        self.btn_con_btn.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_dex_btn.configure(state = "disabled")
            self.btn_str_btn.configure(state = "disabled")
            self.btn_int_btn.configure(state = "disabled")
            self.btn_wis_btn.configure(state = "disabled")
            self.btn_cha_btn.configure(state = "disabled")                
    
    def disable_int(self):
        global INT
        INT += 1
        print(INT)
        self.btn_int_btn.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_dex_btn.configure(state = "disabled")
            self.btn_str_btn.configure(state = "disabled")
            self.btn_con_btn.configure(state = "disabled")
            self.btn_wis_btn.configure(state = "disabled")
            self.btn_cha_btn.configure(state = "disabled") 
        
    def disable_wis(self):
        global WIS
        WIS += 1
        print(WIS)
        self.btn_wis_btn.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_dex_btn.configure(state = "disabled")
            self.btn_str_btn.configure(state = "disabled")
            self.btn_int_btn.configure(state = "disabled")
            self.btn_con_btn.configure(state = "disabled")
            self.btn_cha_btn.configure(state = "disabled") 
        
    def disable_cha(self):
        global CHA
        CHA += 1
        print(CON)
        self.btn_cha_btn.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_dex_btn.configure(state = "disabled")
            self.btn_str_btn.configure(state = "disabled")
            self.btn_int_btn.configure(state = "disabled")
            self.btn_wis_btn.configure(state = "disabled")
            self.btn_con_btn.configure(state = "disabled") 
        
    
        
class race_Human_Regular(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Regular Human", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_reg = tk.Label(self, text = '''All your race features were listed on
        the previous frame.
        o Your ability scores each increase by 1.
        o Your base walking speed is 30 ft per turn.
        o You can speak, read, and write Common and one extra language of your choice.''', 
                                              font = DEFAULT, bg = 'mint cream')
        self.lbl_traits_reg.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = '')
        self.btn_cont_btn.grid(row = 3, column = 0)    
    
        



#Dragonborn
class race_Traits_Dragonborn(tk.Frame):
    def __init__(self):       
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_dragon_lbl = tk.Label(self, text = "Your Racial Traits (Dragonborn):", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_dragon_lbl.grid(row = 1, column = 0)
        
        self.lbl_warning_lbl = tk.Label(self, text = ''' Make sure to write all the information 
        you are given on either a piece of paper or a character sheet.''', 
                                              font = ('Arial', 20), fg = 'red',
                                              bg = 'mint cream')
        self.lbl_warning_lbl.grid(row = 2, column = 0) 
        
        self.lbl_traits_dragon = tk.Label(self, text = '''o Your strength score increases by 2.
        o Your charisma score increases by 1.
        o Your base walking speed is 30 ft per turn.
        o You can speak, read, and write Common and Draconic.''', font = ('Arial', 18), bg = 'mint cream')
        self.lbl_traits_dragon.grid(row = 3, column = 0)
        
        self.lbl_sub_lbl = tk.Label(self, text = ''' Some classes have subclasses,
        which give additional traits. The subclasses of Dragonborn determine yoru breath weapon and
        scale color. Each dragonborn has a breath weapon they can choose; fire, cold, etc. Below, 
        please pick a damage type. Choose wisely as you can not go back...''', 
                                              font = ('Arial', 20), fg = 'blue',
                                              bg = 'mint cream')
        self.lbl_sub_lbl.grid(row = 4, column = 0)
        
        self.btn_black_btn = tk.Button(self, text = "Black (Acid)", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_black)
        self.btn_black_btn.grid(row = 5, column = 0)
        
        self.btn_blue_btn = tk.Button(self, text = "Blue (Lightning)", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_blue)
        self.btn_blue_btn.grid(row = 6, column = 0)      
        
        self.btn_brass_btn = tk.Button(self, text = "Brass (Fire)", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_brass)
        self.btn_brass_btn.grid(row = 7, column = 0)
        
        self.btn_bronze_btn = tk.Button(self, text = "Bronze (Lightning)", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_bronze)
        self.btn_bronze_btn.grid(row = 8, column = 0)
        
        self.btn_copper_btn = tk.Button(self, text = "Copper (Acid)", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_copper)
        self.btn_copper_btn.grid(row = 9, column = 0)
        
        self.btn_gold_btn = tk.Button(self, text = "Gold (Fire)", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_gold)
        self.btn_gold_btn.grid(row = 10, column = 0)
        
        self.btn_green_btn = tk.Button(self, text = "Green (Poison)", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_green)
        self.btn_green_btn.grid(row = 11, column = 0)
        
        self.btn_red_btn = tk.Button(self, text = "Red (Fire)", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_red)
        self.btn_red_btn.grid(row = 12, column = 0)
        
        self.btn_silver_btn = tk.Button(self, text = "Silver (Cold)", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_silver)
        self.btn_silver_btn.grid(row = 13, column = 0)
        
        self.btn_white_btn = tk.Button(self, text = "White (Cold)", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_white)
        self.btn_white_btn.grid(row = 14, column = 0)   
        
    def raise_black(self):
        global RESISTANCE
        RESISTANCE += 'Acid, '
        dragon_black.tkraise()
    
    def raise_blue(self):
        global RESISTANCE
        RESISTANCE += 'Lightning, '
        dragon_blue.tkraise()
        
    def raise_brass(self):
        global RESISTANCE
        RESISTANCE += 'Fire, '
        dragon_brass.tkraise()
        
    def raise_bronze(self):
        global RESISTANCE
        RESISTANCE += 'Lightning, '
        dragon_bronze.tkraise()
        
    def raise_copper(self):
        global RESISTANCE
        RESISTANCE += 'Acid, '
        dragon_copper.tkraise()
        
    def raise_gold(self):
        global RESISTANCE
        RESISTANCE += 'Fire, '
        dragon_gold.tkraise()
        
    def raise_green(self):
        global RESISTANCE
        RESISTANCE += 'Poison, '
        dragon_green.tkraise()
        
    def raise_red(self):
        global RESISTANCE
        RESISTANCE += 'Fire, '
        dragon_red.tkraise()
        
    def raise_silver(self):
        global RESISTANCE
        RESISTANCE += 'Cold, '
        dragon_silver.tkraise()
        
    def raise_white(self):
        global RESISTANCE
        RESISTANCE += 'Cold, ' 
        dragon_white.tkraise()

    
    
    
class race_Dragonborn_Black(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Black(Acid) Dragonborn", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_black = tk.Label(self, text = '''You can now breathe acid! You are
        also resistant to any acid damage. (Resistance will be explained later)''', 
                                              font = ('Arial', 30), bg = 'mint cream')
        self.lbl_traits_black.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 3, column = 0) 
        
class race_Dragonborn_Blue(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Blue(Lightning) Dragonborn", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_blue = tk.Label(self, text = '''You can now breathe lightning! You are
        also resistant to any lightning damage. (Resistance will be explained later)''', 
                                              font = ('Arial', 30), bg = 'mint cream')
        self.lbl_traits_blue.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 3, column = 0)
        
class race_Dragonborn_Brass(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Brass(Fire) Dragonborn", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_brass = tk.Label(self, text = '''You can now breathe fire! You are
        also resistant to any fire damage. (Resistance will be explained later)''', 
                                              font = ('Arial', 30), bg = 'mint cream')
        self.lbl_traits_brass.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 3, column = 0)
        
class race_Dragonborn_Bronze(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Bronze(Lightning) Dragonborn", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_bronze = tk.Label(self, text = '''You can now breathe lightning! You are
        also resistant to any lightning damage. (Resistance will be explained later)''', 
                                              font = ('Arial', 30), bg = 'mint cream')
        self.lbl_traits_bronze.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 3, column = 0)
        
class race_Dragonborn_Copper(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Copper(Acid) Dragonborn", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_copper = tk.Label(self, text = '''You can now breathe acid! You are
        also resistant to any acid damage. (Resistance will be explained later)''', 
                                              font = ('Arial', 30), bg = 'mint cream')
        self.lbl_traits_copper.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 3, column = 0)
        
class race_Dragonborn_Gold(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Gold(Fire) Dragonborn", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_gold = tk.Label(self, text = '''You can now breathe fire! You are
        also resistant to any fire damage. (Resistance will be explained later)''', 
                                              font = ('Arial', 30), bg = 'mint cream')
        self.lbl_traits_gold.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 3, column = 0)
        
class race_Dragonborn_Green(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Green(Poison) Dragonborn", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_green = tk.Label(self, text = '''You can now breathe poison! You are
        also resistant to any poison damage. (Resistance will be explained later)''', 
                                              font = ('Arial', 30), bg = 'mint cream')
        self.lbl_traits_green.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 3, column = 0)
        
class race_Dragonborn_Red(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Red(Fire) Dragonborn", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_red = tk.Label(self, text = '''You can now breathe fire! You are
        also resistant to any fire damage. (Resistance will be explained later)''', 
                                              font = ('Arial', 30), bg = 'mint cream')
        self.lbl_traits_red.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 3, column = 0)
        
class race_Dragonborn_Silver(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Silver(Cold) Dragonborn", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_silver = tk.Label(self, text = '''You can now breathe cold! You are
        also resistant to any cold damage. (Resistance will be explained later)''', 
                                              font = ('Arial', 30), bg = 'mint cream')
        self.lbl_traits_silver.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 3, column = 0)
        
class race_Dragonborn_White(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "White(Cold) Dragonborn", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_white = tk.Label(self, text = '''You can now breathe cold! You are
        also resistant to any cold damage. (Resistance will be explained later)''', 
                                              font = ('Arial', 30), bg = 'mint cream')
        self.lbl_traits_white.grid(row = 2, column = 0)
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 3, column = 0)
         
        
   





#Gnome
class race_Traits_Gnome(tk.Frame):
    def __init__(self):       
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_gnome_lbl = tk.Label(self, text = "Your Racial Traits (Gnome):", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_gnome_lbl.grid(row = 1, column = 0)
        
        self.lbl_warning_lbl = tk.Label(self, text = ''' Make sure to write all the information 
        you are given on either a piece of paper or a character sheet.''', 
                                              font = ('Arial', 20), fg = 'red',
                                              bg = 'mint cream')
        self.lbl_warning_lbl.grid(row = 2, column = 0) 
        
        self.lbl_traits_gnome = tk.Label(self, text = '''o Your intelligence score increases by 2
        o You are considered small in size
        o Your base speed is 25
        o You have advantage on all intelligence, wisdom, and charisma saving throws against magic
        o You can speak, read, and write, common and gnomish''', font = ('Arial', 18),
                                             bg = 'mint cream')
        self.lbl_traits_gnome.grid(row = 3, column = 0)
        
        self.lbl_sub_lbl = tk.Label(self, text = ''' Some classes have subclasses,
        which give additional traits. The subclasses of gnome are forest and
        rock gnomes. Forest gnomes increase your dexterity, you get a bonus spell to cast,
        and you can communicate with small beasts. Rock gnomes increase your constitution
        score,  you can add twice your proficiency bonus to intelligence checks based on
        magic items, alchemical items, or technological devices, and you can create small 
        devices. Choose wisely as you can not go back...''', 
                                              font = ('Arial', 20), fg = 'blue',
                                              bg = 'mint cream')
        self.lbl_sub_lbl.grid(row = 4, column = 0)
        
        self.btn_forest_btn = tk.Button(self, text = "Forest Gnome", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_forest)
        self.btn_forest_btn.grid(row = 5, column = 0)
        
        self.btn_rock_btn = tk.Button(self, text = "Rock Gnome", font = DEFAULT, bg = 'ivory', 
                                            activebackground = 'MistyRose2', command = self.raise_rock)
        self.btn_rock_btn.grid(row = 6, column = 0)
        
    def raise_forest(self):
        global DEX
        global SPELLS
        global OTHER
        SPELLS += 'Minor Illusion(Bonus), '
        DEX += 1
        OTHER += 'Can speak with small/smaller beasts, '
        print(SPELLS, DEX, OTHER)
        gnome_forest.tkraise()
        
    def raise_rock(self):
        global CON
        global PROFICIENCY
        global OTHER
        CON += 1
        PROFICIENCY += 'Intelligence(history) check related to magic items, alchemical objects, or technological devices, '
        OTHER += 'Tinkerer, '
        print(CON, PROFICIENCY, OTHER)
        gnome_rock.tkraise()

class race_Gnome_Forest(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Gnome Forest", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_forest = tk.Label(self, text = '''o Your dexterity score increases by 1
        o You know the minor illusion spell (Casted using INT)
        o Through sounds and and gestures you can speak with small and smaller beasts, but can only
        communicate simple ideas. ''', 
                                              font = DEFAULT, bg = 'mint cream')
        self.lbl_traits_forest.grid(row = 2, column = 0)       
        
        self.btn_str_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_str_btn.grid(row = 4, column = 0) 

class race_Gnome_Rock(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_race_lbl = tk.Label(self, text = "Gnome Rock", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_race_lbl.grid(row = 1, column = 0)

        self.lbl_traits_rock = tk.Label(self, text = '''o Your constitution score increases by 1
        o Whenever you make an Intelligence(history) check related to magic items, alchemical
        objects, or technological devices you can add twice your proficiency bonus.
        o You have proficiency  wuth artisan's tools. Using these tools you can spend 1 hour and 10 GP 
        worth of materials to construct a tiny clockwork device that has AC 5 and 1 HP. After 24 hours,
        the device will cease to function.
        o You can only have three devices active at a time.''', 
                                              font = DEFAULT, bg = 'mint cream')
        self.lbl_traits_rock.grid(row = 2, column = 0)
        
        self.lbl_traits_pick = tk.Label(self, text = '''DEVICES:
        Clockwork Toy: a clockwork animal, monster, or person. When placed on the ground, the toy
        moves 5 feet across the ground on each of your turns in a random direction.
        
        Fire Starter: The device produces a miniature flame, which you can use to light a candle,
        torch, or campfire. This device requires an action.
        
        Music Box: When opened, this music box plays a single song at a moderate volume. The box
        stops playing when it reaches the song's end or when it is closed.''', 
                                              font = DEFAULT, bg = 'mint cream', fg = 'red')
        self.lbl_traits_pick.grid(row = 3, column = 0)        
        
        self.btn_str_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_str_btn.grid(row = 4, column = 0) 
        




#Half-Elf
class race_Traits_HE(tk.Frame):
    def __init__(self):       
        tk.Frame.__init__(self, bg = 'mint cream')
        self.chosen = 0
        self.grid_columnconfigure(0, weight=1)
        self.lbl_he_lbl = tk.Label(self, text = "Your Racial Traits (Half-Elf):", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_he_lbl.grid(row = 1, column = 0)
        
        self.lbl_warning_lbl = tk.Label(self, text = ''' Make sure to write all the information 
        you are given on either a piece of paper or a character sheet.''', 
                                              font = ('Arial', 20), fg = 'red',
                                              bg = 'mint cream')
        self.lbl_warning_lbl.grid(row = 2, column = 0) 
        
        self.lbl_traits_he = tk.Label(self, text = '''o Your Charisma score increases by 2
        o Two other ability scores of your choice increase by 1
        o Your base speed is 30 feet
        o You have darkvision taht reaches 60 feet
        o You have advantage on saving throws against being charmed, and magic can't put you to sleep
        o You gain proficiency in two skills of your choice
        o You can speak, read, and write common and elvish and one exta language of your choice.''', font = ('Arial', 18),
                                             bg = 'mint cream')
        self.lbl_traits_he.grid(row = 3, column = 0)
        
        self.lbl_traits_pick = tk.Label(self, text = '''Please pick two attributes to increase by one. ''', 
                                              font = DEFAULT, bg = 'mint cream', fg = 'red')
        self.lbl_traits_pick.grid(row = 4, column = 0)        
        
        self.btn_str_btn = tk.Button(self, text = "Strength", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = self.disable_str)
        self.btn_str_btn.grid(row = 5, column = 0) 
        
        self.btn_dex_btn = tk.Button(self, text = "Dexterity", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = self.disable_dex)
        self.btn_dex_btn.grid(row = 6, column = 0)
        
        self.btn_con_btn = tk.Button(self, text = "Constitution", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = self.disable_con)
        self.btn_con_btn.grid(row = 7, column = 0)
        
        self.btn_int_btn = tk.Button(self, text = "Intelligence", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = self.disable_int)
        self.btn_int_btn.grid(row = 8, column = 0) 
        
        self.btn_wis_btn = tk.Button(self, text = "Wisdom", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = self.disable_wis)
        self.btn_wis_btn.grid(row = 9, column = 0)        
        
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 10, column = 0)  
        
    def disable_str(self):
        global STR
        STR += 1
        print(STR)
        self.btn_str_btn.configure(state = "disabled")
        self.chosen += 1
        if self.chosen >= 2:
            self.btn_dex_btn.configure(state = "disabled")
            self.btn_con_btn.configure(state = "disabled")
            self.btn_int_btn.configure(state = "disabled")
            self.btn_wis_btn.configure(state = "disabled")          
            
    
    def disable_dex(self):
        global DEX
        DEX += 1
        print(DEX)
        self.btn_dex_btn.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_str_btn.configure(state = "disabled")
            self.btn_con_btn.configure(state = "disabled")
            self.btn_int_btn.configure(state = "disabled")
            self.btn_wis_btn.configure(state = "disabled")

               
    
    def disable_con(self):
        global CON
        CON += 1
        print(CON)
        self.btn_con_btn.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_dex_btn.configure(state = "disabled")
            self.btn_str_btn.configure(state = "disabled")
            self.btn_int_btn.configure(state = "disabled")
            self.btn_wis_btn.configure(state = "disabled")
                 
    
    def disable_int(self):
        global INT
        INT += 1
        print(INT)
        self.btn_int_btn.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_dex_btn.configure(state = "disabled")
            self.btn_str_btn.configure(state = "disabled")
            self.btn_con_btn.configure(state = "disabled")
            self.btn_wis_btn.configure(state = "disabled")

        
    def disable_wis(self):
        global WIS
        WIS += 1
        print(WIS)
        self.btn_wis_btn.configure(state = "disabled")
        self.chosen += 1 
        if self.chosen >= 2:
            self.btn_dex_btn.configure(state = "disabled")
            self.btn_str_btn.configure(state = "disabled")
            self.btn_int_btn.configure(state = "disabled")
            self.btn_con_btn.configure(state = "disabled")

           

#Half-Orc
class race_Traits_Orc(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_orc_lbl = tk.Label(self, text = "Your Racial Traits (Half-Orc):", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_orc_lbl.grid(row = 1, column = 0)
        
        self.lbl_warning_lbl = tk.Label(self, text = ''' Make sure to write all the information 
        you are given on either a piece of paper or a character sheet.''', 
                                              font = ('Arial', 20), fg = 'red',
                                              bg = 'mint cream')
        self.lbl_warning_lbl.grid(row = 2, column = 0) 
        
        
        self.lbl_traits_orc = tk.Label(self, text = '''o Your strength increases by 2
        o Your constitution increases by 1
        o You have darkvision which extends 60ft
        o Your speed is 30ft
        o You have proficiency in the intimidation skill
        o When you are reduced to 0 hit points(health), you can drop to 1 HP instead
        o When you score a critical hit with a melee weapon attack you can roll one of 
        damage dice one more time and add it to the extra damage of the crit
        o You can speak, read, and write Common and Orc''', font = ('Arial', 18),
                                             bg = 'mint cream')
        self.lbl_traits_orc.grid(row = 3, column = 0)
        
    
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 4, column = 0)
    
class race_Traits_Tief(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_tief_lbl = tk.Label(self, text = "Your Racial Traits (Tiefling):", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_tief_lbl.grid(row = 1, column = 0)
        
        self.lbl_warning_lbl = tk.Label(self, text = ''' Make sure to write all the information 
        you are given on either a piece of paper or a character sheet.''', 
                                              font = ('Arial', 20), fg = 'red',
                                              bg = 'mint cream')
        self.lbl_warning_lbl.grid(row = 2, column = 0) 
        
        
        self.lbl_traits_tief = tk.Label(self, text = '''o Your intelligence score increases by 1
        o Your charisma score increases by 2
        o Your speed is 30ft
        o You have darkvision which extends 60ft
        o You have resistance to fire damage
        o You know the thaumaturgy spell as a bonus (As you increase in level
        you will get more bonus spells)
        o You can speak, read, and write Common and Infernal''', font = ('Arial', 18),
                                             bg = 'mint cream')
        self.lbl_traits_tief.grid(row = 3, column = 0)
        
    
        self.btn_cont_btn = tk.Button(self, text = "Continue", font = DEFAULT, bg = 'ivory',
                                            activebackground = 'MistyRose2', command = "")
        self.btn_cont_btn.grid(row = 4, column = 0)    
    
class class_Pick(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg = 'mint cream')
        self.grid_columnconfigure(0, weight=1)
        self.lbl_classes_lbl = tk.Label(self, text = "Classes", 
                                     font = DEFAULT, bg = 'mint cream')
        self.lbl_classes_lbl.grid(row = 1, column = 0)
        
          

#Creating the frames
root = tk.Tk()
root.title("DND Character Creator")

frame_menu = MainMenu()
frame_menu.grid(row = 0, column = 0, sticky = "news")

available_race = RaceMenu()
available_race.grid(row = 0, column = 0, sticky = "news")

available_class = class_Menu()
available_class.grid(row = 0, column = 0, sticky = "news")

dice = Dice()
dice.grid(row = 0, column = 0, sticky = "news")

start = Start()
start.grid(row = 0, column = 0, sticky = "news")

race_info = race_Info()
race_info.grid(row = 0, column = 0, sticky = "news")

race_info2 = race_Info2()
race_info2.grid(row = 0, column = 0, sticky = "news")

race_info3 = race_Info3()
race_info3.grid(row = 0, column = 0, sticky = "news")

race_traits_dwarf = race_Traits_Dwarf()
race_traits_dwarf.grid(row = 0, column = 0, sticky = "news")

hill_dwarf = race_Dwarf_Hill()
hill_dwarf.grid(row = 0, column = 0, sticky = "news")

mtn_dwarf = race_Dwarf_Mtn()
mtn_dwarf.grid(row = 0, column = 0, sticky = "news")

race_traits_elf = race_Traits_Elf()
race_traits_elf.grid(row = 0, column = 0, sticky = "news")

high_elf = race_Elf_High()
high_elf.grid(row = 0, column = 0, sticky = "news")

wood_elf = race_Elf_Wood()
wood_elf.grid(row = 0, column = 0, sticky = "news")

drow_elf = race_Elf_Drow()
drow_elf.grid(row = 0, column = 0, sticky = "news")

race_traits_halfling = race_Traits_Halfling()
race_traits_halfling.grid(row = 0, column = 0, sticky = "news")

half_light = race_Halfling_Light()
half_light.grid(row = 0, column = 0, sticky = "news")

half_stout = race_Halfling_Stout()
half_stout.grid(row = 0, column = 0, sticky = "news")

race_traits_human = race_Traits_Human()
race_traits_human.grid(row = 0, column = 0, sticky = "news")

human_variant = race_Human_Variant()
human_variant.grid(row = 0, column = 0, sticky = "news")

human_regular = race_Human_Regular()
human_regular.grid(row = 0, column = 0, sticky = "news")

race_traits_dragonborn = race_Traits_Dragonborn()
race_traits_dragonborn.grid(row = 0, column = 0, sticky = "news")

dragon_black = race_Dragonborn_Black()
dragon_black.grid(row = 0, column = 0, sticky = "news")

dragon_blue = race_Dragonborn_Blue()
dragon_blue.grid(row = 0, column = 0, sticky = "news")

dragon_brass = race_Dragonborn_Brass()
dragon_brass.grid(row = 0, column = 0, sticky = "news")

dragon_white = race_Dragonborn_White()
dragon_white.grid(row = 0, column = 0, sticky = "news")

dragon_bronze = race_Dragonborn_Bronze()
dragon_bronze.grid(row = 0, column = 0, sticky = "news")

dragon_copper = race_Dragonborn_Copper()
dragon_copper.grid(row = 0, column = 0, sticky = "news")

dragon_gold = race_Dragonborn_Gold()
dragon_gold.grid(row = 0, column = 0, sticky = "news")

dragon_green = race_Dragonborn_Green()
dragon_green.grid(row = 0, column = 0, sticky = "news")

dragon_red = race_Dragonborn_Red()
dragon_red.grid(row = 0, column = 0, sticky = "news")

dragon_silver = race_Dragonborn_Silver()
dragon_silver.grid(row = 0, column = 0, sticky = "news")

race_traits_gnome = race_Traits_Gnome()
race_traits_gnome.grid(row = 0, column = 0, sticky = "news")

gnome_forest = race_Gnome_Forest()
gnome_forest.grid(row = 0, column = 0, sticky = "news")

gnome_rock = race_Gnome_Rock()
gnome_rock.grid(row = 0, column = 0, sticky = "news")

race_traits_he = race_Traits_HE()
race_traits_he.grid(row = 0, column = 0, sticky = "news")

race_traits_orc = race_Traits_Orc()
race_traits_orc.grid(row = 0, column = 0, sticky = "news")

race_traits_tief = race_Traits_Tief()
race_traits_tief.grid(row = 0, column = 0, sticky = "news")


frame_menu.tkraise()
root.mainloop()