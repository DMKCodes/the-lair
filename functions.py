import random
import math
import msvcrt as m
import textwrap as tw
import dictionaries as d
import classes as c
import object_lists as l

# Trinket event variable.
# False until trinket is upgraded, then True.
# Prevents trinket from being upgraded more than once.
trinket_upgraded = False

# Sequential event variable and function.
# Affects the madman event, allowing the player to learn the incantation to weaken the Final Boss.
# Prevents the player from encountering the madman event multiple times.
before = False
knows_incantation = False

# Utility functions.
def check_incantation() -> bool:
    """Function to check if the player knows the incantation when encountering the final boss.
    
    If player knows incantation, test their memory by asking them to choose the correct incantation from a multiple choice list. 
    If player's choice is correct, triggers the weakening of the Boss Enemy object, reducing its stats on initialization.
    
    Returns
    -------
    bool:
        Returns True if the incantation is known and successfully spoken, False otherwise.
    
    """
    global knows_incantation
    if knows_incantation == True:
        for text in d.boss_text_incantation:
            text = wrap_text(text)
            for line in text:
                print(line)
            m.getch()
        for text in d.boss_text_incantations_opts:
            print(text)
        while True:
            choice = input("Choose an incantation by entering the corresponding number.")
            if choice == "1" or choice == "3":
                print("You shout the words, but they have no effect.  Oh well.")
                return False
            elif choice == "2":
                print("You shout the words, and Björn skids to a halt with an anguished 'SQUAWK'.")
                print("'HOW?!  HOW DO YOU KNOW MY TRUE NAME?'")
                m.getch()
                print("The rooster shrinks.  It still towers over you, but you can tell its might has diminished.")
                m.getch()
                return True
            else:
                print("You must input a valid option.")
    else:
        return False

def wrap_text(text: str) -> str:
    """Function to wrap text to 100-character width.
    
    Used to format long sections of text for easier parsing by the user.
    

    Parameters
    ----------
    text:
        The string of text to be wrapped.

    Returns
    -------
    list:
        The wrapped text as a list of strings, which can be iterated over to print as formatted lines.
    
    """
    text = tw.wrap(text, width = 100)
    return text

def room_check(room_intro: str, room_tracker: list):
    """Function to prevent repeat room descriptions during the game.
    
    After each room is successfully traversed, its description is stored in the room_tracker list.
    When a new room is randomly chosen, its description is compared against the list.
    If the description of the new room already exists in the list, prints a line of text acknowledging that the player has already visited that room earlier in the game.

    Parameters
    ----------
    room_intro:
        A string of text describing the room the player is entering.
    room_tracker:
        A list of room intros (strings) the player has already encountered.
    
    """
    seen_before = False
    for i in room_tracker:
        if i == room_intro:
            seen_before = True
    if seen_before == True:
        print("You've been here before...\n")

def is_num(str: str) -> bool:
    """Function to check if a string contains uppercase or lowercase letters.

    Parameters
    ----------
    str: 
        A string of text taken as an input from the user.
    
    Returns
    -------
    bool:
        True if str contains uppercase or lowercase letters, False otherwise.
    
    """
    check = str.isupper() or str.islower()
    return check

def is_len(str: str, character: object) -> bool:
    """Function to check a player input against the length of the Player object's ability list.
    
    If the player input (a number converted to an integer for the purpose of the check) exceeds the length of the Player object's ability list, return True, otherwise return False.
    Used to validate inputs to prevent errors.

    Parameters
    ----------
    str: 
        A string of text taken as an input from the user.
    character:
        The Player object.

    Returns
    -------
    bool:
        True if int(str) is larger than the Player object's ability list, False otherwise.
    
    """
    if int(str) > len(character.abilities):
        return True
    else:
        return False

# Game menu function.
def game_menu(character: object):
    """Function to display a Game Menu.
    
    Calls methods of the Player object according to player inputs.
    Allows player to return to the game at the same point where they accessed the menu.
    Allows player to quit the game (progress is not saved).

    Parameters
    ----------
    character: 
        The Player object.

    """
    while True:
        print("(1) Show Character Sheet")
        print("(2) Show Abilities")
        print("(3) Show Gear")
        print("(4) Show Inventory")
        print("(5) Return To Game")
        print("(6) Quit (Your progress will not be saved.)")

        choice = input("Choose an option by entering the corresponding number. ")
        if choice == "1":
            character.sheet()
            continue
        elif choice == "2":
            character.display_abilities()
            continue
        elif choice == "3":
            character.display_gear()
            continue
        elif choice == "4":
            character.display_inventory(True)
            continue
        elif choice == "5":
            print("")
            break
        elif choice == "6" or choice == "quit":
            print("Thanks for playing!")
            m.getch()
            quit()
        else:
            print("You must enter a valid option.")
            continue

# Populate starting items and abilities.
def starter_gear(character: object):
    """Function to create starter gear for the Player object.
    
    Starter gear is always the same. 
    *Suggested Change: Different starter gear based on Player archetype.*
    Creates Item objects and appends them to the appropriate gear slots within the Player object.

    Parameters
    ----------
    character:
        The Player object.
    
    """
    weapon = make_equipment(1)
    weapon.name = "Rusty Dagger"
    weapon.inspect = "A basic dagger, taken from a fallen adventurer who no longer needs it.  Hopefully it serves you better than its former master..."
    weapon.slot = "Weapon"
    weapon.buy = 0
    weapon.sell = 5
    weapon.max_dmg = 5
    weapon.armor = None
    weapon.stats = {
        "Staunch": 0,
        "Swift": 0,
        "Shrewd": 0,
        "Suave": 0
    }
    character.weapon.append(weapon)

    armor = make_equipment(1)
    armor.name = "Timeworn Leathers"
    armor.inspect = "An old, beat up set of leather armor.  They will have to do."
    armor.slot = "Armor"
    armor.buy = 0
    armor.sell = 5
    armor.max_dmg = None
    armor.armor = 1
    armor.stats = {
        "Staunch": 0,
        "Swift": 0,
        "Shrewd": 0,
        "Suave": 0
    }
    character.armor.append(armor)

    bauble = make_equipment(1)
    bauble.name = "Glimmering Trinket"
    bauble.inspect = "A glass orb, no bigger than a marble.  If you look closely, you can see a mysterious, milky substance swirling around inside.  Its usefulness is unknown... for now."
    bauble.slot = "Bauble"
    bauble.buy = 0
    bauble.sell = 0
    bauble.max_dmg = None
    bauble.armor = None
    bauble.stats = {
        "Staunch": 0,
        "Swift": 0,
        "Shrewd": 0,
        "Suave": 0
    }
    character.bauble.append(bauble)

def starter_abilities(character: object):
    """Function to create starter abilities for the Player object.
    
    Starter abilities are always the same. 
    *Suggested Change: Different starter abilities based on Player archetype.*
    Creates Ability objects and appends them to the abilities list within the Player object.

    Parameters
    ----------
    character:
        The Player object.
    
    """
    attack = c.Ability(1)
    attack.name = "Attack"
    attack.text = "You attack with your"
    attack.subtype = "Damage"
    character.abilities.append(attack)

    block = c.Ability(2)
    block.name = "Block"
    block.text = "You assume a defensive stance."
    block.subtype = "Block"
    character.abilities.append(block)

