"""
Object lists consist of strings, which are pulled from at random to populate the game's various non-player objects - Enemy, Ability, Item, and Boss.

This practice allows for a functionally limitless number of combinations - it is very unlikely two enemies, abilities, or items will be exactly the same.  This is common in "roguelike" games where the death of the player character is permanent - i.e., no "save" or "respawn" mechanism.  

Pseudo-randomly generating objects keeps the game feeling fresh - even when the core gameplay of traipsing through the same dungeon again and again is repetitive, no two playthroughs will ever feel quite the same.
"""

weapon_list = [
    {
        "name": "Bardiche",
        "inspect": "A two-handed polearm with a wicked, curved blade."
    },
    {
        "name": "Club",
        "inspect": "A short length of wood for bludgeoning in close-quarters."
    },
    {
        "name": "Rapier",
        "inspect": "A slender, light-weight and maneuverable sword."
    },
    {
        "name": "Quarterstaff",
        "inspect": "A versatile, wooden staff wielded with one or both hands."
    },
    {
        "name": "Longbow",
        "inspect": "A curved wooden hunting bow capable of firing arrows at great distances."
    },
    {
        "name": "Dagger",
        "inspect": "A short blade wielded with great accuracy in close-quarters."
    },
    {
        "name": "Crossbow",
        "inspect": "A mechanical crossbow that fires small metal quarrels."
    },
    {
        "name": "Greatsword",
        "inspect": "A massive, two-handed blade capable of cleaving enemies in two."
    },
    {
        "name": "Longsword",
        "inspect": "A long, one-handed sword for stabbing or slashing."
    },
    {
        "name": "Warhammer",
        "inspect": "A huge, two-handed hammer that pack a devastating punch."
    },
]

armor_list = [
    {
        "name": "Tarnished Chain Mail",
        "inspect": "A long vest made of interlaced iron rings."
    },
    {
        "name": "Reinforced Robes",
        "inspect": "A set of silken robes reinforced with plates of oiled leather."
    },
    {
        "name": "Gleaming Breastplate",
        "inspect": "A full set of heavy metal plate armor, polished to a shine."
    },
    {
        "name": "Padded Armor",
        "inspect": "Quilted cloth and batting layered to absorb attacks.",
    },
    {
        "name": "Studded Leather",
        "inspect": "Tough but flexible leathers reinforced with close-set metal rivets."
    },
    {
        "name": "Thick Hide",
        "inspect": "Crude armor fashioned from thick animal pelts."
    },
    {
        "name": "Scale Mail",
        "inspect": "A leather coat and leggings covered in overlapping scales of metal."
    }
]

gem_list = [
    "Emerald",
    "Ruby",
    "Sapphire",
    "Amber",
    "Amethyst",
    "Diamond",
    "Opal",
    "Pearl",
    "Quartz",
    "Citrine",
    "Garnet",
    "Jade",
    "Onyx",
    "Topaz"
]

bauble_list = [
    {
        "name": "Brooch",
        "inspect": "A sparkling brooch with a gold clasp."
    },
    {
        "name": "Choker",
        "inspect": "A close-fitting, silver necklace."
    },
    {
        "name": "Ring",
        "inspect": "A small brass ring."
    },
    {
        "name": "Bracelet",
        "inspect": "A gold bracelet studded with gems."
    },
    {
        "name": "Earrings",
        "inspect": "A pair of stud earrings."
    },
]

damage_spells = [
    {
        "name": "Fireball",
        "text": "You launch a searing ball of fire,",
        "text_enemy": "launches a searing ball of fire,",
        "overtime_text": "You continue to burn",
        "overtime_text_enemy": "Your foe continues to burn"
    },
    {
        "name": "Lightning Bolt",
        "text": "You launch a sizzling lightning bolt,",
        "text_enemy": "launches a sizzling lightning bolt,",
        "overtime_text": "You continue to experience electric jolts",
        "overtime_text_enemy": "Your foe continues to experience electric jolts"
    },
    {
        "name": "Cone of Cold",
        "text": "You launch a cone of swirling ice and snow,",
        "text_enemy": "launches a cone of swirling ice and snow,",
        "overtime_text": "You continue to suffer from the penetrating cold",
        "overtime_text_enemy": "Your foe continues to suffer from the penetrating cold"
    },
    {
        "name": "Entangling Vines",
        "text": "You conjure thorny vines to lash at your foe,",
        "text_enemy": "conjures thorny vines to lash at you,",
        "overtime_text": "The vines continue to thrash you",
        "overtime_text_enemy": "The vines continue to thrash your foe"    
    },
    {
        "name": "Acidic Goo",
        "text": "You launch a glob of acidic goo,",
        "text_enemy": "launches a glob of acidic goo,",
        "overtime_text": "The goo continues to eat away at your flesh",
        "overtime_text_enemy": "The goo continues to eat away at your foe's flesh"    
    },
    {
        "name": "Searing Light",
        "text": "You conjure a globe of searing light,",
        "text_enemy": "conjures a globe of searing light,",
        "overtime_text": "Your eyes continue stinging",
        "overtime_text_enemy": "Your foe's eyes continue stinging"    
    },
    {
        "name": "Curse of Agony",
        "text": "You inflict your foe with an agonizing curse,",
        "text_enemy": "inflicts you with an agonizing curse,",
        "overtime_text": "The curse wracks you with intense pain",
        "overtime_text_enemy": "The curse wracks your foe with intense pain"    
    },
]

healing_spells = [
    {
        "name": "Heal",
        "text": "You cast a healing enchantment,",
        "text_enemy": "casts a healing enchantment,",
        "overtime_text": "You continue to heal",
        "overtime_text_enemy": "Your foe continues to heal"
    }
]

enemy_list = [
    {
        "name": "Goblin",
        "greet": "A goblin scrambles into the room.  When it notices you, it shrieks in savage glee, brandishes its sword, and charges toward you.",
        "death": "The goblin slumps to the ground with a groan.",
    },
    {
        "name": "Cultist",
        "greet": "A cultist in a feathered cloak and beaked mask leaps at you from the shadows.",
        "death": "The cultist staggers back, then falls.",
    },
    {
        "name": "Skeleton",
        "greet": "A pile of bones rises from the floor to form an animated skeleton.",
        "death": "The skeleton crumbles to dust.",
    },
    {
        "name": "Zombie",
        "greet": "A rabid zombie shambles toward you, grasping with its rotting fingers.",
        "death": "The zombie collapses in a heap.",
    },
    {
        "name": "Gargoyle",
        "greet": "A stone gargoyle springs to life and sets its malicious gaze on you.",
        "death": "The gargoyle beats its wings a final time, then faints.",
    },
    {
        "name": "Orc",
        "greet": "A hulking, tusked orc notices your entrance and lifts its greataxe in challenge.",
        "death": "The orc tries stubbornly to keep fighting before succumbing to its wounds.",
    },
    {
        "name": "Mind Flayer",
        "greet": "A mind flayer floats into the chamber, its tentacled face wriggling eagerly.",
        "death": "A final, psionic scream floods your thoughts as the mind flayer dies.",
    },
    {
        "name": "Werewolf",
        "greet": "A furry, bipedal werewolf unleashes a savage howl as it advances.",
        "death": "The werewolf reverts to its human form in the throes of death.",
    },
    {
        "name": "Vampire",
        "greet": "A bat flutters toward you before transforming into a cloaked vampire.",
        "death": "'Finally... free,' the vampire whispers as it perishes.",
    },
]