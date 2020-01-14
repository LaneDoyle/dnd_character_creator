This is the original code of the program, which did not have a GUI.

By Lane Doyle
Created on 11/1/19

''' A program which helps a beginner learn how to create D&D characters'''

import dieroller as dr

#Basic Variables
user_command = "" #Determines which command user has typed in and acts accordingly
user_race = "" #Determines which race the user wants for their character
user_name = "" #The character's name chosen by the user
user_subrace = "" #The subrace chosen by the user

#Stat Variables
stat_str = 0 #Strength Score 
stat_dex = 0 #Dexterity Score 
stat_con = 0 #Constitution Score 
stat_int = 0 #Intelligence Score
stat_wis = 0 #Wisdom Score 
stat_cha = 0 #Charisma Score


#Functions
def Menu_classes():
    print(''' Available classes:
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
        Wizard''')
    user_command = input("Please type in the command you wish you use. ")

def Menu_races():
    print(''' Available races: Dwarf, Elf, Halfling, Human, Dragonborn, Gnomes, Half-Elf, 
        Half-Orc, Tiefling''')
    user_command = input("Please type in the command you wish you use. ")

def Menu_die():
    print('''Die:
        1d4- a four sided dice using numbers 1-4.
        1d6- a six sided dice using numbers 1-6.
        1d8- an eight sided dice using numbers 1-8.
        1d12- a twelve sided dice using numbers 1-12.
        1d20- a twenty sided dice using numbers 1-20.''')
    user_command = input("Please type in the command you wish you use. ")

def Menu_back():
    print('''Welcome to the D&D Character Creator! This program can help beginners
        make their first D&D character at first level!''')
    user_command = input("Confused on where to start? Type HELP. Or, type in the command you wish you use. ")

def Menu_help():
    print(''' Commands:
        HELP: shows the list of commands users can use.
        CLASSES: shows the list of classes available to the player.
        DIE: shows the types of die available for use.
        RACES: shows the available races and their attributes.
        BACK: returns to the start screen.
        PLAY: begins the creation process''')
    user_command = input("Please type in the command you wish you use. ")





#Code
#Introduction
print('''Welcome to the 5th Edition D&D Character Creator! This program can help beginners
make their first D&D character at first level! This creator will focus on races, classes, and
backgrounds which appear in the Player's Handbook.''')


user_command = input("Confused on where to start? Type HELP. Or, type in the command you wish you use. (Type PLAY to start!) ")

if user_command == "CLASSES": 
    Menu_classes()
    Menu_back()
elif user_command == "DIE":
    Menu_die()
    Menu_back() 
elif user_command == "RACES":
    Menu_races()
    Menu_back()
elif user_command == "HELP":
    Menu_help()
    Menu_back()