def boss_abilities(enemy: object, incantation_check: bool):
    """Function to create starter abililies for the Final Boss object.
    
    Abilities are always the same - attack and block.
    Creates Ability objects and appends them to the ability list within the Boss object.

    Parameters
    ----------
    enemy:
        The Boss object.
    incantation_check:
        Return from the check_incantation function.  True if the incantation is known and successfully spoken, False otherwise.  Boss Abilities are adjusted accordingly.
    
    """
    attack = c.Ability(1)
    attack.name = "Attack"
    attack.text = [
        "Björn pecks at you with its enormous beak,",
        "Björn buffets you with its powerful wings,",
        "Björn rakes at you with its savage claws,"
    ],
    if incantation_check == True:
        attack.value = 15
    elif incantation_check == False:
        attack.value = 20
    attack.movetype = 1
    enemy.abilities.append(attack)

    block = c.Ability(2)
    block.name = "Block"
    block.text = "Björn retreats from the fury of your onslaught, raising its wings defensively."
    if incantation_check == True:
        block.value = 10
    elif incantation_check == False:
        block.value = 15
    block.movetype = 2
    enemy.abilities.append(block)

def enemy_starter_abilities(enemy: object):
    """Function to create starter abilities for the Enemy objects.
    
    Starter abilities are always the same. 
    Creates Ability objects and appends them to the abilities list within the Enemy object.

    Parameters
    ----------
    enemy:
        The Enemy object.
    
    """
    attack = c.Ability(1)
    attack.name = "Attack"
    attack.text = "The {} attacks with its weapon,".format(enemy.name)
    attack.value = (enemy.level * 2) + 1
    attack.movetype = 1
    enemy.abilities.append(attack)

    block = c.Ability(2)
    block.name = "Block"
    block.text = "The {} attempts to defend itself.".format(enemy.name)
    block.value = enemy.level + 2
    block.movetype = 2
    enemy.abilities.append(block)

# Create object functions.
def make_equipment(num: int) -> object:
    """Function to generate random Item objects.
    
    Called when the player discovers loot or to populate shops.
    Creates equippable Item objects - weapons, armor, baubles.
    Randomizes the Item objects' attributes using the randomize method.
    
    Parameters
    ----------
    num:
        An integer that dictates the "power level" of the Item.
        *Usually the value stored in the Player or Enemy object's level attribute.
    
    Returns
    -------
    object:
        The finished Item object.
        
    """
    item = c.Item(True, False)
    item.randomize(num)
    return item

def make_consumable() -> bool:
    """Function to generate random Item objects.
    
    Called when the player discovers loot or to populate shops.
    Creates consumable Item objects - potions.
    Randomizes the Item objects' attributes using the randomize method.

    Returns
    -------
    object:
        The finished Item object.
        
    """
    item = c.Item(False, True)
    item.randomize(0)
    return item

def make_spells(unit: object, num: int):
    """Function to generate random Ability objects.
    
    Called when the player reaches certain level thresholds.
    Also called whenever an Enemy object is generate.
    Creates random Abilities (spells) - if the unit parameter is an Enemy object, appends the spell(s) to the Enemy object's abilities list - if the unit parameter is a Player object, allows the user to choose an ability and then appends the chosen ability to the Player object's abilities list.
    
    Parameters
    ----------
    unit:
        A Player or Enemy object.
    num:
        An integer that dictates the number of Abilities to create.
        Always 1 if unit is an Enemy object, or 3 if the unit is a Player object.
        
    """
    spell_list = []
    x = 0
    while x < num:
        x += 1
        # Make spell object.
        spell = c.Ability(3)

        # Choose random spell and populate attributes.
        subtype = random.randint(1, 3)
        if subtype <= 2:
            spell_text = random.choice(l.damage_spells)
            spell.name = spell_text["name"]
            spell.subtype = "Damage Spell"
            if unit.player == True:
                spell.text = spell_text["text"]
            else:
                spell.text = spell_text["text_enemy"]
        else:
            spell_text = random.choice(l.healing_spells)
            spell.name = spell_text["name"]
            spell.subtype = "Healing Spell"
            if unit.player == True:
                spell.text = spell_text["text"]
            else:
                spell.text = spell_text["text_enemy"]

        overtime = random.randint(1, 2)
        if overtime == 1:
            spell.overtime = True
            duration = random.randint(2, 4)
            spell.duration = duration
            spell.overtime_text = spell_text["overtime_text"]
            spell.overtime_text_enemy = spell_text["overtime_text_enemy"]

        cooldown = random.randint(1, 3)
        spell.cooldown = cooldown

        if unit.player == True:
            value = random.randint(3, 6)
        else:
            value = random.randint(2, 5)
        multiplier = (unit.level + 1)
        spell.value = (value * multiplier)

        if unit.player == True:
            manacost = random.randint(3, 6)
            spell.manacost = manacost * (multiplier - 1)

        # Add spell to list or to enemy abilities.
        if unit.player == True:
            spell_list.append(spell)
        else:
            unit.abilities.append(spell)

    # Display spells and let player choose spell.
    if unit.player == True:
        x = 0
        for i in spell_list:
            x += 1
            print("(" + str(x) + ")")
            print(i.name)
            print(i.subtype)
            print("Mana Cost:", i.manacost)
            if i.cooldown == 1:
                print("Cooldown:", i.cooldown, "turn")
            elif i.cooldown > 1:
                print("Cooldown:", i.cooldown, "turns")
            if i.subtype == "Damage Spell":
                if i.overtime == True:
                    print("Deals", str(i.value), "damage over",
                          str(i.duration), "turns (plus Shrewd bonus).")
                else:
                    print("Deals", str(i.value), "damage.")
            elif i.subtype == "Healing Spell":
                if i.overtime == True:
                    print("Restores", str(i.value), "health over",
                          str(i.duration), "turns. (plus Shrewd bonus)")
                else:
                    print("Restores", str(i.value), "health.")
        while True:
            choice = input(
                "Choose a spell by entering its corresponding number, or enter (4) to Skip. ")
            if choice == "1":
                unit.abilities.append(spell_list[0])
                print("You learned", spell_list[0].name + "!\n")
                break
            elif choice == "2":
                unit.abilities.append(spell_list[1])
                print("You learned", spell_list[1].name + "!\n")
                break
            elif choice == "3":
                unit.abilities.append(spell_list[2])
                print("You learned", spell_list[2].name + "!\n")
                break
            elif choice == "4":
                print("None of the options seem appealing...")
                break
            elif choice == "menu" or choice == "MENU":
                game_menu(unit)
                break
            else:
                print("You must enter a valid number.")

