# Classes
class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None, west=None, description="INSERT DESCRIPTION HERE"):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


cave_1 = Room("Start", None, None, None, None)
cave_2 = Room("A dark cave", None, None, cave_1, None)
your_house = Room("Your House", None, None, cave_2, None)
field_1 = Room("An open field", None, your_house, None, None)
field_2 = Room("An open field", None, None, field_1, None)
ruined_house = Room("Abandoned House", None, None, field_2, None)
starting_chest = Room("", None, field_2, None, None)
castle_door = Room("Castle Entrance", None, starting_chest, None, None)
entrance_1 = Room("", None, None, None, None)
room_9 = Room("", entrance_1, None, None, None)
room_10 = Room("", None, None, room_9, None)
room_11 = Room("", None, room_10, None, None)
room_12 = Room("", room_11, None, room_10, None)
room_13 = Room("", None, None, room_12, None)
room_14 = Room("", None, None, None, None)
room_15 = Room("", None, None, None, None)
room_16 = Room("", None, None, None, None)
room_17 = Room("", None, None, None, None)
room_18 = Room("", None, None, None, None)
room_19 = Room("", None, None, None, None)
room_20 = Room("", None, None, None, None)

cave_1.west = cave_2
cave_2.west = your_house
your_house.north = field_1
field_1.west = field_2
field_2.west = ruined_house
field_2.north = starting_chest
starting_chest.north = castle_door
castle_door.west = entrance_1  # This is a one-way
entrance_1.south = room_9
room_9.west = room_10
room_10.north = room_11
room_10.west = room_12
room_11.south = room_12
room_12.west = room_13
room_13.south = room_14
room_14.south = room_16
room_14.west = room_15
# -------------------------------------------------------------------------------------------------------- #


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Melee(Weapon):
    def __init__(self, name, damage):
        super(Melee, self).__init__(name, damage)


class WoodenSword(Melee):
    def __init__(self):
        super(WoodenSword, self).__init__("Wooden Sword", 6)


class Crowbar(Melee):
    def __init__(self):
        super(Crowbar, self).__init__("Crowbar", 12)


class SharpSword(Melee):
    def __init__(self):
        super(SharpSword, self).__init__("Sharp Sword", 15)


class BattleAxe(Melee):
    def __init__(self):
        super(BattleAxe, self).__init__("Battle Axe", 22)


class FlameSword(Melee):
    def __init__(self):
        super(FlameSword, self).__init__("Flame Sword", 28)


class LegendarySword(Melee):
    def __init__(self):
        super(LegendarySword, self).__init__("Legendary Sword", 50)


class Ranged(Weapon):
    def __init__(self, name, damage):
        super(Ranged, self).__init__(name, damage)


class OldBow(Ranged):
    def __init__(self):
        super(OldBow, self).__init__("Old Bow", 6)


class BasicBow(Ranged):
    def __init__(self):
        super(BasicBow, self).__init__("Basic Bow", 9)


class KnightBow(Ranged):
    def __init__(self):
        super(KnightBow, self).__init__("Knight's Bow", 20)


class Rifle(Ranged):
    def __init__(self):
        super(Rifle, self).__init__("Rifle", 29)


class ApBow(Ranged):
    def __init__(self):
        super(ApBow, self).__init__("Armour Piercing Bow", 35)
    

class Armour(Item):
    def __init__(self, name, defense):
        super(Armour, self).__init__(name)
        self.defense = defense


class Helmet(Armour):
    def __init__(self, name, defense):
        super(Helmet, self).__init__(name, defense)


class LeatherHelmet(Helmet):
    def __init__(self):
        super(LeatherHelmet, self).__init__("Leather Helmet", 3)


class IronHelmet(Helmet):
    def __init__(self):
        super(IronHelmet, self).__init__("Iron Helmet", 5)


class FortifiedHelmet(Helmet):
    def __init__(self):
        super(FortifiedHelmet, self).__init__("Fortified Helmet", 11)


