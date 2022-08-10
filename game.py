import random
import msvcrt as m
import classes as c
import dictionaries as d
import functions as f

# Set room variables.
# These variables keep track of how many and what rooms the player has passed through.
room_count = 0
trade_count = 0
last_room = ""
room_tracker = []

def play(character: object):
    """Function to control the core gameplay loop.
    
    Passes the Player object through a series of 30 pseudo-randomly chosen Rooms, calling the appropriate functions from the function module.
    Checks for death after each combat and event Room and triggers the appropriate combat resolution.
    If player survives all rooms, player encounters the Final Boss combat - if player is victorious, triggers endgame and prompts player to Play Again or Exit.
    
    Parameters
    ----------
    character:
        The Player object.

    """
    
    global room_count
    global trade_count
    global last_room
    global room_tracker

    while room_count <= 29:
        # Increment room count on each loop.
        room_count += 1
        if room_count == 1:
            # Room 1 always the same - set the scene.
            print("===============")
            print("Awaken - Room", str(room_count))
            print("===============\n")
            for text in d.awaken_text:
                text = f.wrap_text(text)
                for line in text:
                    print(line)
                print("")
                m.getch()
            character.coin_gain(20)
            f.starter_gear(character)
            f.starter_abilities(character)
            print("Press any key to continue.\n")
            m.getch()
            continue
        # Room 2 and rooms divisible by 4 always the same - fight.
        elif room_count == 2 or room_count % 4 == 0:
            room = d.rooms[0]
            last_room = room
        # Rooms 10 and 20 always the same - treasure.
        elif room_count % 10 == 0:
            room = d.rooms[4]
            last_room = room
        # Else room is random but rooms cannot repeat.
        else:
            while True:
                room = random.choice(d.rooms[0:4])
                if room == last_room:
                    continue
                else:
                    last_room = room
                    break

        # Call appropriate room function based on room type.
        print("======")
        print("Room", str(room_count))
        print("======\n")
        room_intro = random.choice(d.room_descriptions)
        text = f.wrap_text(room_intro)
        for line in text:
            print(line)
        print("")
        m.getch()
        f.room_check(room_intro, room_tracker)
        room_tracker.append(room_intro)
        if room == "Fight":
            death_check = f.combat(character, False, False)
            if death_check == True:
                print("You are dead.  The lair claims another victim.")
                print("Better luck next time!")
                choice = input("Enter (1) to play again or (2) to exit.")
                if choice == "1":
                    intro()
                else:
                    print("Thanks for playing!")
                    quit()
            print("Press any key to move on.\n")
            m.getch()
        elif room == "Event":
            death_check = f.event(character)
            if death_check == True:
                print("You are dead.  The lair claims another victim.")
                print("Better luck next time!")
                choice = input("Enter (1) to play again or (2) to exit.")
                if choice == "1":
                    intro()
                else:
                    print("Thanks for playing!")
                    quit()
            print("Press any key to move on.\n")
            m.getch()
        elif room == "Camp":
            f.camp(character)
            print("Press any key to move on.\n")
            m.getch()
        elif room == "Trade":
            trade_count += 1
            f.trade(character, trade_count)
            print("Press any key to move on.\n")
            m.getch()
        elif room == "Treasure":
            f.treasure(character)
            print("Press any key to move on.\n")
            m.getch()

    # Final boss.
    print("==========")
    print("FINAL BOSS")
    print("==========\n")
    for text in d.boss_text:
        text = f.wrap_text(text)
        for line in text:
            print(line)
        print("")
        m.getch()
    incantation_check = f.check_incantation()
    print("      .*.*.*.                            ")
    print("    (`       `)               _.-=-.     ")
    print("     '.  / .-;             .-`  -'  '.   ")
    print("    .-'`.o )  \           /  .-_.--'  `\ ")
    print("   `;-  ) \    ;         /  / ;' _-_.-' `")
    print("     `;*`  ;    \        ; .  .'   _-' \ ")
    print("      (    )    |        |  / .-.-'    -`")
    print("       '-.-'     \       | .' ` '.-'-\`  ")
    print("        /_./\_.|\_\      ;  ' .'-'.-.    ")
    print("        /         '-._    \` /  _;-,     ")
    print("       |         .-=-.;-._ \  -'-,       ")
    print("       \        /      `*;`-`,-*`)       ")
    print("        \       \     '-- `\.\           ")
    print("         '.      '._ '-- '--'/           ")
    print("           `-._     `'----'`;            ")
    print("               `***--.____,/             ")
    print("                      \   \              ")
    print("                      // /`              ")
    print("                  ___// /__              ")
    print("                (`(`(---*-`)             \n")
    m.getch()
    death_check = f.combat(character, True, incantation_check)
    if death_check == True:
        print("You are dead. Björn's Lair claims another victim...")
        print("Better luck next time!")
        choice = input("Enter (1) to play again or (2) to exit.")
        if choice == "1":
            intro()
        else:
            print("Thanks for playing!")
            quit()

    # Outro text.
    m.getch()
    text = f.wrap_text(d.outro_text)
    for line in text:
        print(line)
    m.getch()
    print("\nYou have escaped Björn's Lair.  Congratulations!")
    m.getch()
    print("Here's your character.  Look how far you've come!")
    character.sheet()
    m.getch()
    choice = input("Enter (1) to play again or any key to exit. ")
    if choice == "1":
        intro()
    else:
        print("Thanks for playing!  See you next time!`")
        quit()