# Display functions.
def display_shop_item(character: object, loot: object):
    """Function to display Item objects in a shop.
    
    Called whenever the player browses a shop to display its wares.
    Properly applies the Suave discount to the purchase price (buy attribute) of the Item object.
    
    Parameters
    ----------
    character:
        The Player object.
    loot:
        An Item object.
        
    """
    print("===")
    print(loot.name)
    print(loot.slot)
    print(loot.inspect)
    if loot.slot != "Consumable":
        if loot.slot == "Weapon":
            print("Base Damage:", loot.max_dmg)
        elif loot.slot == "Armor":
            print("Armor Value:", loot.armor)
        print("Staunch: +" + str(loot.stats["Staunch"]), "|", "Swift: +" + str(loot.stats["Swift"]), "|", "Shrewd: +" + str(loot.stats["Shrewd"]), "|", "Suave: +" + str(loot.stats["Suave"]))

    # Suave discount.
    suave_check = (character.suave - 10) * 2
    suave_multiplier = 100 - suave_check
    cost = math.ceil((loot.buy * suave_multiplier) / 100)
    print("COST:", str(cost), "\n")

# Combat rewards function.
def rewards(character: object):
    """Function to randomly generate and allocate rewards for the player after they have defeated an enemy in combat.
    
    Grants an amount of XP (experience) based on the player's current level.
    Checks if the XP granted triggers a level up by calling the appropriate Player object method.
    If a level up is triggered and new level is evenly divisible by 3, calls the make_spells function and allows the player to learn a new spell.
    
    Grants a random amount of Coin, plus bonus Coin based on the Player object's Suave stat.
    
    Generates a random Item object (loot).
    Allows the player to choose to keep the loot (appends it to Player object's inventory list), equip the loot (calls the equip_item method of the Player object), or discard the loot (continues with no additional operation).

    Parameters
    ----------
    character:
        The Player object.
    
    """
    # Gain XP and check for level up.
    xp = character.level * 10
    print("\nYou gained", str(xp), "XP. \n")
    level_up = character.xp_gain(xp)
    if level_up == True and character.level % 3 == 0:
        print("\nYou have new spells available!  Press any key to see them.\n")
        m.getch()
        make_spells(character, 3)

    print("After catching your breath, you search the room for anything useful. \n")
    print("Press any key to continue. \n")
    m.getch()

    # Give Coin.
    coin = random.randint(10, 20) + character.suave
    character.coin_gain(coin)
    print("You find", str(coin), "Coin.  You now have",
            str(character.coin), "Coin. \n")

    # Generate random item and display it.
    ec = random.randint(1, 2)
    loot = ""
    if ec == 1:
        loot = make_equipment(character.level)
    else:
        loot = make_consumable()

    print("You find a", loot.name + ".\n")
    character.display_item(loot)
    while True:
        # Add loot to inventory or discard it.
        if loot.can_equip == True:
            choice = input("Enter (1) to keep, (2) to equip, or (3) to discard. ")
            print("")
            if choice == "1":
                character.inventory.append(loot)
                print("You add the", loot.name, "to your inventory.\n")
                character.display_inventory(False)
                break
            elif choice == "2":
                character.equip_gear(loot)
                break
            elif choice == "3":
                print("You leave the", loot.name, "behind.\n")
                break
            elif choice == "menu" or choice == "MENU":
                game_menu(character)
            else:
                print("You must input a valid option.")
        elif loot.can_consume == True:
            choice = input("Enter (1) to keep or (2) to discard. ")
            if choice == "1":
                character.inventory.append(loot)
                character.abilities.append(loot)
                print("You add the", loot.name, "to your inventory.")
                character.display_inventory(False)
                break
            elif choice == "2":
                print("You leave the", loot.name, "behind.")
                break
            elif choice == "menu" or choice == "MENU":
                game_menu(character)
            else:
                print("You must input a valid option.")

