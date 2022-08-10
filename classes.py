import msvcrt as m
import math
import random
import object_lists as l

class Player:
    """The Player class, controlled by the user. 
    
    One instantiation per run - the main character.  That object is then passed repeatedly through the ROOM functions and updated using its methods.

    Attributes
    ----------
    name:
        Main character's name - input provided by user.
    type:
        Main character's archetype - input provided by user.
    player: bool
        Always True - used in combat calculations.
    staunch, swift, shrewd, suave: int
        Player stats - used in calculations.
    hp, max_hp: int
        Player hitpoints and maximum hitpoints.  hp cannot exceed max_hp.  If hp is 0, game ends.
    mana, max_mana: int
        Player mana and maximum mana.  mana cannot exceed max_mana.  Mana is used to cast Spells.
    level, xp: int
        Player level.  At xp thresholds, level increases.  Advancing level is the primary progression mechanism in the game.
    coin: int
        Coin is the buy/spend resource mechanism, accrued throughout the game and spent in trade.
    inventory: list
        A list containing Item objects the player owns but does not have equipped.
    weapon, armor, bauble: list
        Lists containing Item objects the player has equipped (Gear).  The stats and bonuses of these items are passively applied to the Player object while equipped.
    abilities: list
        A list containing the player's Spells (Ability objects) and Consumable Items.
    companion: bool
        True if the player currently has an animal companion, False otherwise.
    companion_name, companion_type, companion_text: 
        Animal companion characteristics, used in combat text.


    """
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        self.player = True
        self.staunch = 10
        self.swift = 10
        self.shrewd = 10
        self.suave = 10
        self.hp = self.staunch * 2
        self.max_hp = self.staunch * 2
        self.mana = 30
        self.max_mana = 10 + (self.shrewd * 2)
        self.level = 1
        self.xp = 0
        self.coin = 0
        self.inventory = []
        self.weapon = []
        self.armor = []
        self.bauble = []
        self.abilities = []
        self.companion = False
        self.companion_name = ""
        self.companion_type = ""
        self.companion_text = ""

    def stat_change(self, stat: str, updown: str, num: int):
        """Method to increase player stats in response to game events.
        
        Increments or decrements a stat according to arguments received.
        Increments attributes if applicable.
        Ensures hp and mana do not exceed max_hp and max_mana.

        Parameters
        ----------
        stat:
            The stat to be adjusted.
        updown:
            Increments stat if "up", decrements stat if "down".
        num:
            The value to increment or decrement by. 
        """
        if updown == "up":
            if stat == "staunch":
                self.staunch += num
                self.max_hp += num * 2
                self.hp += num * 2
                print("You now have", str(self.staunch), "Staunch.")
            elif stat == "swift":
                self.swift += num
                print("You now have", str(self.swift), "Swift.")
            elif stat == "shrewd":
                self.shrewd += num
                self.max_mana += num * 2
                self.mana += num * 2
                print("You now have", str(self.shrewd), "Shrewd.")
            elif stat == "suave":
                self.suave += num
                print("You now have", str(self.suave), "Suave.")
        elif updown == "down":
            if stat == "staunch":
                self.staunch -= num
                self.max_hp -= num
                if self.hp > self.max_hp:
                    self.hp = self.max_hp
                print("You now have", str(self.staunch), "Staunch.")
            elif stat == "swift":
                self.swift -= num
                print("You now have", str(self.swift), "Swift.")
            elif stat == "shrewd":
                if self.mana > self.max_mana:
                    self.mana = self.max_mana
                self.shrewd -= num
                print("You now have", str(self.shrewd), "Shrewd.")
            elif stat == "suave":
                self.suave -= num
                print("You now have", str(self.suave), "Suave.")

    def xp_gain(self, num: int) -> bool: 
        """Method to increment player xp attribute in response to game events.
        
        Increments by num argument received.
        Calls lvl_check method to see if xp gain triggers a level up.
        If level up is triggered returns True, otherwise False.

        Parameters
        ----------
        num:
            The amount to increment the xp attribute. 
        """
        self.xp += num
        check = self.lvl_check()
        if check == True:
            return True
        else:
            return False

    def lvl_check(self) -> bool:
        """Method to compare player xp to level thresholds for level up.

        If current xp exceeds threshold to advance to next level, call lvl_up method and return True, otherwise return False.
        """
        if self.level == 1 and self.xp >= 20:
            self.level = 2
            self.lvl_up(2)
            return True
        elif self.level == 2 and self.xp >= 70:
            self.level = 3
            self.lvl_up(3)
            return True
        elif self.level == 3 and self.xp >= 130:
            self.level = 4
            self.lvl_up(4)
            return True
        elif self.level == 4 and self.xp >= 200:
            self.level = 5
            self.lvl_up(5)
            return True
        elif self.level == 5 and self.xp >= 280:
            self.level = 6
            self.lvl_up(6)
            return True
        elif self.level == 6 and self.xp >= 370:
            self.level = 7
            self.lvl_up(7)
            return True
        elif self.level == 7 and self.xp >= 470:
            self.level = 8
            self.lvl_up(8)
            return True
        elif self.level == 8 and self.xp >= 580:
            self.level = 9
            self.lvl_up(9)
            return True
        elif self.level == 9 and self.xp >= 700:
            self.level = 10
            self.lvl_up(10)
            return True
        else:
            return False

    def lvl_up(self, level: int):
        """Method to perform level up on player object.

        Check if new level is max level (10).
        Award 2 stat points per level, allowing player to assign the points and update the stat attributes by calling the stat_change method.

        Parameters
        ----------
        level:
            The player's new level.
        """
        print("You leveled up!  You are now level", str(level) + ".\n")
        self.mana = self.max_mana
        if level == 10:
            print("You have reached max level.  Great job!")

        # Gain 2 stat points at each level.
        print("You gained 2 stat points!")
        x = 0
        while x < 2:
            x += 1
            while True:
                print("(1) Staunch | (2) Swift | (3) Shrewd | (4) Suave")
                stat = input("Choose a stat to increase: \n").upper()
                if stat == "1" or stat == "STAUNCH":
                    stat = "staunch"
                    self.stat_change(stat, "up", 1)
                    break
                elif stat == "2" or stat == "SWIFT":
                    stat = "swift"
                    self.stat_change(stat, "up", 1)
                    break
                elif stat == "3" or stat == "SHREWD":
                    stat = "shrewd"
                    self.stat_change(stat, "up", 1)
                    break
                elif stat == "4" or stat == "SUAVE":
                    stat = "suave"
                    self.stat_change(stat, "up", 1)
                    break
                else:
                    print("You must choose a valid option.")

    def coin_gain(self, num: int):
        """Method to increment the coin attribute when Coin is gained.

        Parameters
        ----------
        num: 
            The amount to increment by. 
        """
        self.coin += num

    def coin_loss(self, num: int):
        """Method to increment the coin attribute when Coin is gained.

        Parameters
        ----------
        num: 
            The amount to increment by. 
        """
        self.coin -= num

    def equip_gear(self, item: object):
        """Method to equip an Item in a gear slot.

        Checks the slot attribute of the Item object.
        Pops the existing Item from the gear slot (if applicable) and appends the new Item.
        Updates the stat attributes accordingly.
        Calls the display_gear method to show the player the change. 

        Parameters
        ----------
        item: 
            The Item object to be equipped.
        """
        # Equip Item.
        if item.slot == "Weapon":
            print("You equip the", item.name, "and add your old", self.weapon[0].name, "to your inventory. \n")
            removed = self.weapon.pop(0)
            self.inventory.append(removed)
            self.weapon.append(item)
        elif item.slot == "Armor":
            print("You equip the", item.name, "and add your old",
                self.armor[0].name, "to your inventory. \n")
            removed = self.armor.pop(0)
            self.inventory.append(removed)
            self.armor.append(item)
        elif item.slot == "Bauble":
            print("You equip the", item.name, "and add your old",
                self.bauble[0].name, "to your inventory. \n")
            removed = self.bauble.pop(0)
            self.inventory.append(removed)
            self.bauble.append(item)

        # Update stats.
        staunch = item.stats["Staunch"] - removed.stats["Staunch"]
        swift = item.stats["Swift"] - removed.stats["Swift"]
        shrewd = item.stats["Shrewd"] - removed.stats["Shrewd"]
        suave = item.stats["Suave"] - removed.stats["Suave"]

        if staunch > 0:
            self.stat_change("staunch", "up", staunch)
        elif staunch < 0:
            self.stat_change("staunch", "down", staunch)
        if swift > 0:
            self.stat_change("swift", "up", swift)
        elif swift < 0:
            self.stat_change("swift", "down", swift)
        if shrewd > 0:
            self.stat_change("shrewd", "up", shrewd)
        elif shrewd < 0:
            self.stat_change("shrewd", "down", shrewd)
        if suave > 0:
            self.stat_change("suave", "up", suave)
        elif suave < 0:
            self.stat_change("suave", "down", suave)
        self.display_gear()

    def display_abilities(self):
        """Method to display the player's abilities outside of combat.
        
        Iterates through player's ability list, printing statements based on ability movetype.

        """
        print("========================")
        print(self.name + "'s Abilities")
        print("========================")
        x = 0
        for i in self.abilities:
            x += 1
            print("(" + str(x) + ")")
            print(i.name)
            if i.movetype == 1:
                print("Attack with your equipped weapon.")
                print("Base Damage:", str(self.weapon[0].max_dmg))
            elif i.movetype == 2:
                print("Attempt to mitigate incoming damage.")
                print("Blocks damage equal to your armor value ({}) plus your Staunch bonus ({}).".format(self.armor[0].armor, math.floor(self.staunch / 5)))
            elif i.movetype == 3:
                print("Cast a", i.name + ".")
                if i.subtype == "Damage Spell":
                    if i.overtime == True:
                        print("Deals", str(i.value), "damage plus your Shrewd bonus ({}) over",
                            str(i.duration), "turns.".format(math.floor(self.shrewd / 5)))
                    else:
                        print("Deals", str(i.value), "damage plus your Shrewd bonus ({}).".format(math.floor(self.shrewd / 5)))
                elif i.subtype == "Healing Spell":
                    if i.overtime == True:
                        print("Restores", str(i.value), "health plus your Shrewd bonus ({}) over",
                            str(i.duration), "turns.".format(math.floor(self.shrewd / 5)))
                    else:
                        print("Restores", str(i.value), "health plus your Shrewd bonus ({}).".format(math.floor(self.shrewd / 5)))
            elif i.movetype == 4:
                print(i.inspect)
        print("========================")

    def display_abilities_combat(self):
        """Method to display the player's abilities inside of combat.
        
        Iterates through player's ability list, printing statements based on ability movetype.
        Prints abbreviated statements to avoid clogging the screen during each combat loop.

        """
        abilities = []
        x = 0
        for ability in self.abilities:
            if ability.cooldown_count > 0:
                ability.cooldown_count -= 1
            elif ability.cooldown_count == 0:
                if ability.movetype == 1:
                    abilities.insert(0, ability)
                elif ability.movetype == 2:
                    abilities.insert(1, ability)
                elif ability.movetype == 3:
                    abilities.insert(2, ability)
                elif ability.movetype == 4:
                    abilities.append(ability)
        for ability in abilities:
            x += 1
            print("(" + str(x) + ")", ability.name)
            if ability.movetype == 1:
                print("Base Damage:", str(self.weapon[0].max_dmg), "(+" + str(math.floor(self.staunch / 5)) + ")")
            elif ability.movetype == 2:
                print("Base Armor:", str(self.armor[0].armor), "(+" + str(math.floor(self.staunch / 5)) + ")")
            elif ability.movetype == 3:
                if ability.subtype == "Damage Spell":
                    print("Mana Cost:", str(ability.manacost))
                    print("Damage:", str(ability.value), "(+" + str(math.floor(self.shrewd / 5)) + ") | Duration:", str(ability.duration), "| Cooldown:", str(ability.cooldown), "turns.")
                elif ability.subtype == "Healing Spell":
                    print("Mana Cost:", str(ability.manacost))
                    print("Healing:", str(ability.value), "(+" + str(math.floor(self.shrewd / 5)) + ") | Duration:", str(ability.duration), "| Cooldown:", str(ability.cooldown), "turns.")
            elif ability.movetype == 4:
                print(ability.inspect)
        return abilities

    def display_gear(self):
        """Method to display the player's currently equipped gear.
        
        Iterates through player's gear lists (weapon, armor, bauble), printing the relevant information for each Item.

        """
        print("============================")
        print(self.name + "'s Equipped Gear")
        print("============================")
        print(self.weapon[0].name)
        print(self.weapon[0].slot)
        print(self.weapon[0].inspect)
        print("Max Damage:", self.weapon[0].max_dmg)
        print("Staunch: +" + str(self.weapon[0].stats["Staunch"]), "|", "Swift: +" + str(self.weapon[0].stats["Swift"]), "|", "Shrewd: +" + str(self.weapon[0].stats["Shrewd"]), "|", "Suave: +" + str(self.weapon[0].stats["Suave"]))
        print("============================")
        print(self.armor[0].name)
        print(self.armor[0].slot)
        print(self.armor[0].inspect)
        print("Armor Value:", self.armor[0].armor)
        print("Staunch: +" + str(self.armor[0].stats["Staunch"]), "|", "Swift: +" + str(self.armor[0].stats["Swift"]), "|", "Shrewd: +" + str(self.armor[0].stats["Shrewd"]), "|", "Suave: +" + str(self.armor[0].stats["Suave"]))
        print("============================")
        print(self.bauble[0].name)
        print(self.bauble[0].slot)
        print(self.bauble[0].inspect)
        print("Staunch: +" + str(self.bauble[0].stats["Staunch"]), "|", "Swift: +" + str(self.bauble[0].stats["Swift"]), "|", "Shrewd: +" + str(self.bauble[0].stats["Shrewd"]), "|", "Suave: +" + str(self.bauble[0].stats["Suave"]))
        print("============================")
        print("Press any key to continue.")
        m.getch()

    def display_item(self, item: object):
        """Method to display an Item.
        
        Prints relevant information based on the Item's slot.
        Primarily used in combat rewards and shops. 

        Parameters
        ----------
        item:
            The Item object to be displayed.

        """
        print(item.name)
        print(item.slot)
        print(item.inspect)
        if item.slot == "Weapon":
            print("Max Damage:", item.max_dmg)
        elif item.slot == "Armor":
            print("Armor Value:", item.armor)
        if item.slot != "Consumable":
            print("Staunch: +" + str(item.stats["Staunch"]), "|", "Swift: +" + str(item.stats["Swift"]), "|", "Shrewd: +" + str(item.stats["Shrewd"]), "|", "Suave: +" + str(item.stats["Suave"]))
        print("Sell Price:", str(item.sell) + "\n")

    def display_inventory(self, equip: bool):
        """Method to display the Item objects in the player's inventory.
        
        Iterates through player's inventory list, printing the relevant information for each Item.
        If equip is True, permits the player to equip an inventory Item by inputting its corresponding number.

        Parameters
        ----------
        equip:
            True if player is permitted to equip an item in the inventory display, False otherwise.

        """
        x = 1
        print("========================")
        print(self.name + "'s Inventory")
        print("========================")
        for i in self.inventory:
            print("(" + str(x) + ")")
            x += 1
            self.display_item(i)
        if equip == True:
            if len(self.inventory) != 0:
                while True:
                    leave = len(self.inventory) + 1
                    choice = input("You can equip an item by entering its corresponding number, or enter (" + str(leave) + ") to return to the main menu. ")
                    check = choice.isupper() or choice.islower()
                    if check == False  and choice != "":
                        choice = int(choice)
                        if choice > (len(self.inventory) + 1):
                            print("You must enter a valid number.")
                        elif choice == leave:
                            break
                        else:
                            choice = choice - 1
                            if self.inventory[choice].can_consume == True:
                                print("You cannot equip a consumable item.")
                            else:
                                self.equip_gear(self.inventory[choice])
                    else:
                        print("You must enter a valid number.")

    def sheet(self):
        """Method to display a longform character sheet.
        
        Prints statements for all pertinent player attributes.

        """
        print("\n===============")
        print("Character Sheet")
        print("===============")
        print("Name:", self.name)
        print("Archetype:", self.type)
        print("Level:", self.level, "")
        if self.companion == True:
            print("Companion:", self.companion_name, "the", self.companion_type)
        print("Coin:", self.coin)
        print("Max HP:", self.max_hp)
        print("Current HP:", self.hp, "\n")
        print("Max Mana:", self.max_mana)
        print("Current Mana:", self.mana)
        print("=====")
        print("Stats")
        print("=====")
        print("Staunch:", str(self.staunch), "(Bonus weapon damage, armor, and HP.)")
        print("Swift:", str(self.swift), "(Bonus crit and dodge chance.)")
        print("Shrewd:", str(self.shrewd), "(Bonus magic damage and magic resistance.)")
        print("Suave:", str(self.suave), "(Bonus coin, better treasure, and shop discounts.)\n")
        print("=============")
        print("Equipped Gear")
        print("=============")
        print("Weapon:")
        self.display_item(self.weapon[0])
        print("Armor:")
        self.display_item(self.armor[0])
        print("Bauble:")
        self.display_item(self.bauble[0])
        print("=========")
        print("Inventory")
        print("=========")
        if len(self.inventory) >= 1:
            x = 1
            for item in self.inventory:
                print("(" + str(x) + ")")
                self.display_item(item)
                x += 1
        else:
            print("Your inventory is empty.")

    def sheet_intro(self):
        """Method to display a shortform character sheet.
        
        Prints abbreviated statements for all pertinent player attributes.
        Used during the game to prevent text from clogging the screen.
        
        """
        print("\n===============")
        print("Character Sheet")
        print("===============")
        print("Name:", self.name)
        print("Archetype:", self.type, "\n")
        if self.companion == True:
            print("Companion:", self.companion_name, "the", self.companion_type)
        print("Level:", self.level)
        print("Coin:", self.coin)
        print("Max HP:", self.max_hp)
        print("Current HP:", self.hp)
        print("Max Mana:", self.max_mana)
        print("Current Mana:", self.mana, "\n")
        print("Staunch:", str(self.staunch))
        print("Swift:", str(self.swift))
        print("Shrewd:", str(self.shrewd))
        print("Suave:", str(self.suave))
        print("===============")

