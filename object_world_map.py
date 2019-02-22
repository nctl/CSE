class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


"""
Example
R19A = Room("Mr. Wiebe's Room")
parking_lot = Room("The Parking Lot", None, R19A)
R19A.north = parking_lot
"""

library = Room("Library", None, None, None, None, "Desc.")
quad = Room("Name", None, None, None, None, "Desc.")
N40 = Room("N40", None, None, None, None, "Desc.")
gym_1 = Room("Main Gym", N40, None, None, None, "Desc.")
north_hall = Room("Northern Hall", None, quad, None, N40, "Desc.")
south_hall = Room("Southern Hall", quad, None, None, None, "Desc.")
cafe = Room("Cafeteria", library, None, south_hall, None, "Desc.")
office = Room("Office", gym_1, library, quad, None, "Desc.")  # You start here

library.north = office
library.west = cafe
library.east = quad
quad.north = north_hall
quad.west = office
quad.south = south_hall
N40.south = gym_1
N40.east = north_hall
gym_1.south = office
south_hall.west = cafe