# Room functions.
# Player object is passed through pseudo-randomly selected Rooms until they reach the Final Boss.
def combat(character: object, boss: bool, incantation_check: bool) -> bool:
    """Function to pass the Player object through the Combat event.
    
    Each combat: 
    1. Generates an Enemy object of appropriate difficulty and randomly populates its attributes.

    Each loop:
    2. Checks if Player object or Enemy object's hp attribute is <= 0 - if so, triggers the appropriate combat resolution. 
    3. Checks if player crits (deals double damage) or dodges (avoids damage).
    4. Chooses a random Enemy Ability.
    5. Allows the player to choose an Ability from their Ability list and validates it.
    6. Calculates combat math based on Player Ability.
    7. Calculates combat math based on Enemy Ability.
    8. Prints combat outcome as a string of text, concatenating all necessary values.
    9. Checks if player has a companion and updates combat outcome accordingly.
    10. Adjusts the Player and Enemy objects' health totals.
    11. Checks for and updates damage-over-time (DOT) and healing-over-time (HOT) effects.
    12. Prints HP and mana totals for player and enemy.
    13. When consumables are used, clears them from Player inventory and Abilities lists.

    Parameters
    ----------
    character:
        The Player object.
    boss:
        True if the player has reached the Final Boss combat, False otherwise.
    incantation_check:
        Return from the check_incantation function.  True if the incantation is known and successfully spoken, False otherwise.  Boss Abilities are adjusted accordingly.
    
    Returns
    -------
    bool:
        True if the player survives the combat, False otherwise.

    """
    # 1. Generate and populate random enemy of character's level (or boss if final floor).
    if boss == False:
        enemy = c.Enemy(character.level)
        enemy.populate()
        enemy_starter_abilities(enemy)
        make_spells(enemy, 1)
        print(enemy.greet)
        print("Press any key to initiate combat.")
        m.getch()
    elif boss == True:
        if incantation_check == True:
            enemy = c.Boss(True)
            boss_abilities(enemy, incantation_check)
            make_spells(enemy, 3)
            print("Press any key to initiate combat.")
            m.getch()
        else:
            enemy = c.Boss(False)
            boss_abilities(enemy, incantation_check)
            make_spells(enemy, 2)
            print("Press any key to initiate combat.")
            m.getch()

    # Combat loop.
    # Non-resetting variables - damage/heal over time checks/counters.
    dot = False
    hot = False
    enemy_dot = False
    enemy_hot = False
    dot_damage = 0
    enemy_dot_damage = 0
    hot_heal = 0
    enemy_hot_heal = 0
    dot_counter = 0
    hot_counter = 0
    enemy_dot_counter = 0
    enemy_hot_counter = 0
    dot_text = ""
    hot_text = ""
    enemy_dot_text = ""
    enemy_hot_text = ""
    # Non-resetting variables - stat potions.
    staunch_pot = False
    swift_pot = False
    shrewd_pot = False
    staunch_pot_value = 0
    swift_pot_value = 0
    shrewd_pot_value = 0

    while True:
        # Resetting variables.
        damage = 0
        enemy_damage = 0
        enemy_damage_type = ""
        block = 0
        enemy_block = 0
        heal = 0
        enemy_heal = 0
        resist = math.floor(character.shrewd / 5)
        base_damage = character.weapon[0].max_dmg
        armor = character.armor[0].armor
        staunch = math.floor(character.staunch / 5)
        shrewd = math.floor(character.shrewd / 5)
        attack = False
        enemy_attack = False
        blocked = False
        enemy_blocked = False
        spell = False
        enemy_spell = False
        consumable = False
        dodge = False
        crit = False

        # 2. Check for death of enemy or player.
        if character.hp <= 0:
            return True
        elif enemy.hp <= 0:
            speech = enemy.death
            text = wrap_text(speech)
            for line in text:
                print(line)
            print("")
            m.getch()
            # Clear stat potions.
            if boss == False:
                if staunch_pot == True:
                    staunch_pot = False
                    character.staunch -= staunch_pot_value
                    print("Your Staunch Potion wears off.")
                elif swift_pot == True:
                    swift_pot = False
                    character.swift -= swift_pot_value
                    print("Your Swift Potion wears off.")
                elif shrewd_pot == True:
                    shrewd_pot = False
                    character.shrewd -= shrewd_pot_value
                    print("Your Shrewd Pot wears off.")
                # Reset cooldowns.
                for ability in character.abilities:
                    ability.cooldown_count = 0
                # Give combat rewards.
                print("You are victorious! Press any key to see your rewards. \n")
                m.getch()
                print("===========================================")
                rewards(character)
            return False

        # 3. Check dodge and crit.
        dodge_check = random.randint(1, 100)
        if dodge_check <= character.swift:
            dodge = True
        crit_check = random.randint(1, 100)
        if crit_check <= character.swift:
            crit = True

        # 4. Choose random enemy ability.
        enemy_ability = random.choice(enemy.abilities)

        # 5. Display abilities and verify player choice.  
        abilities = character.display_abilities_combat()
        while True:
            choice = input("Choose an ability by entering its corresponding number: ")
            print("")
            check = is_num(choice)
            if check == False and choice != "":
                choice = int(choice) - 1
                if choice >= len(abilities):
                    print("You must enter a valid number.")
                else:
                    ability = abilities[choice]
                    break
            elif choice == "menu" or choice == "MENU":
                game_menu(character)
            else:
                print("You must enter a valid input.")

        # 6. Do player math.
        if ability.movetype == 1:
            attack = True
            damage = random.randint(1, base_damage) + staunch
        elif ability.movetype == 2:
            blocked = True
            staunch = math.ceil(character.staunch / 5)
            block = armor + staunch
        elif ability.movetype == 3:
            if ability.manacost > character.mana:
                print("You don't have enough mana for that.")
            else:
                spell = True
                value = ability.value
                if ability.subtype == "Damage Spell":
                    if ability.overtime == False:
                        damage = value + shrewd
                    elif ability.overtime == True:
                        duration = ability.duration
                        enemy_dot = True
                        enemy_dot_damage = math.ceil(
                            (value + shrewd) / duration)
                        enemy_dot_counter = duration
                        enemy_dot_text = ability.overtime_text_enemy
                elif ability.subtype == "Healing Spell":
                    if ability.overtime == False:
                        heal = value + shrewd
                    elif ability.overtime == True:
                        duration = ability.duration
                        hot = True
                        hot_heal = math.ceil((value + shrewd) / duration)
                        hot_counter = duration
                        hot_text = ability.overtime_text
        elif ability.movetype == 4:
            consumable = True
            if ability.effect == 1:
                character.hp += character.level * 10
            elif ability.effect == 2:
                character.mana += character.level * 10
            elif ability.effect == 3:
                staunch_pot = True
                staunch_pot_value = ability.value
                character.staunch += ability.value
            elif ability.effect == 4:
                swift_pot = True
                swift_pot_value = ability.value
                character.swift += ability.value
            elif ability.effect == 5:
                shrewd_pot = True
                shrewd_pot_value = ability.value
                character.shrewd += ability.value

        # 7. Do enemy math.
        if enemy_ability.movetype == 1:
            enemy_attack = True
            base_damage = enemy_ability.value
            enemy_damage = random.randint(1, base_damage)
        elif enemy_ability.movetype == 2:
            enemy_blocked = True
            base_block = enemy_ability.value
            enemy_block = random.randint(1, base_block)
        elif enemy_ability.movetype == 3:
            enemy_spell = True
            value = enemy_ability.value
            if enemy_ability.subtype == "Damage Spell":
                if enemy_ability.overtime == False:
                    enemy_damage_type = "Magic"
                    enemy_damage = value
                elif enemy_ability.overtime == True:
                    duration = enemy_ability.duration
                    dot = True
                    dot_damage = math.ceil((value) / duration)
                    dot_counter = duration
                    dot_text = enemy_ability.overtime_text
            elif enemy_ability.subtype == "Healing Spell":
                if enemy_ability.overtime == False:
                    enemy_heal = value + shrewd
                elif enemy_ability.overtime == True:
                    duration = enemy_ability.duration
                    enemy_hot = True
                    enemy_hot_heal = math.ceil((value + shrewd) / duration)
                    enemy_hot_counter = duration
                    enemy_hot_text = enemy_ability.overtime_text_enemy

        # Crit multiplier.
        if crit == True:
            damage = damage * 2
        
        # Choose combat text - for boss fight ONLY.
        if boss == True and enemy_attack == True:
            enemy_ability.text = random.choice(enemy.abilities[0].text)

        # 8. Print outcomes.
        if attack == True:
            if crit == True:
                print("It's a critical hit!")
            if enemy_attack == True:
                print(ability.text, character.weapon[0].name + ", dealing", str(damage), "damage.")
                if dodge == True:
                    print(enemy_ability.text + " but you narrowly dodge!")
                elif dodge == False:
                    if enemy_damage > armor:
                        print(enemy_ability.text, "dealing", str(enemy_damage),"damage.  Your armor absorbs", str(armor), "of it.")
                    else:
                        print(enemy_ability.text, "dealing", str(enemy_damage), "damage.  Your armor absorbs all of it.")
            elif enemy_blocked == True:
                print(enemy_ability.text)
                if damage > enemy_block:
                    print(ability.text, character.weapon[0].name + ", dealing", str(damage), "damage.  The", enemy.name, "blocks", enemy_block, "of it.")
                else:
                    print(ability.text, character.weapon[0].name + ", dealing", str(damage), "damage.", enemy.name, "blocks all of it.")
            elif enemy_spell == True:
                print(ability.text, character.weapon[0].name + ", dealing", str(damage), "damage.")
        elif blocked == True:
            print(ability.text)
            if enemy_attack == True:
                if dodge == True:
                    print(enemy_ability.text, "but you narrowly dodge!")
                elif dodge == False:
                    if enemy_damage > block:
                        print(enemy_ability.text, "dealing", str(enemy_damage), "damage.  You block", str(block), "of it.")
                    else:
                        print(enemy_ability.text, "dealing", str(enemy_damage), "damage.  You block all of it.")
            elif enemy_blocked == True:
                print(enemy_ability.text)
        elif spell == True:
            if enemy_blocked == True:
                print(enemy_ability.text)
            if ability.subtype == "Damage Spell":
                if crit == True:
                    print("It's a critical hit!")
                if ability.overtime == False:
                    print(ability.text, "dealing", str(damage), "damage.")
                else:
                    print(ability.text, "dealing", str(enemy_dot_damage), "damage per turn for the next", enemy_dot_counter, "turns.")
            elif ability.subtype == "Healing Spell":
                if ability.overtime == False:
                    print(ability.text, "restoring", str(heal), "health.")
                else:
                    print(ability.text, "restoring", str(hot_heal), "health per turn for the next", str(hot_counter), "turns.")
            if enemy_attack == True:
                if dodge == True:
                    print(enemy_ability.text, "but you narrowly dodge!")
                elif dodge == False:
                    if enemy_damage > armor:
                        print(enemy_ability.text, "dealing", str(enemy_damage), "damage.  Your armor absorbs", str(armor), "of it.")
                    else:
                        print(enemy_ability.text, "dealing", str(enemy_damage), "damage.  Your armor absorbs all of it.")
        elif consumable == True:
            if enemy_blocked == True:
                print(enemy_ability.text)
            if ability.effect == 1:
                value = character.level * 10
                print("You drink the Health Potion, restoring", str(value), "health.")
            elif ability.effect == 2:
                value = character.level * 10
                print("You drink the Mana Potion, restoring", str(value), "mana.")
            elif ability.effect == 3:
                print("You drink the Staunch Potion, gaining", str(ability.value), "Staunch until end of combat.")
            elif ability.effect == 4:
                print("You drink the Swift Potion, gaining", str(ability.value), "Swift until end of combat.")
            elif ability.effect == 5:
                print("You drink the Shrewd Potion, gaining", str(ability.value), "Shrewd until end of combat.")
            if enemy_attack == True:
                if dodge == True:
                    print(enemy_ability.text, "but you narrowly dodge!")
                elif dodge == False:
                    if enemy_damage > armor:
                        print(enemy_ability.text, "dealing", str(enemy_damage), "damage.  Your armor absorbs", str(armor), "of it.")
                    else:
                        print(enemy_ability.text, "dealing", str(enemy_damage), "damage.  Your armor absorbs all of it.")

        if enemy_spell == True:
            if enemy_ability.subtype == "Damage Spell":
                if dodge == True:
                    print("The", enemy.name, enemy_ability.text, "but you narrowly dodge!")
                else:
                    if enemy_ability.overtime == False:
                        print("The", enemy.name, enemy_ability.text, "dealing", str(enemy_damage), "damage, but you resist", str(resist), "of it.")
                    else:
                        print("The", enemy.name, enemy_ability.text, "dealing", str(dot_damage), "per turn for the next", str(dot_counter), "turns.")
            elif enemy_ability.subtype == "Healing Spell":
                if enemy_ability.overtime == False:
                    print("The", enemy.name, enemy_ability.text, "restoring", str(enemy_heal), "health.")
                else:
                    print("The", enemy.name, enemy_ability.text, "restoring", str(enemy_hot_heal), "health per turn for the next", str(enemy_hot_counter), "turns.")

        # 9. Companion damage.
        if character.companion == True:
            companion_damage = random.randint(1, 5)
            print(character.companion_name, character.companion_text, "dealing", str(companion_damage), "damage.")
            enemy.hp -= companion_damage

        # 10. Calculate health totals.
        if enemy_blocked == True and damage > enemy_block:
            damage = damage - enemy_block
            enemy.hp -= damage
        else:
            enemy.hp -= damage

        if enemy_damage > 0:
            if blocked == True and enemy_damage_type == "Physical":
                if enemy_damage > block and dodge == False:
                    enemy_damage = enemy_damage - block
                    character.hp -= enemy_damage
            elif enemy_damage_type == "Magic":
                if dodge == False:
                    resist = math.ceil(character.shrewd / 5)
                    enemy_damage = enemy_damage - resist
                    character.hp -= enemy_damage
            else:
                if dodge == False:
                    enemy_damage -= armor
                    character.hp -= enemy_damage

        if heal > 0:
            character.hp += heal
            if character.hp > character.max_hp:
                character.hp = character.max_hp

        if enemy_heal > 0:
            enemy.hp += enemy_heal

        # 11. Check and update DOTs and HOTs.
        if enemy_dot == True:
            enemy_dot_counter -= 1
            print(enemy_dot_text, "for", str(enemy_dot_damage), "damage. ", str(enemy_dot_counter), "turns remaining.")
            if enemy_dot_counter <= 0:
                enemy_dot = False
            enemy.hp -= enemy_dot_damage
        if dot == True:
            dot_counter -= 1
            if resist < dot_damage:
                print(dot_text, "for", str(dot_damage), "damage, but you resist", str(resist), "of it. ", str(dot_counter), "turns remaining.")
                character.hp -= dot_damage - resist
            else:
                print(dot_text, "for", str(dot_damage), "damage, but you resist all of it. ", str(dot_counter), "turns remaining.")
            if dot_counter <= 0:
                dot = False
        if hot == True:
            print(hot_text, "for", str(hot_heal), "health. ", str(hot_counter), "turns remaining.")
            hot_counter -= 1
            if hot_counter <= 0:
                hot = False
            character.hp += hot_heal
            if character.hp > character.max_hp:
                character.hp = character.max_hp
        if enemy_hot == True:
            print(enemy_hot_text, "for", str(enemy_hot_heal), "health. ", str(enemy_hot_counter), "turns remaining.")
            enemy_hot_counter -= 1
            if enemy_hot_counter <= 0:
                enemy_hot = False
            enemy.hp += enemy_hot_heal
            if enemy.hp > enemy.max_hp:
                enemy.hp = enemy.max_hp

        m.getch()

        # 12. Print HP and mana totals.
        if character.hp <= 0:
            character.hp = 0
        elif character.hp > character.max_hp:
            character.hp = character.max_hp
        if character.mana > character.max_mana:
            character.mana = character.max_mana
        if enemy.hp <= 0:
            enemy.hp = 0
        if spell == True:
            character.mana -= ability.manacost
        print("\nYour HP:", str(character.hp))
        print("Your Mana:", str(character.mana), "\n")
        print(enemy.name + "'s HP:", str(enemy.hp), "\n")

    # 13. Clear consumables.
        if consumable == True:
            character.inventory.remove(ability)
            character.abilities.remove(ability)

