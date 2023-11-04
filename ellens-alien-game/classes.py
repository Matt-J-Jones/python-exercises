"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    health = 3
    def __init__(self, location_x, location_y):
        self.x_coordinate = location_x
        self.y_coordinate = location_y
        Alien.total_aliens_created += 1
    def hit(self):
        self.health -= 1
    def is_alive(self):
        if self.health > 0:
            return True
        return False
    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate
    def collision_detection(self, other):
        return None

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

def new_aliens_collection(position_data):
    aliens = []
    for coordinates in position_data:
        aliens.append(Alien(coordinates[0], coordinates[1]))
    return aliens
