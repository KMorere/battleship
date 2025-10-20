import random


class Ship:
    ships = []

    @classmethod
    def get_ships(cls):
        return f"{cls.ships}"

    def __init__(self, _name, _position, _size):
        self.name = _name
        self.position = _position
        self.size = _size
        self.ship = {"name":_name, "pos":_position}
        Ship.ships.append(self.ship)

    def set_hit(self, _position):
        if _position in self.position:
            self.size -= 1
            print(f"Hit {self.name} at {_position}.")

            if self.size == 0:
                print(f"Sunk {self.name}.")

            return True
        return False


def generate_ship(size, pos, direction):
    """ Places each tiles of a ship in the grid.

    :param size: Number of tiles on the grid.
    :param pos: Coordinates of the starting position.
    :param direction: Horizontal or vertical direction based on if direction is True or False.
    """
    def place_ship_row():
        grid[pos_y - 1][pos_x + step] = 1

        ship_pos.append(letters[pos_x + step] + (str(pos_y)))
        ship_pos.append(letters[pos_x + step] + (str(pos_y + 1)))
        ship_pos.append(letters[pos_x + step] + (str(pos_y - 1)))
    def place_ship_col():
        grid[pos_y - 1 + step][pos_x] = 1

        ship_pos.append(letters[pos_x] + (str(pos_y + step)))
        if pos_x + 1 < grid_size:
            ship_pos.append(letters[pos_x + 1] + (str(pos_y + step)))
        if pos_x - 1 > 0:
            ship_pos.append(letters[pos_x - 1] + (str(pos_y + step)))

    global ship_tile_amount
    pos_x, pos_y = get_coordinates(pos)

    if can_place_ship(pos_y, pos_x, size, direction): # If no ship is blocking the way.
        if direction is True: # True = left to right direction.
            if pos_x + size < grid_size: # Right.
                for step in range(0, size):
                    place_ship_row()
                    ship_tile_amount += 1
                ship_pos.append(letters[pos_x - 1] + (str(pos_y)))
                ship_pos.append(letters[pos_x + size] + (str(pos_y)))
            else: # Left.
                for step in range(0, -size, -1):
                    place_ship_row()
                    ship_tile_amount += 1
                ship_pos.append(letters[pos_x - size] + (str(pos_y)))
                if pos_x + 1 < grid_size:
                    ship_pos.append(letters[pos_x + 1] + (str(pos_y)))
        else: # False = up or down direction.
            if pos_y + size < grid_size: # Down.
                for step in range(0, size):
                    place_ship_col()
                    ship_tile_amount += 1
                ship_pos.append(letters[pos_x] + (str(pos_y - 1)))
                ship_pos.append(letters[pos_x] + (str(pos_y + size)))
            else: # Up.
                for step in range(0, -size, -1):
                    place_ship_col()
                    ship_tile_amount += 1
                ship_pos.append(letters[pos_x] + (str(pos_y + 1)))
                ship_pos.append(letters[pos_x] + (str(pos_y - size)))
    else: # Restart.
        get_random_coordinates()


def can_place_ship(pos_y, pos_x, size, direction):
    """ Checks in the line if it's possible to create a ship there.

    :param pos_y: Up coordinates (numbers).
    :param pos_x: Side coordinates (letters).
    :param size: Size of the ship in tiles of the grid.
    :param direction: Horizontal or vertical direction based on if direction is True or False.
    :return: Return True if you can place a ship, False if not.
    """
    for i in range(0, size):
        if direction is True:
            if pos_x + size < grid_size:
                if letters[pos_x + i] + (str(pos_y)) in ship_pos:
                    return False
            else:
                if letters[pos_x - i] + (str(pos_y)) in ship_pos:
                    return False
        else:
            if pos_y + size < grid_size:
                if letters[pos_x] + (str(pos_y + i)) in ship_pos:
                    return False
            else:
                if letters[pos_x] + (str(pos_y - i)) in ship_pos:
                    return False
    return True


def get_random_coordinates():
    """ Find a random starting point in the grid.
    """
    rand_nb = letters[random.randint(0, grid_size - 1)] + (str(random.randint(1, grid_size)))
    while rand_nb in ship_pos:
        rand_nb = letters[random.randint(0, grid_size - 1)] + (str(random.randint(1, grid_size)))

    generate_ship(random.choice(ship_list), rand_nb, bool(random.getrandbits(1))) # Get 0 or 1 randomly and convert it to bool.
    ship_pos.sort()


def get_coordinates(pos):
    """ Separate letter and number to later read."""
    return letters.index(pos[0]), int(pos[1:])


LETTER = ord('a')

grid_size = 10
ship_amount = 5
global ship_tile_amount
reader = ''

grid = [[0] * grid_size for _ in range(0, grid_size)]
ship_list = list(range(1, 6))

ship_pos = []
letters = [chr(LETTER + i) for i in range(0, grid_size)]

if __name__ == "__main__":
    new_pos = [(4, 4), (4, 5), (4, 6)]
    cruiser = Ship("Cruiser", new_pos, 3)

    new_pos = [(2, 2), (2, 3), (2, 4), (2, 5)]
    battleship = Ship("Battleship", new_pos, 4)

    print(f"{cruiser.name}{cruiser.position}, {cruiser.size}")
    print(f"{battleship.name}{battleship.position}, {battleship.size}")

    if not cruiser.set_hit((2, 2)):
        print("Miss.")

    print(Ship.get_ships())