def event(character: object) -> bool:
    """Function to pass the Player object through the Event events (did not think this one through).
    * Will be renaming this.

    Events are a Room type with many possible outcomes.  The design intention here is to add an additional layer of unpredictability to the game.  Statistically, many of these Events will not be encountered each run, but instead are unique experiences the player can look forward to.  This type of design is common in roguelike games to further reduce predictability.

    Events are also excellent storytelling vehicles to flesh out the world in which the game is set.

    1. Damaging Goo: The player is presented with a risk - reach inside the mysterious goo for a chance at treasure, or play it safe and move on.  The player's choice is verified and, if they choose to reach inside, they are rewarded with unique loot but punished by losing HP.

    2. Animal Companion: The most requested feature in a poll I ran among friends when deciding on different Event options.  The player finds and names a cute animal companion who fights alongside them in battle with unique text and abilities.  There are many different types of animals you can discover, further adding pseudo-randomness to the game.

    3. Glimmering Trinket: At the start of the game, the player is always given a piece of gear called the "Glimmering Trinket" that tantalizingly offers no benefits and hints at a mysterious purpose.  When encountering this Event, a celestial being infuses it with energy, turning it into a very powerful piece of gear.  Players are rewarded for holding onto this seemingly useless Item until they encounter this Event.

    4. Spell Event: The player discovers a knapsack full of scrolls.  They are rewarded by being able to choose from a list of randomly generated Abilities (spells) that are stronger than usual.  This enforces the "highroll vs. lowroll" nature of roguelike games, where the player's power level can vary widely from run to run based on random chance.

    5. Sequential Event: In this Event, the player encounters a madman.  If this Event is only encountered once in a run, it is merely a storytelling vehicle that offers no benefit to the player.  But on the rare occasion that it is encountered multiple times in a run, each subsequent encounter will reveal deeper information about The Lair and its mysterious inhabitants.  Encounter it enough times, and the madman will teach the player a secret incantation that allows them to weaken the Final Boss, improving their chances of escape.

    6. Elementals Event: The player is given a choice between helping one of two imprisoned elementals.  Depending on their choice, they will be awarded different benefits.  This is also fairly common roguelike design - as the player plays the game more and learns more about the different types of events, they can choose the option that most benefits them in the moment.

    *If I continue developing this game, I plan to add many more Events.

    Parameters
    ----------
    character:
        The Player object.

    Returns
    -------
    bool:
        Returns True if the Player object's HP attribute value is <= 0, False otherwise.
        *Some Events can cause the player to lose HP, so this is a basic check to see if they died during the Event.
    
    """
    this_event = random.randint(1, 6)
    # 1. Damaging Goo Event.
    if this_event == 1:
        print("A basin filled with sticky, translucent goo sits in a corner of the room.")
        print("Straining your eyes, you can see an object resting at the bottom.")
        print("Do you dare to reach inside?")
        while True:
            choice = input("Enter (1) to reach inside, or (2) to ignore it. ")
            if choice == "1":
                character.hp -= 5
                if character.hp <= 0:
                    return True
                else:
                    num = character.level + 1
                    loot = make_equipment(num)
                print("You fish out a", loot.name + ".")
                print("The goo scalds your skin, dealing 5 damage.")
                character.display_item(loot)
                while True:
                    choice_two = input(
                        "Enter (1) to keep, (2) to equip, or (3) to discard.")
                    if choice_two == "1":
                        character.inventory.append(loot)
                        print("You add the", loot.name, "to your inventory.")
                        character.display_inventory(False)
                        break
                    elif choice_two == "2":
                        character.equip_gear(loot)
                        break
                    elif choice_two == "3":
                        print("You leave the", loot.name, "behind. \n")
                        break
                    elif choice_two == "menu" or choice_two == "MENU":
                        game_menu(character)
                    else:
                        print("You must input a valid option.")
            elif choice == "2":
                print("You didn't make it this far by sticking your hands in strange places...")
                break
            elif choice == "menu" or choice == "MENU":
                game_menu(character)
                continue
            else:
                print("You must enter a valid option.")
                continue
            break
    
    # 2. Animal Companion Event.
    elif this_event == 2:
        if character.companion == False:
            check = random.randint(1, 5)
            text = check + 5
            character.companion = True
            character.companion_type = d.companions[check]
            character.companion_text = d.companions[text]
            print("Nestled in a corner of the room, you discover a small, mewling", character.companion_type + ".")
            m.getch()
            print("It must have been abandoned here.  You don't have the heart to leave it to die, so you scoop it up.")
            print("Its presence is instantly comforting to you in this dark place.\n")
            m.getch()
            print("The", character.companion_type, "eyes you warily at first.")
            print("As the moments pass in calm silence, it nestles further into your arms.")
            print("'I suppose you'll need a name,' you murmur.\n")
            while True:
                choice = input("Enter a name for your new companion: ")
                if len(choice) > 0:
                    character.companion_name = choice
                    break
                elif choice == "menu" or choice == "MENU":
                    game_menu(character)
                else:
                    print("You must choose a name.")
        else:
            coin = random.randint(5, 25)
            character.coin += coin
            print("You find", str(coin), "Coin.  You now have",
                  str(character.coin), "Coin.")
    
    # 3. Glimmering Trinket Event.
    elif this_event == 3:
        global trinket_upgraded
        print("A glowing bead of light appears in front of you.")
        print("It twists and warps outward, forming the shape of a woman.")
        print("Even without features, you can tell it is friendly. \n")
        m.getch()

        if trinket_upgraded == False:
            for i in character.bauble:
                if i.name == "Glimmering Trinket":
                    i.inspect = "A glass orb, no bigger than a marble. You now understand its importance."
                    i.stats["Staunch"] += 4
                    i.stats["Swift"] += 4
                    i.stats["Shrewd"] += 4
                    i.stats["Suave"] += 4
                    loot = i
            for j in character.inventory:
                if j.name == "Glimmering Trinket":
                    i.inspect = "A glass orb, no bigger than a marble. You now understand its importance."
                    j.stats["Staunch"] += 4
                    j.stats["Swift"] += 4
                    j.stats["Shrewd"] += 4
                    j.stats["Suave"] += 4
                    loot = j

        if trinket_upgraded == False:
            if character.type == "Paladin":
                speech = "'Ah, so you are {} the Paladin,' the figure says, its voice mellifluous and ethereal.  'There is much talk of you in the realm above.  Many pass through this accursed place, but few who possess your courage.  There may be hope for you yet.  I cannot remain on this physical plane to aid you, but I beg - take this gift, that it might see you through this trial.' \n".format(character.name)
                text = wrap_text(speech)
                for line in text:
                    print(line)
                print("")
                m.getch()
            elif character.type == "Warrior":
                speech = "'Ah, so you are {} the Warrior,' the figure says, its voice mellifluous and ethereal.  'There is much talk of you in the realm above.  Many pass through this accursed place, but few who possess your ferocity.  There may be hope for you yet.  I cannot remain on this physical plane to aid you, but I beg - take this gift, that it might see you through this trial.' \n".format(character.name)
                text = wrap_text(speech)
                for line in text:
                    print(line)
                print("")
                m.getch()
            elif character.type == "Monk":
                speech = "'Ah, so you are {} the Monk,' the figure says, its voice mellifluous and ethereal.  'There is much talk of you in the realm above.  Many pass through this accursed place, but few who possess your strength of will.  There may be hope for you yet.  I cannot remain on this physical plane to aid you, but I beg - take this gift, that it might see you through this trial.' \n".format(character.name)
                text = wrap_text(speech)
                for line in text:
                    print(line)
                print("")
                m.getch()
            elif character.type == "Rogue":
                speech = "'Ah, so you are {} the Rogue,' the figure says, its voice mellifluous and ethereal.  'There is much talk of you in the realm above.  Many pass through this accursed place, but few who possess your guile.  There may be hope for you yet.  I cannot remain on this physical plane to aid you, but I beg - take this gift, that it might see you through this trial.' \n".format(character.name)
                text = wrap_text(speech)
                for line in text:
                    print(line)
                print("")
                m.getch()
            elif character.type == "Cleric":
                speech = "'Ah, so you are {} the Cleric,' the figure says, its voice mellifluous and ethereal.  'There is much talk of you in the realm above.  Many pass through this accursed place, but few who possess your devotion.  There may be hope for you yet.  I cannot remain on this physical plane to aid you, but I beg - take this gift, that it might see you through this trial.' \n".format(character.name)
                text = wrap_text(speech)
                for line in text:
                    print(line)
                print("")
                m.getch()
            elif character.type == "Wizard":
                speech = "'Ah, so you are {} the Wizard,' the figure says, its voice mellifluous and ethereal.  'There is much talk of you in the realm above.  Many pass through this accursed place, but few who possess your intellect.  There may be hope for you yet.  I cannot remain on this physical plane to aid you, but I beg - take this gift, that it might see you through this trial.' \n".format(character.name)
                text = wrap_text(speech)
                for line in text:
                    print(line)
                print("")
                m.getch()
            m.getch()

        if trinket_upgraded == False:
            trinket_upgraded = True
            speech = "The figure raises a hand, and the Glimmering Trinket you hold appears in front of them.  It spins and hovers, glowing brighter and brighter before finally dimming.  You can sense the figure's approval.  'Good luck,' it says simply, before fading away into nothingness."
            text = wrap_text(speech)
            for line in text:
                print(line)
            print("")
            m.getch()
            print("You snatch the trinket from the air, and you can see its power has multiplied.")
            character.display_item(loot)
            for i in character.bauble:
                if i.name == "Glimmering Trinket":
                    character.stat_change("staunch", "up", 4)
                    character.stat_change("swift", "up", 4)
                    character.stat_change("shrewd", "up", 4)
                    character.stat_change("suave", "up", 4)
        elif trinket_upgraded == True:
            speech = "'Ah, we meet again,' the figure intones.  I regret that I cannot be of as much use this time.  My power only permits brief visits to this lair.  But take this small token and keep fighting.'  Then it is gone."
            text = wrap_text(speech)
            for line in text:
                print(line)
            print("")
            m.getch()
            print("You gained a stat point!")
            print("(1) Staunch, (2) Swift, (3) Shrewd, (4) Suave")
            while True:
                stat = input("Choose a stat to increase: \n").upper()
                if stat == "1" or stat == "STAUNCH":
                    stat = "staunch"
                    character.stat_change(stat, "up", 1)
                    break
                elif stat == "2" or stat == "SWIFT":
                    stat = "swift"
                    character.stat_change(stat, "up", 1)
                    break
                elif stat == "3" or stat == "SHREWD":
                    stat = "shrewd"
                    character.stat_change(stat, "up", 1)
                    break
                elif stat == "4" or stat == "SUAVE":
                    stat = "suave"
                    character.stat_change(stat, "up", 1)
                    break
                elif stat == "MENU":
                    game_menu(character)
                else:
                    print("You must choose a valid option.")
    
    # 4. Spell Event.
    elif this_event == 4:
        speech = "You discover a knapsack stuffed with scrolls.  Most of them are in surface languages you don't speak, but a few seem promising.  You read further, and discover they can teach you new spells!"
        text = wrap_text(speech)
        for line in text:
            print(line)
        print("")
        m.getch()
        make_spells(character, 3)

    # 5. Sequential Event.
    elif this_event == 5:
        global before
        global knows_incantation
        if before == False:
            before = True
            for speech in d.madman_text_one:
                text = wrap_text(speech)
                for line in text:
                    print(line)
                print("")
                m.getch()
        elif before == True:
            before == "skip"
            knows_incantation == True
            for speech in d.madman_text_two:
                text = wrap_text(speech)
                for line in text:
                    print(line)
                print("")
                m.getch()
        elif before == "skip":
            text = d.madman_text_three
            text = wrap_text(text)
            for line in text:
                print(line)
            print("")
            m.getch()
            
    # 6. Elementals Event.
    elif this_event == 6:
        speech = "A small, orange fire burns in a brazier in one corner of the chamber.  In the opposite corner, a second brazier similarly burns, except its flames are bright blue."
        text = wrap_text(speech)
        for line in text:
            print(line)
        print("")
        m.getch()
        while True:
            choice = input(
                "Enter (1) to check the red fire, or (2) to check the blue fire. \n")
            if choice == "1":
                print("You approach cautiously.")
                print("With each step you take, the fire flares higher and wider.")
                print("You stare in awe as it sprouts limbs and takes the shape of a red fire elemental.\n")
                m.getch()
                break
            elif choice == "2":
                print("You approach cautiously.")
                print("With each step you take, the fire flares higher and wider.")
                print("You stare in awe as it sprouts limbs and takes the shape of a blue fire elemental.\n")
                m.getch()
                break
            elif choice == "menu" or choice == "MENU":
                game_menu(character)
                continue
            else:
                print("You must enter a valid option.")
                continue
        print("'Free me!'  Its voice, deep and crackling, fills the chamber.")
        print("'Free me, and be rewarded.'\n")
        m.getch()
        speech = "You scan the room and notice a ring of clay disks carved with unfamiliar runes surrounding the brazier.  Despite your better judgement, you bend down and pick up one of the disks.  The elemental cackles as it steps through the ring.  You grip your weapon tighter, tensed for combat."
        text = wrap_text(speech)
        for line in text:
            print(line)
        print("")
        m.getch()
        print("'Thank you, mortal,' the elemental rumbles.  'Now take this gift and be gone from this place.'\n")
        m.getch()
        speech = "The elemental raises its arm and a gout of flame rushes over you.  You expect to die, but instead you feel a restorative warmth suffuse your aching body.  When it passes, you open your eyes to see that the elemental has disappeared."
        text = wrap_text(speech)
        for line in text:
            print(line)
        print("")
        m.getch()
        if choice == "1":
            character.hp = character.max_hp
            print("You are restored to full health!")
        elif choice == "2":
            character.max_hp += 5
            character.hp += 5
            print("You gained 5 maximum HP!")
        m.getch()
    return False