class Item:
    """The Item class, used to generate and randomize Items.
    
    Initializes Item objects with empty values.
    Includes method to randomize all object attributes.
    
    Attributes
    ----------
    name: str
        The name of the Item, pulled randomly from the object lists module.
    inspect: str
        A line of text giving a brief description of the Item, pulled randomly from the object lists module.
    can_equip:
        True if the Item is a weapon, armor, or bauble, False otherwise.
    slot: str
        The gear slot an Item can be equipped in - weapon, armor, or bauble.
    buy: int
        The Coin required to buy the Item from a shop.
    sell: int
        The Coin received when selling the Item to a shop.
    max_dmg: int
        For weapons: the maximum damage value, used in combat calculations.
    armor: int
        For armor: the Item's damage mitigation value, used in combat calculations.
    stats: dict
        The stat bonuses conferred while the Item is equipped.
    can_consume:
        True if the Item is a consumable potion, False otherwise.
    effect: int
        The effect conferred when consuming the item, 1 thru 5.
        1: Restores HP
        2: Restores Mana
        3: Temporarily buffs Staunch.
        4: Temporarily buffs Swift.
        5: Temporarily buffs Shrewd.
    value: int
        The potency of the consumable effect.  Dictates HP and mana restored, or value of the stat increase.
    movetype: int
        Always 4.  Used to allow consumable Items to display as Abilities during combat.
    cooldown, cooldown_count, mana_cost: int
        Always 0.  Used to allow consumable Items to display as Abilities during combat.

    """
    def __init__(self, can_equip: bool, can_consume: bool):
        # General properties.
        self.name = None
        self.inspect = None
        # Equipment properties.
        self.can_equip = can_equip
        self.slot = None
        self.buy = 0
        self.sell = 0
        self.max_dmg = None
        self.armor = None
        self.stats = {
            "Staunch": 0,
            "Swift": 0,
            "Shrewd": 0,
            "Suave": 0
        }
        # Consumable properties.
        self.can_consume = can_consume
        self.effect = None
        self.value = None
        self.movetype = 4
        self.cooldown = 0
        self.cooldown_count = 0
        self.manacost = 0

    def randomize(self, num: int):
        """Method to randomize an Item object's attributes.
        
        First checks the can_equip and can_consume attribute values to determine item type.
        Receives the player object's level attribute value as a parameter - this allows Items to scale in power with the player's level.
        
        Parameters
        ----------
        num:
            The player object's level, used in multipliers to scale Item as game goes on.
        
        """
        # If equippable:
        if self.can_equip == True:
            # Randomize slot, choose random item and randomize its stats.
            slot = random.randint(0, 2)
            if slot == 0:
                self.slot = "Weapon"
                choose_weapon = random.choice(l.weapon_list)

                name = choose_weapon["name"]
                self.name = name

                inspect = choose_weapon["inspect"]
                self.inspect = inspect

                range_one = num * 3
                range_two = num * 5
                damage = random.randint(range_one, range_two)
                self.max_dmg = damage

                if damage >= 4 and damage <= 6:
                    self.buy = 40
                    self.sell = 20
                elif damage >= 7 and damage <= 10:
                    self.buy = 80
                    self.sell = 40
                elif damage >= 11 or damage <= 14:
                    self.buy = 120
                    self.sell = 60
                elif damage >= 15 or damage <= 20:
                    self.buy = 200
                    self.sell = 100
                elif damage > 20:
                    self.buy = 250
                    self.sell = 125
            elif slot == 1:
                self.slot = "Armor"
                choose_armor = random.choice(l.armor_list)

                name = choose_armor["name"]
                self.name = name

                inspect = choose_armor["inspect"]
                self.inspect = inspect

                armor = random.randint(1, num)
                self.armor = armor

                if armor == 1 or armor == 2:
                    self.buy = 40
                    self.sell = 20
                elif armor == 3 or armor == 4:
                    self.buy = 80
                    self.sell = 40
                elif armor == 5:
                    self.buy = 120
                    self.sell = 60
            elif slot == 2:
                self.slot = "Bauble"
                gem = random.choice(l.gem_list)
                choose_bauble = random.choice(l.bauble_list)
                name = choose_bauble["name"]

                name = "{} {}".format(gem, name)
                self.name = name

                inspect = choose_bauble["inspect"]
                self.inspect = inspect

                self.buy = 80
                self.sell = 40
            
            # Randomize stat bonuses.
            stats_range = num + 1
            if self.slot == "Bauble":
                stats_range = num + 2
            stats = random.randint(1, stats_range)
            if self.slot == "Bauble":
                stats = stats_range
            self.buy += stats * 10
            self.sell += stats * 5
            x = 0
            while x < stats:
                x += 1
                stat = random.randint(1, 4)
                if stat == 1:
                    self.stats["Staunch"] += 1
                elif stat == 2:
                    self.stats["Swift"] += 1
                elif stat == 3:
                    self.stats["Shrewd"] += 1
                elif stat == 4:
                    self.stats["Suave"] += 1
        
        # If consumable:
        elif self.can_consume == True:
            self.slot = "Consumable"
            # Health, mana, or stat potion.
            type = random.randint(1, 3)
            if type == 1:
                self.effect = 1
                self.value = 1
                self.name = "Health Potion"
                self.inspect = "Drink this to restore health equal to your level times 10."
                self.buy = 10
                self.sell = 5
                self.movetype = 4
            elif type == 2:
                self.effect = 2
                self.value = 1
                self.name = "Mana Potion"
                self.inspect = "Drink this to restore mana equal to your level times 10."
                self.buy = 10
                self.sell = 5
                self.movetype = 4
            elif type == 3:
                stat = random.randint(1, 3)
                amount = random.randint(1, 5)
                self.movetype = 4
                if stat == 1:
                    self.effect = 3
                    self.value = amount
                    self.name = "Staunch Potion"
                    self.inspect = "Drink this to gain {} Staunch until the end of combat.".format(amount)
                    self.buy = 20
                    self.sell = 10
                elif stat == 2:
                    self.effect = 4
                    self.value = amount
                    self.name = "Swift Potion"
                    self.inspect = "Drink this to gain {} Swift until the end of combat.".format(amount)
                    self.buy = 20
                    self.sell = 10
                elif stat == 3:
                    self.effect = 5
                    self.value = amount
                    self.name = "Shrewd Potion"
                    self.inspect = "Drink this to gain {} Shrewd until the end of combat.".format(amount)
                    self.buy = 20
                    self.sell = 10

