# Classes


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
        super(Crowbar, self).__init__("Crowbar", 10)


class SharpSword(Melee):
    def __init__(self):
        super(SharpSword, self).__init__("Sharp Sword", 15)


class BattleAxe(Melee):
    def __init__(self):
        super(BattleAxe, self).__init__("Battle Axe", 19)


class FlameSword(Melee):
    def __init__(self):
        super(FlameSword, self).__init__("Flame Sword", 21)


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
        super(BasicBow, self).__init__("Basic Bow", 10)


class KnightBow(Ranged):
    def __init__(self):
        super(KnightBow, self).__init__("Knight's Bow", 26)


class Rifle(Ranged):
    def __init__(self):
        super(Rifle, self).__init__("Rifle", 29)


class ApBow(Ranged):
    def __init__(self):
        super(ApBow, self).__init__("Armour Piercing Bow", 33)
    

class Armour(Item):
    def __init__(self, name, defense):
        super(Armour, self).__init__(name)
        self.defense = defense


class Helmet(Armour):
    def __init__(self, name, defense):
        super(Helmet, self).__init__(name, defense)


class LeatherHelmet(Helmet):
    def __init__(self):
        super(LeatherHelmet, self).__init__("Leather Helmet", 2)


class IronHelmet(Helmet):
    def __init__(self):
        super(IronHelmet, self).__init__("Iron Helmet", 5)


class FortifiedHelmet(Helmet):
    def __init__(self):
        super(FortifiedHelmet, self).__init__("Fortified Helmet", 9)


class Chestplate(Armour):
    def __init__(self, name, defense):
        super(Chestplate, self).__init__(name, defense)


class LeatherChestplate(Chestplate):
    def __init__(self):
        super(LeatherChestplate, self).__init__("Leather Chestplate", 4)


class IronChestplate(Chestplate):
    def __init__(self):
        super(IronChestplate, self).__init__("Iron Chestplate", 7)


class FortifiedChestplate(Chestplate):
    def __init__(self):
        super(FortifiedChestplate, self).__init__("Fortified Chestplate", 12)


class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)


class Healing(Consumable):
    def __init__(self, name, hp_recovered):
        super(Healing, self).__init__(name)
        self.hp_recovered = hp_recovered


class HealthPotion(Healing):
    def __init__(self):
        super(HealthPotion, self).__init__("Health Potion", 50)


class SuperHealthPotion(Healing):
    def __init__(self):
        super(SuperHealthPotion, self).__init__("Super Health Potion", 120)


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
    def __init__(self, name, health, weapon, armour):
        super(Player, self).__init__(name, health, weapon, armour)
        self.inventory = [health_potion]  # infinite inventory, start with 1 health potion
        self.current_location = cave_1
        self.arrows = 7

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
        return room_name

    def attack(self, target):
        if issubclass(type(self.weapon), Ranged):
            if self.arrows <= 0:
                self.weapon = Melee("Bare Fists", 2)

            elif self.arrows == 1:
                print("%s attacks %s for %d damage" %
                      (self.name, target.name, self.weapon.damage))
                target.take_damage(self.weapon.damage)
                self.arrows = 0
                print("You are out of arrows. You can no longer use any bows.")

            else:
                self.arrows -= 1
                print("%s attacks %s for %d damage" %
                      (self.name, target.name, self.weapon.damage))
                target.take_damage(self.weapon.damage)
        else:
            print("%s attacks %s for %d damage" %
                  (self.name, target.name, self.weapon.damage))
            target.take_damage(self.weapon.damage)


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

weakest_enemy = Enemy("Punching Bag", 12, Melee("itself", 0), Armour("unequipped", 0))
weak_enemy = Enemy("Goblin", 26, Melee("Wooden Stick", 5), Armour("unequipped", 0))
basic_enemy1 = Enemy("Skeleton", 58, Melee("Bone Club", 8), Armour("Light Armour", 2))
basic_enemy2 = Enemy("Skeleton", 64, Melee("Bone Club", 11), Armour("Light Armour", 3))
bulky_enemy = Enemy("Giant", 106, Melee("Large Axe", 17), Armour("Aaaa", 11))
fast_enemy = Enemy("Spiked Bug", 24, Melee("Spikes", 38), Armour("Light Armour", 2))
ranged_enemy = Enemy("Castle Guard", 47, Ranged("Steel Bow", 15), Armour("Leather Chestplate", 5))
boss1 = Enemy("Dragon", 222, Melee("a BIG fireball", 24), Armour("Boss Armour", 7))
# -------------------------------------------------------------------------------------------------------- #
# Rooms