def camp(character: object):
    """Function to pass the Player object through the Camp event.

    Allows player to choose between "Rest" or "Train":
    Rest: Restores missing HP and mana.
    Train: Awards 1 stat point and allows player to assign it to a stat of their choice.

    Parameters
    ----------
    character:
        The Player object.
    
    """
    print(d.room_intros[2])
    print("(1) Rest - Restore your missing HP and Mana.")
    print("(2) Train - Gain a stat point.")
    while True:
        choice = input(
            "Choose an option by entering the corresponding number: \n")
        if choice == "1":
            character.hp = character.max_hp
            character.mana = character.max_mana
            print("You hunker down for a short rest and awake feeling rejuvenated.")
            print("Your HP:", character.hp)
            print("Your Mana:", character.mana)
            break
        elif choice == "2":
            print("You gained a stat point!")
            print("(1) Staunch, (2) Swift, (3) Shrewd, (4) Suave")
            while True:
                stat = input("Choose a stat to increase: \n").upper()
                if stat == "1" or stat == "STAUNCH":
                    stat = "staunch"
                    character.stat_change(stat, "up", 1)
                    break
                elif stat == "2" or stat == "SWIFT":
                    stat = "swift"
                    character.stat_change(stat, "up", 1)
                    break
                elif stat == "3" or stat == "SHREWD":
                    stat = "shrewd"
                    character.stat_change(stat, "up", 1)
                    break
                elif stat == "4" or stat == "SUAVE":
                    stat = "suave"
                    character.stat_change(stat, "up", 1)
                    break
                elif stat == "MENU":
                    game_menu(character)
                    continue
                else:
                    print("You must choose a valid option.")
                    continue
            break
        elif choice == "menu" or choice == "MENU":
            game_menu(character)
        else:
            print("You must choose a valid option.")

