class Item(object):
    def __init__(self):
        self.in_inventory = True


class Weapon(Item):
    def __init__(self, damage):
        super(Weapon, self). __init__()
        self.damage = damage


class Melee(Weapon):
    def __init__(self, damage):
        super(Melee, self). __init__()
        self.damage = damage
        self.range = 2


class Ranged(Weapon):
    def __init__(self, damage, range):
        super(Ranged, self).__init__()
        self.damage = damage
        self.range = range
        self.accuracy = 95

# ----------------------------------------------------------------------------------------------- #


class Armour(Item):
    def __init__(self, defense):
        super(Armour, self).__init__()
        self.defense = defense


class Helmet(Armour):
    def __init__(self, defense):
        super(Helmet, self).__init__()
        self.defense = defense


class Chestplate(Armour):
    def __init__(self, defense):
        super(Chestplate, self).__init__()
        self.defense = defense

# ----------------------------------------------------------------------------------------------- #


class Consumable(Item):
    def __init__(self):
        super(Consumable, self).__init__()
        self.quantity = 9


class Healing(Consumable):
    def __init__(self, hp_recovered):
        super(Healing, self).__init__()
        self.hp_recovered = hp_recovered
