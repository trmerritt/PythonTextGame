#copyright@trm 2023 Spring - a simple choose own adventure text based game
#this game consists mainly of functions


def welcome():
    print("""Note: To play this game, simply type your choice of one of the two
options given in square brackets at each level of the game. Enjoy!
\n You are a brave adventurer. You have been walking for several days and now you come across a large forest up ahead, 
    stretching for as far as you can see on both sides. You enter the forest and almost immediately there is a path with a fork. 
    Do you turn [left] or [right]?> """)
    option = input("").lower().strip()
    if option == "left":
        leftFork()
    elif option == "right":
        rightFork()
    else:
        invalidChoice()

def invalidChoice():
    print("That is invalid. Please try again")
    welcome()

def leftFork():
    print("""You walk down the left fork of the path, where a swamp begins to appear on the right side,
    within a few minutes you are attacked by a crocodile and eaten, as you did not see the creature in
    the tall grass. Game over""")
    option = input("Wanna start the adventure again. [yes] or [no]?> ").strip().lower()
    if option == "yes":
        welcome()
    else:
        print("Thanks for playing")
        quit()

def rightFork():
    print("""You have made the right choice as you walk along the right path and do not have any troubles
    so far. Up ahead there is a small hut with smoke coming out of its chimney. Hungry and tired, you must
    decide whether or not to trust the occupants. Do you [knock] the door or [ignore] the building?> """)
    option = input("").lower().strip()
    if option == "ignore":
        ignore()
    elif option == "knock":
        knock()
    else:
        invalidChoice()


def ignore():
    print("""You don't trust the occupant of the building and carry on, despite being hungry and thirsty.
    Unfortunately as you continue through the forest, the trees and bushes around you become more barren
    and you can no longer find sources of sustenance. Exhausted, you eventually give up and starve. Game over""")
    option = input("Wanna start the adventure again. [yes] or [no]?> ").strip().lower()
    if option == "yes":
        welcome()
    else:
        print("Thanks for playing")
        quit()


def knock():
        print("""You make the right choice and a lonely and kind old woman opens the door. Happy to finally
        have a friend, she welcomes you in and makes a filling supper to share, gives you a safe place to sleep
        for the night as well as packs up a hamper of food and water to sustain you along the path as she warns it
        is a very barren area of the forest just a little way away and you will need it.\n
        You thank her the next day and continue your journey. For a few days you travel the barren part of the forest
        with your useful hamper of food. You eventually make it to a wide river. Do you attempt to [cross] via a
        fragile looking bridge? Or do you avoid crossing, change course, and instead walk along the marshy [bank]?> """)
        option = input("").strip().lower()
        if option == "cross":
            cross()
        elif option == "bank":
            bank()
        else:
            invalidChoice()

def bank():
    print("""You walk only a few steps into the marshy bank alongside the river, as within seconds you are
    stuck and cannot get out of the thick mud which causes you to sink. Game over""")
    option = input("Wanna start the adventure again. [yes] or [no]?> ").strip().lower()
    if option == "yes":
        welcome()
    else:
        print("Thanks for playing")
        quit()

def cross():
    print("""You cross the bridge and although it appeared fragile, you manage to walk across it without problem.
    Up ahead, you notice there is a rather large clearing and within that clearing there appears a town within
    a thick square of large castle walls. You eventually come closer eager to enter the castle but aware
    the townsfolk may be very hostile to outsiders so you must decide now if to sneak in or reason your 
    way in. Do you dive under the [moat] or try the [drawbridge] to speak to the guards?> """)
    option = input("").strip().lower()
    if option == "drawbridge":
        drawbridge()
    elif option == "moat":
        moat()
    else:
        invalidChoice()

def drawbridge():
    print("""You walk toward the drawbridge hoping to reason with the guards so they might let you into
     the castle but they are hostile as you had feared and as soon as they see you shoot arrows at you. Game over""")
    option = input("Wanna start the adventure again. [yes] or [no]?> ").strip().lower()
    if option == "yes":
        welcome()
    else:
        print("Thanks for playing")
        quit()

def moat():
    print("""You dive under the moat and make it under the castle walls without problem. However, within
     a few moments, a guard sees you. Do you [attack] or [run]?> """)
    option = input("").strip().lower()
    if option == "run":
        run()
    elif option == "attack":
        attack()
    else:
        invalidChoice()

def run():
    print("""You run and in doing so give the guard time to shout and alert more guards. They all shoot
     arrows at you and you dont get away and instead perish. Game over""")
    option = input("Wanna start the adventure again. [yes] or [no]?> ").strip().lower()
    if option == "yes":
        welcome()
    else:
        print("Thanks for playing")
        quit()

def attack():
    print("""You subdue to guard quickly and silently, avoiding any further negative attention, allowing
     you to continue further into the small secretive town. Up ahead, you see a set of stone steps. Do you
     go [up] or [down] them?> """)
    option = input("").strip().lower()
    if option == "up":
        up()
    elif option == "down":
        down()
    else:
        invalidChoice()

def down():
    print("""You go down the stone steps and soon get lost in a seemingly endless network of tunnels
    under the town. It is so dark and confusing. It is too late by the time you realise the tunnels form
    a sewage system under the town, and you thus drown as water suddenly floods the tunnels. Game over""")
    option = input("Wanna start the adventure again. [yes] or [no]?> ").strip().lower()
    if option == "yes":
        welcome()
    else:
        print("Thanks for playing")
        quit()

def up():
    print("""You go up the stone steps, and after a few quiet corridors you come to a large set of grand doors.
    You open them timidly and enter the room. The king of the town is inside and he is pleasantly suprised by
    your bravery rather than angry as you recount your journey to him. Because he is impressed by your bravery
    and intelligence, he decides to reward you thousands of gold coins as well as providing you a job
    as his assistant in making his kingdom safer by warning him of potential weaknesses and therefore you
    end up a successful and rich member of his kingdom. \n
    Congrats! You have won the game!!! \n
    Wanna play again [yes] or [no] ?> """)
    option = input("").strip().lower()
    if option == "yes":
        welcome()
    else:
        quit()

welcome()