class Ability:
    """The Ability class, used to generate and randomize Spells.
    
    Works in conjunction with the make_spells function to generate lists of random Spells for the player and Enemies.

    Attributes
    ----------
    movetype: int
        The type of ability, used in combat calculations.
        1: Basic Weapon Attack
        2: Block
        3: Spell
        4: Consumable Item
    name: str
        The name of the Ability, pulled randomly from object lists module.
    text: str
        The combat text displayed when the Ability is used by the player, used in combat.
    text_enemy: str
        The combat text displayed when the Ability is used by an Enemy, used in combat.
    overtime_text: str
        The combat text displayed when the Ability deals damage over time (DOT) or restores HP over time (HOT).
    subtype: str
        The subtype, used for Spells to differentiate between Healing Spells and Damage Spells, used in combat calculations.
    overtime: bool
        True if the Ability deals damage or restores HP over time (DOT/HOT), False otherwise.
    duration: int
        The number of turns the Ability deals damage or restores HP over time (DOT/HOT).
    cooldown_count: int
        The number of turns remaining until an Ability can be used again.  Set during combat and decremented from the cooldown value to 0.
    cooldown: int
        The number of turns a player must wait after using the Ability before using it again.
    manacost: int
        The amount of mana the player must spend to use the Ability.
    value: int
        The amount of damage dealt or HP restored by the Ability.

    """
    def __init__(self, movetype: int):
        self.movetype = movetype
        self.name = ""
        self.text = ""
        self.text_enemy = ""
        self.overtime_text = ""
        self.overtime_text_enemy = ""
        self.subtype = "Subtype"
        self.overtime = False
        self.duration = 1
        self.cooldown_count = 0
        self.cooldown = 0
        self.manacost = 0
        self.value = 0