class Chestplate(Armour):
    def __init__(self, name, defense):
        super(Chestplate, self).__init__(name, defense)


class LeatherChestplate(Chestplate):
    def __init__(self):
        super(LeatherChestplate, self).__init__("Leather Chestplate", 7)


class IronChestplate(Chestplate):
    def __init__(self):
        super(IronChestplate, self).__init__("Iron Chestplate", 12)


class FortifiedChestplate(Chestplate):
    def __init__(self):
        super(FortifiedChestplate, self).__init__("Fortified Chestplate", 19)


class Consumable(Item):
    def __init__(self, name, quantity):
        super(Consumable, self).__init__(name)
        self.quantity = quantity


class Healing(Consumable):
    def __init__(self, name, quantity, hp_recovered):
        super(Healing, self).__init__(name, quantity)
        self.hp_recovered = hp_recovered


class HealthPotion(Healing):
    def __init__(self):
        super(HealthPotion, self).__init__("Health Potion", 5, 50)


class SuperHealthPotion(Healing):
    def __init__(self):
        super(SuperHealthPotion, self).__init__("Super Health Potion", 3, 120)


class Character(object):
    def __init__(self, name, health, weapon, armour):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armour = armour

    def take_damage(self, damage):
        if damage < self.armour.defense:
            print("No damage is done.")

        else:
            self.health -= damage - self.armour.defense
            if self.health <= 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" %
              (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Player(Character):
    def __init__(self, name, health, weapon, armour, starting_location):
        super(Player, self).__init__(name, health, weapon, armour)
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """
        :param new_location:
        """
        self.current_location = new_location

    def find_room(self, direction):
        """
        :param direction:
        :return:
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]


class Enemy(Character):
    def __init__(self, name, health, weapon, armour):
        super(Enemy, self).__init__(name, health, weapon, armour)
# -------------------------------------------------------------------------------------------------------- #
# Items


wooden_sword = WoodenSword()
crowbar = Crowbar()
sharp_sword = SharpSword()
battle_axe = BattleAxe()
flame_sword = FlameSword()
legendary_sword = LegendarySword()
old_bow = OldBow()
basic_bow = BasicBow()
knight_bow = KnightBow()
rifle = Rifle()
armour_piercing_bow = ApBow()
leather_helmet = LeatherHelmet()
iron_helmet = IronHelmet()
fortified_helmet = FortifiedHelmet()
leather_chestplate = LeatherChestplate()
iron_chestplate = IronChestplate()
fortified_chestplate = FortifiedChestplate()
health_potion = HealthPotion()
super_health_potion = SuperHealthPotion()
# -------------------------------------------------------------------------------------------------------- #
# Characters and Mobs

player = Player("Human", 150, Melee("Bare Fists", 1), Armour("unequipped", 0), room_1)

weakest_enemy = Enemy("1", 17, Melee("Stick", 4), Armour("unequipped", 0))
weak_enemy = Enemy("6", 44, Melee("Improved Stick", 9), Armour("unequipped", 0))
basic_enemy = Enemy("5", 78, Melee("Hard Club", 15), Armour("Light Armour", 3))
bulky_enemy = Enemy("2", 114, Melee("Large Axe", 23), Armour("\/", 12))
fast_enemy = Enemy("3", 9, Melee("?", 64), Armour("Light Armour", 3))
ranged_enemy = Enemy("4", 41, Ranged("Fast Bow", 11), Armour("Leather Chestplate", 7))
boss1 = Enemy("+", 450, Melee("a BIG plane", 69), Armour("Boss Armour", 20))
# -------------------------------------------------------------------------------------------------------- #
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")

    elif "take" in command:
        item_name = command[5:]
        found_item = None
        for item in player.current_location.items:
            if item == item_name:
                found_item = item
                
        if found_item is not None:
            player.inventory.append(found_item)
            player.current_location.items.remove(found_item)
    else:
        print("Command not recognized.")

# -------------------------------------------------------------------------------------------------------- #