#Starts Creator
elif user_command == "PLAY":
    #Fake loading
    print('''



    Creating Creation Process....









    Creating Races...











    Killing off Goblins...

    ''')  

    print('''
    Alright! Let's start!
    ''')

    print(''' 
    There are several layers to the character creation process. First, let's start with your character's 
    race. You surely looked at the races beforehand...right? Just kidding! I know you didn't. So, I grabbed 
    an extra copy of the list of races! Here they are: 
        Dwarf
        Elf
        Halfling
        Human
        Dragonborn
        Gnomes
        Half-Elf
        Half-Orc
        Tiefling
    ''')

    print(''' 

    ''')
    user_name = input("What's your character's name? ")
    print("Let's create " + user_name + "!")
    #End of fake loading

    #Choosing a race
    print(''' To know more about each race, just type 'INFO', or choose your race!
 To choose your race type the race name ex. 'DWARF' ''')
    print(''' It is also important to note that things such as advantage, proficiency, etc.
 will be explained later! I would also reccommend writing all this down! :) ''')
    user_race = input("Please pick your race: ")
    if user_race == "INFO":
        print(''' Race Info:
        Dwarf: Dwarves have an appearance similar to humans, if humans were all naturally
        under 5ft. Dwarves can live over 400 years old. Tiny but mighty, they are skilled 
        warriors in battle. They stand around 4 to  5ft tall and weigh around 150. Hardy 
        creatures, your constitution (vitality) score increases by 2 when you are a dwarf.

        Elf: Elves are graceful creatures. They live for centuries and hold vast knowledge of the
        world around them. Elves can live to be 750 years old. They are, on average, 5 or over 6 ft
        tall. Their weight is similar to a human's. As an elf your dexterity (agility) increases by 2.

        Halfling: Halflings are shorter than dwarves. They are skilled in fitting into communities and
        are fiercely loyal to their allies. They reach adulthood around the age of 20 and live into the
        middle of their second century. On average halflings stand about 3 ft tall and weigh 40 pounds.
        As a halfling your dexterity (agility) increases by 2.

        Human: The most recognizable race, humans are adaptable and ambitious. Because of their shorter
        life spans, they do not hesitate to seize the moment. Humans live less than a century. Their height
        and weight vary greatly, from being 5 to over 6 ft tall and 100 to 200 pounds or more. As a human,
        each of your ability scores increase by one. 

        Dragonborn: The kin of dragons, dragonborn resemble a dragon-like humanoid, although they have no tail
        or wings. Their scale color can range from blue to gold. Their clans are the most important thing in their
        lives. Dragonborn usually live to around 80 years old. On average they are well over 6 ft tall and are around
        250 pounds. As a dragonborn, your strength score increases by 2 and your charisma (confidence, charm, etc.) 
        score increases by 1.

        Gnome: About the size of a halfling, the gnome has a delightful energy about them, greatly enjoying the life
        they lead. A gnome's appearance generally tells all you need to know about their personality. They are curious
        people, and enjoy each and every moment. Gnomes can live to almost 500 years old and are, on average, 3 to 4 ft 
        tall and 40 pounds. As a gnome, your intelligence score increases by 2. 

        Half-Elf: A mix of human and elf, half-elves are usually curious adventurers are quick talking diplomats. They 
        appear to be human, except their ears are pointy and they have the eyes of their elven parents. They live to 
        be around 180 years old and average a height of 5 to 6 ft tall. They have about the same weight as a human. As
        a half-elf, your charisma (confidence, charm, etc.) score increases by two and two other ability scores of your 
        choice increase by 1.

        Half-Orc: A mix of human and orc, half-orcs are more than intimidating. Their large figures, jutting jaws, and sharp 
        teeth, can be seen are terrifying by others. Most have scars they collected from battle, while some have scars which
        mark them as an exile. Regardless of the meaning, most half-orcs are marked by at least one scar. However, they rarely
        live longer than 75 years old. They average around 5 to well over 6 ft tall and can be around 200 pounds or more. As 
        a half-orc, your strength score increases by 2, and your constitution (vitality) score increases by 1. 

        Tiefling: Although appearing similar to humans, tieflings have large horns which take a variety of shapes. Their skin
        color is the same as a human's except some have various shades of red as their skin color. They also have thick tails
        which are around 4 or 5 ft long and solid-colored eyes. They believe trust is earned, not given freely. They live about
        the same length as a human, plus a few years. They have the same average height and weight of a human. As a tiefling,
        your intelligence score increases by 1 and your charisma (confidence, charm, etc.) increases by 2. ''')
        user_race = input("Please pick your race: ")
        if user_race == "DWARF":
            print('''You have chosen Dwarf as your class. Congrats! You get the following abilities:
            o Your Constitution increase by 2.
            o Your speed is 25 ft per turn.
            o You can see in dim light within 60 ft of you as if it were bright light and in darkness
            as if it were dim light.
            o You have advantage on saving throws against poison and resistance to poison damage.
            o You have proficiency with the battleaxe, handaxe, throwing hammer, and warhammer.
            o You have proficiency with one set of tools of your choice: smith's tools, brewer's supplies, or
            mason's tools. 
            o Whenever you make a history check related to the origin of stonework, you can add your proficiency
            bonus to the check and double it.
            o You can speak, read, and write Dwarvish. ''')
            print()
            print("There are two subraces of dwarves, hill dwarves and mountain dwarves.")
            print('''Hill Dwarves: Hill dwarves have keen senses, incredible intuition and unbeatable
            resilience. As a hill dwarf, your wisdom score increases by 1 and your maximum health 
            increases by 1, and it continues to increase by 1 everytime you level up.''')
            print()
            print('''Mountain Dwarves: Mountain dwarves are hardy creatures used to rough terrain. They
            are a little taller than a hill dwarf and have a lighter skin color. As a mountain dwarf, your
            strength score increases by 2 and you have proficiency using medium and light armor.''')
            user_subrace = input("Please type either 'HILL' or 'MOUNTAIN' based on the subrace you choose. ")
            print("Alright! " + user_name + " is a " + user_subrace + " " + user_race + "!")
        elif user_race == "ELF":
            print('''You have chosen Elf as your class. Congrats! You get the following abilities:
            o Your dexterity score increases by 2.
            o Your walking speed is 30 ft per turn.
            o You can see in dim light within 60 ft of you as if it were bright light and in darkness
            as if it were dim light.
            o You have proficiency in the perception skill.
            o You have advantage on saving throws against being charmed, and magic can't put you to
            sleep.
            o Elves do not require sleep, instead they meditate deeply for 4 hours a day.
            o You can speak, read, and write Elvish.''')
            print()
            print("There are three subraces of elves, high elves, wood elves, and dark elves.")
            print('''High Elf: A master of magic, the high elf is a very intelligent being. As a 
            high elf your intelligence increases by 1 and you are proficient with the longsword,
            shortbow, and longbow. You also know one cantrip of your choice from the wizard spell
            list, using intelligence as your spellcasting ability. You can also speak, read, and write
            one extra language.''')
            print()
            print('''Wood Elf: The wood elf is a stealthy and quick individual. They have copperish skin with 
            copper colored hair and green/brown/hazel eyes.As a wood elf your wisdom increases by 1 and you are 
            proficient with the longsword, shortsword, shortbow, and longbow. Your base walking speed increases 
            by 35 ft anf you can attempt to hide even when you are only lightly obscured by foliage, heavy rain, 
            falling snow, mist, etc.''')
            print()
            print('''Dark Elf(Drow): Banished from the surface, the drow now call the Underdark their home.
            They usually have very dark skin and pale eyes with white or yellow hair. Your charisma score 
            increases by one and your darkvision extends to 120 ft. Drow, being from underground, have
            disadvantage on attack rolls and on wisdom checks that rely on sight when you, your target,
            or whatever you are trying to see is in sunlight. You know the dancing lights cantrip, and are
            profiecient with rapiers, shortswords, and hand crossbows.''')
            user_subrace = input("Please type 'HIGH', 'WOOD', or 'DARK' based on the subrace you choose. ")
            print("Alright! " + user_name + " is a " + user_subrace + " " + user_race + "!")
    elif user_race == "DWARF":
        print('''You have chosen Dwarf as your class. Congrats! You get the following abilities:
        o Your Constitution increase by 2.
        o Your speed is 25 ft per turn.
        o You can see in dim light within 60 ft of you as if it were bright light and in darkness
        as if it were dim light.
        o You have advantage on saving throws against poison and resistance to poison damage.
        o You have proficiency with the battleaxe, handaxe, throwing hammer, and warhammer.
        o You have proficiency with one set of tools of your choice: smith's tools, brewer's supplies, or
        mason's tools. 
        o Whenever you make a history check related to the origin of stonework, you can add your proficiency
        bonus to the check and double it.
        o You can speak, read, and write Dwarvish. ''')
        print()
        print("There are two subraces of dwarves, hill dwarves and mountain dwarves.")
        print('''Hill Dwarves: Hill dwarves have keen senses, incredible intuition and unbeatable
        resilience. As a hill dwarf, your wisdom score increases by 1 and your maximum health 
        increases by 1, and it continues to increase by 1 everytime you level up.''')
        print()
        print('''Mountain Dwarves: Mountain dwarves are hardy creatures used to rough terrain. They
        are a little taller than a hill dwarf and have a lighter skin color. As a mountain dwarf, your
        strength score increases by 2 and you have proficiency using medium and light armor.''')
        user_subrace = input("Please type either 'HILL' or 'MOUNTAIN' based on the subrace you choose. ")
        print("Alright! " + user_name + " is a " + user_subrace + " " + user_race + "!")
    elif user_race == "ELF":
        print('''You have chosen Elf as your class. Congrats! You get the following abilities:
        o Your dexterity score increases by 2.
        o Your walking speed is 30 ft per turn.
        o You can see in dim light within 60 ft of you as if it were bright light and in darkness
        as if it were dim light.
        o You have proficiency in the perception skill.
        o You have advantage on saving throws against being charmed, and magic can't put you to
        sleep.
        o Elves do not require sleep, instead they meditate deeply for 4 hours a day.
        o You can speak, read, and write Elvish.''')
        print()
        print("There are three subraces of elves, high elves, wood elves, and dark elves.")
        print('''High Elf: A master of magic, the high elf is a very intelligent being. As a 
        high elf your intelligence increases by 1 and you are proficient with the longsword,
        shortbow, and longbow. You also know one cantrip of your choice from the wizard spell
        list, using intelligence as your spellcasting ability. You can also speak, read, and write
        one extra language.''')
        print()
        print('''Wood Elf: The wood elf is a stealthy and quick individual. They have copperish skin with 
        copper colored hair and green/brown/hazel eyes.As a wood elf your wisdom increases by 1 and you are 
        proficient with the longsword, shortsword, shortbow, and longbow. Your base walking speed increases 
        by 35 ft anf you can attempt to hide even when you are only lightly obscured by foliage, heavy rain, 
        falling snow, mist, etc.''')
        print()
        print('''Dark Elf(Drow): Banished from the surface, the drow now call the Underdark their home.
        They usually have very dark skin and pale eyes with white or yellow hair. Your charisma score 
        increases by one and your darkvision extends to 120 ft. Drow, being from underground, have
        disadvantage on attack rolls and on wisdom checks that rely on sight when you, your target,
        or whatever you are trying to see is in sunlight. You know the dancing lights cantrip, and are
        profiecient with rapiers, shortswords, and hand crossbows.''')
        user_subrace = input("Please type 'HIGH', 'WOOD', or 'DARK' based on the subrace you choose. ")
        print("Alright! " + user_name + " is a " + user_subrace + " " + user_race + "!")   
    elif user_race == "HALFLING":
        print('''You have chosen Halfling as your class. Congrats! You get the following abilities:
        o Your dexterity score increases by 2.
        o Your base walking speed is 25 ft per turn.
        o When you roll a 1 on an attack roll, skill check, or saving throw, you can reroll the die and
        must use the new roll.
        o You have advantage on saving throws against being frightened.
        o You can move through the space of any creature that is of a size larger than yours.
        o You can speak, read, and write Common and Halfling.''')
        print()
        print("There are two subraces of halflings, Lightfoot and Stout.")
        print('''Lightfoot Halfling: Silent creatures, lightfoot halflings can easily hide from sight.
        As a lightfoot halfling your charisma score increases by 1 and you can attempt to hide even when
        you are obscured only by a creature that is at least one size larger than you.''')
        print()
        print('''Stout Halfling: Stout Halflings are hardier creatures that are rumored to have dwarven
        blood. As a stout halfling your constitution score increases by 1 and you have advantage on saving
        throws against poison, and you have resistance against poison damage.''')
        print()
        user_subrace = input("Please type 'LIGHTFOOT' or 'STOUT' based on the subrace you choose. ")
        print("Alright! " + user_name + " is a " + user_subrace + " " + user_race + "!")    
    elif user_race == "HUMAN":
        print('''You have chosen Human as your class. Congrats! You get the following abilities:
        o Your ability scores each increase by 1.
        o Your base walking speed is 30 ft per turn.
        o You can speak, read, and write Common and one extra language of your choice.''')
        print()
        user_subrace == ""
        print("Alright! " + user_name + " is a " + " " + user_race + "!") 
    elif user_race == "DRAGONBORN":
        print('''You have chosen Human as your class. Congrats! You get the following abilities:
        o Your strength score increases by 2.
        o Your charisma score increases by 1.
        o Your base walking speed is 30 ft per turn.
        o You can speak, read, and write Common and Draconic.''')
        print()
        print('''Each dragon has a breath weapon such as fire breath. Depending on the color
        the breath weapon type varies. Here they are:
        Black = Acid
        Blue = Lightning
        Brass = Fire
        Bronze = Lightning
        Copper = Acid
        Gold = Fire
        Green = Poison
        Red = Fire
        Silver = Cold (Ice)
        White = Cold (Ice)''')
        print()
        user_subrace = input("Please type the color of dragon you chose. Ex. 'BLACK'.")
        if user_subrace == "BLACK":
            print('''You have chosen black as your type! You are resistant to acid damage!''')
        elif user_subrace == "BLUE":
            print('''You have chosen blue as your type! You are resistant to lightning damage!''')  
        elif user_subrace == "BRASS":
            print('''You have chosen brass as your type! You are resistant to fire damage!''')
        elif user_subrace == "BRONZE":
            print('''You have chosen bronze as your type! You are resistant to lightning damage!''')
        elif user_subrace == "COPPER":
            print('''You have chosen copper as your type! You are resistant to acid damage!''')
        elif user_subrace == "GOLD":
            print('''You have chosen gold as your type! You are resistant to fire damage!''')
        elif user_subrace == "GREEN":
            print('''You have chosen green as your type! You are resistant to poison damage!''')
        elif user_subrace == "RED":
            print('''You have chosen red as your type! You are resistant to fire damage!''')
        elif user_subrace == "SILVER":
            print('''You have chosen silver as your type! You are resistant to cold damage!''')
        elif user_subrace == "WHITE":
            print('''You have chosen white as your type! You are resistant to cold damage!''')        
        print()
        print("Alright! " + user_name + " is a " + user_subrace + " " + user_race + "!")      











