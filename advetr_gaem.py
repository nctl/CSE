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


class Ranged(Weapon):
    def __init__(self, name, damage):
        super(Ranged, self).__init__(name, damage)


class Armour(Item):
    def __init__(self, name, defense):
        super(Armour, self).__init__(name)
        self.defense = defense


class Helmet(Armour):
    def __init__(self, name, defense):
        super(Helmet, self).__init__(name, defense)


class Chestplate(Armour):
    def __init__(self, name, defense):
        super(Chestplate, self).__init__(name, defense)


class Shield(Armour):
    def __init__(self, name, defense):
        super(Shield, self).__init__(name, defense)


class Consumable(Item):
    def __init__(self, name, quantity):
        super(Consumable, self).__init__(name)
        self.quantity = quantity


class Healing(Consumable):
    def __init__(self, name, quantity, hp_recovered):
        super(Healing, self).__init__(name, quantity)
        self.hp_recovered = hp_recovered

# --------------------------------------------------------------------------------------------------------#


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


wooden_sword = Melee("Wooden Sword", 6)
sharp_sword = Melee("Sharp Sword", 14)
flame_sword = Melee("Flame Sword", 23)
legendary_sword = ("Legendary Sword", 30)
old_bow = Ranged("Old Bow", 9)
knight_bow = Ranged("Knight's Bow", 20)
armour_piercing_bow = Ranged("Armour Piercing Bow", 28)
leather_helmet = Helmet("Leather Helmet", 3)
iron_helmet = Helmet("Iron Helmet", 5)
fortified_helmet = Helmet("Fortified Helmet", 11)
leather_chestplate = Chestplate("Leather Chestplate", 7)
iron_chestplate = Chestplate("Iron Chestplate", 12)
fortified_chestplate = Chestplate("Fortified Chestplate", 20)
health_potion = Healing("Health Potion", 5, 50)
super_health_potion = Healing("Super Health Potion", 3, 120)