def trade(character: object, trade_count: int):
    """A function to pass the Player object through the Trade event.
    
    1. Formats and prints appropriate intro using wrap_text function.
    2. Each shop contains 6 randomly generated Items - 4 equippable gear Items and 2 consumable Items - which are appended to a list: item_list.

    Each loop: User is prompted to choose Buy, Sell, or Leave.
    3. Buy functionality: Iterates over item_list using the display_shop_item function to display each randomly generated Item in the list.  If the player purchases an Item, their input is verified to ensure the selection is valid and checks that the Item's buy attribute value is less than the Player object's Coin attribute value.  Player can then equip the Item or store it in their inventory via the appropriate Player class methods.
    4. Sell functionality: Calls the display_inventory method of the Player class to display existing Items in the player's inventory.  If the player sells an Item, their input is verified to ensure the selection is valid.  The Player object's Coin attribute value is incremented by the Item's sell attribute value.

    The player can loop through the Buy and Sell functionalities an unlimited number of times until they choose to Leave, at which point the while loop breaks.

    Parameters
    ----------
    character:
        The Player object.
    trade_count:
        An integer count of the number of times the player has encountered the Trade event.  This is used to display the appropriate room intro, as this intro changes based on the player's previous visits.
    
    """
    # 1. Print appropriate intro.
    if trade_count == 1:
        for i in d.room_intros[3]:
            text = wrap_text(i)
            for line in text:
                print(line)
            print("")
            m.getch()
    else:
        for i in d.room_intros[4]:
            text = wrap_text(i)
            for line in text:
                print(line)
            print("")
            m.getch()

    # 2. Generate a list of 6 random items - 4 equipment, 2 consumable.
    x = 0
    item_list = []
    while x < 6:
        x += 1
        if x < 4:
            item = make_equipment(character.level)
            item_list.append(item)
        elif x == 4:
            num = character.level + 1
            item = make_equipment(num)
            item_list.append(item)
        else:
            item = make_consumable()
            item_list.append(item)

    while True:
        print("=============")
        choice = input("Do you want to (1) Buy, (2) Sell, or (3) Exit? \n")
        # 3. Buy functionality.
        if choice == "1":
            x = 1
            print("=============")
            print("Björn's Wares")
            print("=============")
            for i in item_list:
                print("(" + str(x) + ")")
                x += 1
                display_shop_item(character, i)
            print("You have", str(character.coin), "Coin.")
            shop_choice = input("Buy an item by entering its corresponding number, or enter (7) return to the shop menu. ")
            if choice == "7" or choice == "":
                continue
            elif choice == "menu" or choice == "MENU":
                game_menu(character)
            else:
                shop_check = is_num(shop_choice)
                if shop_check == False:
                    shop_choice = int(shop_choice)
                else:
                    print("You must enter a valid option.")
                    continue
                if shop_choice >= 1 and shop_choice <= 6:
                    shop_choice = shop_choice - 1
                    if item_list[shop_choice].buy <= character.coin:
                        character.coin -= item_list[shop_choice].buy
                        print("You buy the", item_list[shop_choice].name + ".  Björn clucks approvingly.")
                        ("You have", str(character.coin), "Coin remaining.")
                        new_item = item_list.pop(shop_choice)
                        if new_item.can_equip == True:
                            while True:
                                shop_choice_two = input(
                                    "Enter (1) to add the {} to your inventory, or (2) to equip it. \n".format(new_item.name))
                                if shop_choice_two == "2":
                                    character.equip_gear(new_item)
                                    break
                                elif shop_choice_two == "1":
                                    character.inventory.append(new_item)
                                    character.display_inventory(False)
                                    break
                                elif shop_choice_two == "menu" or shop_choice_two == "MENU":
                                    game_menu(character)
                                    continue
                                else:
                                    print("You must enter a valid input.")

                        elif new_item.can_consume == True:
                            character.inventory.append(new_item)
                            character.abilities.append(new_item)
                            character.display_inventory(False)
                    else:
                        print("You don't have enough Coin for that.")
                else:
                    print("You must enter a valid number.")

        # 4. Sell functionality.
        elif choice == "2":
            inv = len(character.inventory)
            leave = inv + 1
            character.display_inventory(False)
            print("You have", str(character.coin), "Coin.")
            choice = input("Sell an item by entering its corresponding number, or enter ({}) to return to the shop menu. \n".format(leave))
            check = is_num(choice)
            if check == False and choice != "":
                choice = int(choice)

            if choice == "{}".format(leave):
                continue
            elif choice == "menu" or choice == "MENU":
                game_menu(character)
            elif choice >= 1 and choice < leave:
                choice = choice - 1
                character.coin += character.inventory[choice].sell
                removed = character.inventory.pop(choice)
                for ability in character.abilities:
                    if ability == removed:
                        character.abilities.remove(ability)
                print("You sell the", removed.name + ".  Björn clucks approvingly.")
                print("You now have", str(character.coin), "Coin.")
            elif choice == leave:
                continue
            else:
                print("You must enter a valid option.")
        
        elif choice == "menu" or choice == "MENU":
            game_menu(character)
            continue

        # Leave.
        else:
            print("'So long, and good CLUCK!' rasps Björn emphatically.")
            break