class Enemy:
    """The Enemy class, used to generate and randomize Enemies.
    
    Enemies are generated and populated during combat for the player to fight against.
    
    Attributes
    ----------
    level:
        Received as a parameter during initialization, typically the player's level (with some exceptions).
    name: str
        The enemy's name, pulled randomly from object lists module.
    greet: str
        The text to be displayed when the player encounters the Enemy, pulled randomly from the object lists module.
    death: str
        The text to be displayed when the player defeats the Enemy, pulled randomly from the object lists module.
    player: bool
        Always False - used in combat calculations.
    hp: int
        The Enemy's HP, used in combat calculations.
    max_hp: int
        The Enemy's maximum HP, used in combat calculations.  HP cannot exceed max HP.
    abilities: list
        The Enemy's Abilities, generated randomly and appended to when the Enemy is generated.
        
    """
    def __init__(self, level: int):
        self.level = level
        self.name = ""
        self.greet = ""
        self.death = ""
        self.player = False
        self.hp = 0
        self.max_hp = 0
        self.abilities = []
    
    def populate(self):
        """A module to populate the Enemy's attributes.
        
        Called when the Enemy object is generated.

        """
        identity = random.choice(l.enemy_list)
        self.name = identity["name"]
        self.greet = identity["greet"]
        self.death = identity["death"]
        self.hp = self.level * 15
        self.max_hp = 15 + (self.level * 10)
        self.block = self.level + 2

class Boss:
    """The Boss class, used to generate the Final Boss Enemy.

    Functions the same as the Enemy class except that most attributes are not randomized - Final Boss is always the same.

    Parameters
    ----------
    Same as Enemy object, except:
    incantation:
        True if the player encountered the incantation event during the game, False otherwise.
        If incantation is True, Final Boss stats change. 
    """
    def __init__(self, incantation: bool):
        self.name = "Beast"
        self.incantation = incantation
        self.greet = ""
        self.death = "'HOW?!  HOW CAN THIS BE?!'  Björn's voice shifts in timbre from a deep, thundering bellow to a pitiful whine as it reverts to its normal size.  With a cough and a wheeze, the creature's eyes close and it stills.  The cultists flee the chamber, deeper into the bowels of the lair, the echo of their sorrowful wails growing more distant.\n"
        self.player = False
        if self.incantation == True:
            self.hp = 175
            self.max_hp = 175
            self.level = 8
        elif self.incantation == False:
            self.hp = 250
            self.max_hp = 250
            self.level = 12
        self.abilities = []