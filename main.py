from classes.game import Person, bColor
from classes.magic import Spell

fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Blizzard", 14, 140, "black")

cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bColor.FAIL + bColor.BOLD + "AN ENEMY ATTACKS!" + bColor.ENDC)

while (running):
    print("====================================")
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