def treasure(character: object):
    """Function to pass the Player object through the Treasure event.

    Grants a random amount of Coin.
    Generates a random Item object (loot) at an enhanced power level.
    Allows the player to choose to keep the loot (appends it to Player object's inventory list), equip the loot (calls the equip_item method of the Player object), or discard the loot (continues with no additional operation).

    Parameters
    ----------
    character:
        The Player object.
    
    """
    print(d.room_intros[5])

    # Give Coin.
    coin = character.level * 10
    character.coin_gain(coin)
    print("You find", str(coin), "Coin.  You now have", str(character.coin), "Coin.")

    # Give high level loot.
    num = character.level + 3
    loot = make_equipment(num)

    print("You find a", loot.name + ".  Its magical power is palpable.\n")
    character.display_item(loot)
    while True:
        choice = input(
            "Enter (1) to keep, (2) to equip, or (3) to discard. \n")
        if choice == "1":
            character.inventory.append(loot)
            print("You add the", loot.name, "to your inventory. \n")
            character.display_inventory(False)
            break
        elif choice == "2":
            character.equip_gear(loot)
            break
        elif choice == "3":
            print("You leave the", loot.name, "behind. \n")
            break
        elif choice == "MENU" or choice == "menu":
            game_menu(character)
        else:
            print("You must enter a valid option.")