def intro():
    """Function to introduce the player to the game and create the Player object.
    
    Instantiates the Player object with "placeholder" attributes.
    Resets all global variables.
    Introduces the player to the game rules. 
    Allows the player to name their character and select their archetype - populates the Player object's attributes with the chosen values.

    """
    # Create 'empty' character in global scope.
    character = c.Player("Anonymous", "No Archetype")
    character.level = 1

    # Reset global variables for replay.
    global room_count
    global trade_count
    global last_room
    global room_tracker
    room_count = 0
    trade_count = 0
    last_room = ""
    room_tracker = []
    f.trinket_upgraded = False
    f.before = False
    f.knows_incantation = False

    
    # Intro text.
    print("=================================================================================")
    print(" ___________  __    __    _______      ___            __        __      _______  ")  
    print("(*     _   *)/* |  | *\  /*     *|    |*  |          /**\      |* \    /* __   \ ")
    print(" )__/   \__/(:  (__)  :)(: ______)    ||  |         /    \     ||  |  |: /  \   |")
    print("    | _ /    |/      \|  \/    |      |:  |        /' /\  \    |:  |  |  \__/ __)")
    print("    |.  |    |/  __  \|  // ___)_     |   |___    //  __'  \   |.  |  |   _   \  ") 
    print("    \:  |   (:  (  )  :)(:      *|    |   |:  \  /   /  \   \  /\  |\ |: | \   \ ") 
    print("     \__|    \__|  |__/  \_______)     \_______)(___/    \___)(__\_|_)|__|  \___)") 
    print("=================================================================================\n")
    print("""Welcome to THE LAIR.
    This is an RPG where you navigate a hero through a dungeon.
    Each room you enter will present you with a challenge.
    Defeat monsters, accumulate loot, and try your best to survive.
    If you make it far enough, you will encounter the FINAL BOSS.
    Defeat it to exit the dungeon victorious.\n""")
    print("Press any key to continue. \n")
    m.getch()

    # Set player name.
    while True:
        name = input("Now, give your character a name: ")
        if len(name) == 0:
            print("You must enter a name.")
            continue
        else:
            print("Thanks,", name + "!\n")
            break

    # Explain Stats
    print("""In this game, you have four primary stats:
    Staunch: Bonus weapon damage, armor, and HP.
    Swift: Bonus crit and dodge chance.
    Shrewd: Bonus magic damage and magic resistance.
    Suave: Bonus coin, better treasure, and shop discounts.\n""")
    m.getch()

    # Set player archetype.
    print("""Your archetype defines what sort of person you are and assigns your initial stats:
    1. Paladin: You take the lead and show no fear.  +Staunch and +Suave, -Shrewd.
    2. Warrior: You punch first and ask questions later.  +Staunch and +Swift, -Suave.
    3. Cleric: You value strength of arm and mind in equal measure.  +Staunch and +Shrewd, -Swift
    4. Monk: You are fleet of foot and highly disciplined.  +Swift and +Shrewd, -Suave
    5. Rogue: You lurk in the shadows, ready to strike. +Swift and +Suave, -Staunch
    6. Wizard: You value your intellect above all else.  +Shrewd and +Suave, -Swift\n""")

    while True:
        type = input("Choose an archetype by entering its corresponding number to continue. ")

        # Populate character name and type based on inputs.
        character.name = name
        if type == "1":
            character.type = "Paladin"
            character.stat_change("staunch", "up", 2)
            character.stat_change("suave", "up", 2)
            character.stat_change("shrewd", "down", 2)
            break
        elif type == "2":
            character.type = "Warrior"
            character.stat_change("staunch", "up", 2)
            character.stat_change("swift", "up", 2)
            character.stat_change("suave", "down", 2)
            break
        elif type == "3":
            character.type = "Cleric"
            character.stat_change("staunch", "up", 2)
            character.stat_change("shrewd", "up", 2)
            character.stat_change("swift", "down", 2)
            break
        elif type == "4":
            character.type = "Monk"
            character.stat_change("swift", "up", 2)
            character.stat_change("shrewd", "up", 2)
            character.stat_change("suave", "down", 2)
            break
        elif type == "5":
            character.type = "Rogue"
            character.stat_change("suave", "up", 2)
            character.stat_change("swift", "up", 2)
            character.stat_change("staunch", "down", 2)
            break
        elif type == "6":
            character.type = "Wizard"
            character.stat_change("suave", "up", 2)
            character.stat_change("shrewd", "up", 2)
            character.stat_change("staunch", "down", 2)
            break
        else:
            print("You must choose a valid number.")
            continue

    # Show character sheet.
    character.sheet_intro()
    print("Press any key to continue. \n")
    m.getch()

    print("FYI: Whenever you are presented with a choice, you can enter MENU to see the game menu.")

    # Send player into the story.
    print("It's time to get going.  Good luck!")
    print("Press any key to ENTER THE LAIR. \n")
    m.getch()
    play(character)

intro()