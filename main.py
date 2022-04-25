from classes.game import Person, bColor
from classes.magic import Spell
from classes.inventory import Item

# black magics
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Blizzard", 14, 140, "black")

# white magics
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 50)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores partt's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

player1 = Person("Varus", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Teemo", 460, 65, 60, 34, player_spells, player_items)
player3 = Person("Nexus", 460, 65, 60, 34, player_spells, player_items)

enemy = Person("Blitz", 1200, 65, 45, 25, [], [])

players = [player1, player2, player3]

running = True
i = 0

print("\n" + bColor.FAIL + bColor.BOLD + "AN ENEMY ATTACKS!" + bColor.ENDC)

while (running):
    print("====================================")
    print("\n\n")
    print("NAME            HP                                    MP")
    for player in players:
        player.get_stats()

    print("\n")

    for player in players:
        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage.")
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
                enemy.take_damage(magic_dmg)
                print(bColor.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bColor.ENDC)
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
                player.hp = player.max_hp
                player.mp = player.max_mp
                print(bColor.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bColor.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bColor.FAIL + "\n" + item.name + "deals", str(item.prop), "points of damage" + bColor.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("--------------------------------")
    print("Enemy HP:", bColor.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bColor.ENDC + "\n")
    print("Your HP:", bColor.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bColor.ENDC)
    print("Your MP:", bColor.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bColor.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bColor.OKGREEN + "You win!" + bColor.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bColor.FAIL + "Your enemy has defeated you!" + bColor.ENDC)
        running = False
