import random

from classes.game import Person, bColor
from classes.magic import Spell
from classes.inventory import Item

# black magics
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Blizzard", 14, 140, "black")

# white magics
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

# items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores partt's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

player1 = Person("Varus", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Teemo", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Nexus", 3089, 174, 288, 34, player_spells, player_items)

enemy1 = Person("Elise", 1250, 130, 560, 325, [], [])
enemy2 = Person("Amumu", 18200, 701, 525, 25, [], [])
enemy3 = Person("Kaisa", 1250, 130, 560, 325, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print("\n" + bColor.FAIL + bColor.BOLD + "AN ENEMY ATTACKS!" + bColor.ENDC)

while (running):
    print("====================================")
    print("\n\n")
    print("NAME            HP                                     MP")
    for player in players:
        player.get_stats()

    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked", enemies[enemy].name.replace(" ", ""), "for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " is defeated")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic:")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bColor.FAIL + "\nNot enough MP\n" + bColor.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == 'white':
                player.heal(magic_dmg)
                print(bColor.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bColor.ENDC)
            elif spell.type == 'black':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(dmg)
                print(bColor.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg),
                      "points of damage to " + enemies[enemy].name.replace(" ", "") + bColor.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " is defeated")
                    del enemies[enemy]
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player_items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(bColor.FAIL + "\n" + "None left..." + bColor.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bColor.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bColor.ENDC)
            elif item.type == "elixer":

                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.max_hp
                        i.mp = i.max_mp

                player.hp = player.max_hp
                player.mp = player.max_mp
                print(bColor.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bColor.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bColor.FAIL + "\n" + item.name + "deals", str(item.prop),
                      "points of damage to " + enemies[enemy].name.replace(" ", "") + bColor.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " is defeated")
                    del enemies[enemy]

    enemy_choice = 1
    target = random.randrange(0, 3)

    enemy_dmg = enemies[0].generate_damage()
    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    if defeated_enemies == 3:
        print(bColor.OKGREEN + "You win!" + bColor.ENDC)
        running = False
    elif defeated_players == 3:
        print(bColor.FAIL + "Your enemy has defeated you!" + bColor.ENDC)
        running = False
