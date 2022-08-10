import functions as f
import classes as c
import msvcrt as m

# Create an "empty" Item object - can_equip True, can_consume False.
print("Create an empty Item object - can_equip True, can_consume False.")
test_item = c.Item(True, False)
attributes = dir(test_item)
print("\n", vars(test_item), "\n")
m.getch()

# Randomize Item object's attributes.
print("Randomize Item object's attributes.")
test_item.randomize(1)
print(vars(test_item), "\n")
m.getch()

# Create an "empty" Item object - can_equip False, can_consume True.
print("Create an empty Item object - can_equip False, can_consume True.")
test_item_cons = c.Item(False, True)
attributes = dir(test_item_cons)
print("\n", vars(test_item_cons), "\n")
m.getch()

# Randomize Item object's attributes.
print("Randomize Item object's attributes.")
test_item_cons.randomize(0)
print(vars(test_item_cons), "\n")
m.getch()

# Create an "empty" Enemy object.
print("Create an empty Enemy object.")
test_enemy = c.Enemy(3)
print(vars(test_enemy), "\n")
m.getch()

# Populate Enemy object's base stats based on argument 3 - "level".
print("Populate Enemy object's base stats based on argument.")
test_enemy.populate()
print(vars(test_enemy), "\n")
m.getch()

# Generate Ability objects and populate Enemy object's Abilities list.
print("Generate Ability objects and populate Enemy object's Abilities list.")
f.enemy_starter_abilities(test_enemy)
f.make_spells(test_enemy, 1)
for ability in test_enemy.abilities:
    print(vars(ability), "\n")