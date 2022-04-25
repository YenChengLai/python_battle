import random
from .magic import Spell


class bColor:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_l = atk - 10
        self.atk_h = atk + 10
        self.magic = magic
        self.actions = ["Attack", "Magic", "Item"]
        self.items = items

    def generate_damage(self):
        return random.randrange(self.atk_l, self.atk_h)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + bColor.BOLD + self.name + bColor.ENDC)
        print(bColor.OKBLUE + "Actions" + bColor.ENDC)
        for item in self.actions:
            print("     " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bColor.OKBLUE + "Magics" + bColor.ENDC)
        for spell in self.magic:
            print("     " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bColor.OKGREEN + bColor.BOLD + "ITEMS:" + bColor.ENDC)
        for item in self.items:
            print("     " + str(i) + ".", item["item"].name, ":", item["item"].description,
                  " (x" + str(item["quantity"]) + ")")
            i += 1

    def get_stats(self):
        print("                       _________________________            __________ ")
        print(bColor.BOLD + self.name + "           " + str(self.hp) + "/" + str(self.max_hp) + "|"
              + bColor.OKGREEN + "████████████████████████" + bColor.ENDC
              + "|     " + str(self.mp) + "/" + str(self.max_mp) + " |" + bColor.OKBLUE + "█████████|" + bColor.ENDC)
