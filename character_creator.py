#!/usr/bin/python3
#Lane Doyle
#11/1/19

''' A program which helps a beginner learn how to create D&D characters'''

#Variables
user_command = "" #Determines which command user has typed in and acts accordingly



#Functions



#Code
#Introduction
print('''Welcome to the D&D Character Creator! This program can help beginners
make their first D&D character at first level!''')
user_command = input("Confused on where to start? Type HELP. Or, type in the command you wish you use. (Type PLAY to start!) ")
if user_command == "CLASSES": 
    print(''' Available classes:''')
    user_command = input("Please type in the command you wish you use. ")
    if user_command == "DIE":
        print('''Die:
        1d4- a four sided dice using numbers 1-4.
        1d6- a six sided dice using numbers 1-6.
        1d8- an eight sided dice using numbers 1-8.
        1d12- a twelve sided dice using numbers 1-12.
        1d20- a twenty sided dice using numbers 1-20.''')
        user_command = input("Please type in the command you wish you use. ")
    elif user_command == "RACES":
        print(''' Available races:''')
        user_command = input("Please type in the command you wish you use. ")
    elif user_command == "BACK":
        print('''Welcome to the D&D Character Creator! This program can help beginners
        make their first D&D character at first level!''')
        user_command = input("Confused on where to start? Type HELP. Or, type in the command you wish you use. ")  
#Die Menu
elif user_command == "DIE":
    print('''Die:
    1d4- a four sided dice using numbers 1-4.
    1d6- a six sided dice using numbers 1-6.
    1d8- an eight sided dice using numbers 1-8.
    1d12- a twelve sided dice using numbers 1-12.
    1d20- a twenty sided dice using numbers 1-20.''')
    user_command = input("Please type in the command you wish you use. ")
    if user_command == "CLASSES":
        print(''' Available classes:''')
        user_command = input("Please type in the command you wish you use. ")        
    elif user_command == "RACES":
        print(''' Available races:''')
        user_command = input("Please type in the command you wish you use. ")
    elif user_command == "BACK":
        print('''Welcome to the D&D Character Creator! This program can help beginners
        make their first D&D character at first level!''')
        user_command = input("Confused on where to start? Type HELP. Or, type in the command you wish you use. ")  
#Races Menu
elif user_command == "RACES":
    print(''' Available races:''')
    user_command = input("Please type in the command you wish you use. ")
    if user_command == "CLASSES":
        print(''' Available classes:''')
        user_command = input("Please type in the command you wish you use. ")        
    elif user_command == "BACK":
        print('''Welcome to the D&D Character Creator! This program can help beginners
        make their first D&D character at first level!''')
        user_command = input("Confused on where to start? Type HELP. Or, type in the command you wish you use. ") 
    elif user_command == "DIE":
        print('''Die:
        1d4- a four sided dice using numbers 1-4.
        1d6- a six sided dice using numbers 1-6.
        1d8- an eight sided dice using numbers 1-8.
        1d12- a twelve sided dice using numbers 1-12.
        1d20- a twenty sided dice using numbers 1-20.''') 
#Back Menu
elif user_command == "BACK":
    print('''Welcome to the D&D Character Creator! This program can help beginners
    make their first D&D character at first level!''')
    user_command = input("Confused on where to start? Type HELP. Or, type in the command you wish you use. ") 
    if user_command == "HELP":
        print(''' Commands:
        HELP: shows the list of commands users can use.
        CLASSES: shows the list of classes available to the player.
        DIE: shows the types of die available for use.
        RACES: shows the available races and their attributes.
        BACK: returns to the start screen.''')
        user_command = input("Please type in the command you wish you use. ")        
    elif user_command == "RACES":
        print(''' Available races:''')
        user_command = input("Please type in the command you wish you use. ")
    elif user_command == "CLASSES":
        print(''' Available classes:''')
        user_command = input("Please type in the command you wish you use. ")        
    elif user_command == "DIE":
        print('''Die:
        1d4- a four sided dice using numbers 1-4.
        1d6- a six sided dice using numbers 1-6.
        1d8- an eight sided dice using numbers 1-8.
        1d12- a twelve sided dice using numbers 1-12.
        1d20- a twenty sided dice using numbers 1-20.''')