class Room(object):
    def __init__(self, name, north=None, south=None, east=None,
                 west=None,  description="None", items=None, enemies=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.item = items
        self.enemies = enemies


cave_1 = Room("A dark cave", None, None, None, None, "None")
cave_2 = Room("A dark cave", None, None, cave_1, None,
              "There appears to be an exit from this cave.")
your_house = Room("Your House", None, None, cave_2, None,
                  "This is your home.", wooden_sword)
field_1 = Room("An open field", None, your_house, None, None,
               "Don't forget to equip your sword with [equip {Item}]", None, weakest_enemy)
field_2 = Room("An open field", None, None, field_1, None,
               "A dilapidated house can be seen west.", None)
ruined_house = Room("Abandoned House", None, None, field_2, None,
                    "", leather_helmet, weak_enemy)
starting_chest = Room("Small Hills", None, field_2, None, None,
                      "There is an open box here", basic_bow)
castle_door = Room("Castle Entrance", None, starting_chest, None, None,
                   "A tall wooden door west leads the way to a castle.", sharp_sword)
castle_door2 = Room("Castle Exit", None, None, None, None,
                    "The door behind you is locked shut.", None)
hall = Room("Hall", None, None, castle_door2, None,
            "None", None, basic_enemy2)
gate = Room("The Gate", None, hall, None, None,
            "An open gate north from you can be seen along with a hostile dragon.", knight_bow)
staircase = Room("Staircase", gate, None, hall, None,
                 "None", health_potion, None)
throne_room = Room("Throne Room", None, None, staircase, None,
                   "None", None, fast_enemy)
room_14 = Room("A Two-Way Hall", throne_room, None, None, None,
               "None", flame_sword, None)
dungeon = Room("Dungeon", None, None, room_14, None,
               "There are decayed bones at the edge of the room.", armour_piercing_bow, bulky_enemy)
storage_room = Room("Storage Room", room_14, None, None, None,
                    "None", iron_chestplate, ranged_enemy)
forest = Room("Forest", None, None, None, castle_door,
              "A forest clearing lies east of you. There are also more trees south.", None, basic_enemy1)
statue = Room("Ancient Statue", forest, None, None, None,
              "A statue wearing a leather chestplate can be seen.", leather_chestplate)
field_3 = Room("Forest Edge", None, None, None, forest,
               "None", health_potion)
end = Room("Boss Room", None, None, None, None, "None", None, boss1)

cave_1.west = cave_2
cave_2.west = your_house
your_house.north = field_1
field_1.west = field_2
field_2.west = ruined_house
field_2.north = starting_chest
starting_chest.north = castle_door
castle_door.east = forest
castle_door.west = castle_door2
castle_door2.west = hall
hall.north = gate
hall.west = staircase
gate.west = staircase
gate.north = end
staircase.west = throne_room
throne_room.south = room_14
room_14.south = storage_room
room_14.west = dungeon
forest.south = statue
forest.east = field_3

the_player = Player("you", 200, Melee("Bare Fists", 2), Armour("unequipped", 0))
# -------------------------------------------------------------------------------------------------------- #
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while playing:
    if the_player.health <= 0:
        print("Game Over!")
        playing = False
    print()
    print("Current inventory:")
    for item in the_player.inventory:
        print(item.name)
    print()
    print(the_player.current_location.name)
    print(the_player.current_location.description)
    print("You have %d HP remaining." % the_player.health)
    print("You have %d arrows left." % the_player.arrows)
    if the_player.current_location.item is not None:
        print("There is a(n) %s on the ground." % the_player.current_location.item.name)
    if the_player.current_location.enemies is not None:
        print("%s stands, blocking your path." % the_player.current_location.enemies.name)
    if boss1.health <= 0:
        print("Congrats! You're Winner!")
        playing = False

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        if the_player.current_location.enemies is not None:
            print("There is someone blocking your path")
        else:
            try:
                next_room = the_player.find_room(command)
                if next_room is None:
                    raise AttributeError
                the_player.move(next_room)
            except AttributeError:
                print("I can't go that way.")
            except KeyError:
                print("I can't go that way.")

    elif "heal" in command:
        if health_potion in the_player.inventory:
            the_player.health += 50
            the_player.inventory.remove(health_potion)
            print("You now have %d HP." % the_player.health)

        else:
            print("I can't do that")

    elif "take" in command:
        item_name = command[5:]
        found_item = None
        if the_player.current_location.item.name == item_name:
            found_item = the_player.current_location.item
                
        if found_item is not None:
            the_player.inventory.append(found_item)
            the_player.current_location.item = None

    elif "attack" in command and the_player.current_location.enemies is not None:
        the_player.attack(the_player.current_location.enemies)
        if the_player.current_location.enemies.health <= 0:
            the_player.current_location.enemies = None
        else:
            the_player.current_location.enemies.attack(the_player)

    elif "equip" in command:
        equippable_item = command[6:]
        for equippable_item in the_player.inventory:
            if isinstance(equippable_item, Weapon):
                the_player.weapon = equippable_item
                print("Your new equipped weapon is %s" % the_player.weapon.name)

            if isinstance(equippable_item, Armour):
                the_player.armour = equippable_item
# -------------------------------------------------------------------------------------------------------- #