#Help Menu
if user_command == "HELP":
    print(''' Commands:
    HELP: shows the list of commands users can use.
    CLASSES: shows the list of classes available to the player.
    DIE: shows the types of die available for use.
    RACES: shows the available races and their attributes.
    BACK: returns to the start screen.
    PLAY: begins the creation process''')
    user_command = input("Please type in the command you wish you use. ")
    if user_command == "CLASSES":
        print(''' Available classes:''')
        user_command = input("Please type in the command you wish you use. ")
    elif user_command == "DIE":
        print('''Die:
        1d4- a four sided dice using numbers 1-4.
        1d6- a six sided dice using numbers 1-6.
        1d8- an eight sided dice using numbers 1-8.
        1d12- a twelve sided dice using numbers 1-12.
        1d20- a twenty sided dice using numbers 1-20.''')
        user_command = input("Please type in the command you wish you use. ")
    elif user_command == "RACES":
        print(''' Available races:''')
        user_command = input("Please type in the command you wish you use. ")
    elif user_command == "BACK":
        print('''Welcome to the D&D Character Creator! This program can help beginners
        make their first D&D character at first level!''')
        user_command = input("Confused on where to start? Type HELP. Or, type in the command you wish you use. ")    
#Classes Menu
elif user_command == "CLASSES":
    print(''' Available classes:''')
    user_command = input("Please type in the command you wish you use. ")
    if user_command == "DIE":
        print('''Die:
        1d4- a four sided dice using numbers 1-4.
        1d6- a six sided dice using numbers 1-6.
        1d8- an eight sided dice using numbers 1-8.
        1d12- a twelve sided dice using numbers 1-12.
        1d20- a twenty sided dice using numbers 1-20.''')
        user_command = input("Please type in the command you wish you use. ")
    elif user_command == "RACES":
        print(''' Available races:''')
        user_command = input("Please type in the command you wish you use. ")
    elif user_command == "BACK":
        print('''Welcome to the D&D Character Creator! This program can help beginners
        make their first D&D character at first level!''')
        user_command = input("Confused on where to start? Type HELP. Or, type in the command you wish you use. ")  
#Die Menu
elif user_command == "DIE":
    print('''Die:
    1d4- a four sided dice using numbers 1-4.
    1d6- a six sided dice using numbers 1-6.
    1d8- an eight sided dice using numbers 1-8.
    1d12- a twelve sided dice using numbers 1-12.
    1d20- a twenty sided dice using numbers 1-20.''')
    user_command = input("Please type in the command you wish you use. ")
    if user_command == "CLASSES":
        print(''' Available classes:''')
        user_command = input("Please type in the command you wish you use. ")        
    elif user_command == "RACES":
        print(''' Available races:''')
        user_command = input("Please type in the command you wish you use. ")
    elif user_command == "BACK":
        print('''Welcome to the D&D Character Creator! This program can help beginners
        make their first D&D character at first level!''')
        user_command = input("Confused on where to start? Type HELP. Or, type in the command you wish you use. ")  
#Races Menu
elif user_command == "RACES":
    print(''' Available races:''')
    user_command = input("Please type in the command you wish you use. ")
    if user_command == "CLASSES":
        print(''' Available classes:''')
        user_command = input("Please type in the command you wish you use. ")        
    elif user_command == "BACK":
        print('''Welcome to the D&D Character Creator! This program can help beginners
        make their first D&D character at first level!''')
        user_command = input("Confused on where to start? Type HELP. Or, type in the command you wish you use. ") 
    elif user_command == "DIE":
        print('''Die:
        1d4- a four sided dice using numbers 1-4.
        1d6- a six sided dice using numbers 1-6.
        1d8- an eight sided dice using numbers 1-8.
        1d12- a twelve sided dice using numbers 1-12.
        1d20- a twenty sided dice using numbers 1-20.''')
#Back Menu
elif user_command == "BACK":
    print('''Welcome to the D&D Character Creator! This program can help beginners
    make their first D&D character at first level!''')
    user_command = input("Confused on where to start? Type HELP. Or, type in the command you wish you use. ") 
    if user_command == "HELP":
        print(''' Commands:
        HELP: shows the list of commands users can use.
        CLASSES: shows the list of classes available to the player.
        DIE: shows the types of die available for use.
        RACES: shows the available races and their attributes.
        BACK: returns to the start screen.''')
        user_command = input("Please type in the command you wish you use. ")        
    elif user_command == "RACES":
        print(''' Available races:''')
        user_command = input("Please type in the command you wish you use. ")
    elif user_command == "CLASSES":
        print(''' Available classes:''')
        user_command = input("Please type in the command you wish you use. ")        
    elif user_command == "DIE":
        print('''Die:
        1d4- a four sided dice using numbers 1-4.
        1d6- a six sided dice using numbers 1-6.
        1d8- an eight sided dice using numbers 1-8.
        1d12- a twelve sided dice using numbers 1-12.
        1d20- a twenty sided dice using numbers 1-20.''') 
#Play Menu
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
    ''')
    
    print(''' 
    Barbarian
    Warlock
    Fighter
    Wizard
    Sorcerer
    Monk
    Paladin
    Cleric
    ''')
    


