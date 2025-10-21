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


class Grid:
    grid = []

    @classmethod
    def get_cell(cls, _column, _row):
        return cls.grid[_column][_row]

    def __init__(self):
        Grid.grid = [[0] * grid_size for _ in range(0, grid_size)]


def generate_grid():
    """ Writes the grid in the console.
    """
    print(end='    |')

    for i in range(0, grid_size):
        print(f" {letters[i].upper()} ", end='|')
    print()

    for y in range(0, grid_size):
        print("----", end='|')
        for _ in range(0, grid_size):
            print("---", end='|')
        print()
        if y + 1 < 10:
            print(f" {y + 1}  ", end='|')
        else:
            print(f" {y + 1} ", end='|')
        for x in range(0, grid_size):
            if grid[y][x] <= 1:
                print(f"   ", end='|')
            elif grid[y][x] == 2:
                print(f" 0 ", end='|')
            elif grid[y][x] == 3:
                print(f" X ", end='|')
        print()


def generate_ship():
    """ Generate each ship using specific coordinates. """

    global ships
    global ship_tile_amount

    for i in range(len(coords)):
        for j in range(len(coords[i])):
            y = coords[i][j][0]-1
            x = coords[i][j][1]-1
            grid[y][x] = 1
            ship_tile_amount += 1

    ships = [
        Ship("Torpedo", coords[0], 2),
        Ship("Cruiser", coords[1], 3),
        Ship("Cruiser_2", coords[2], 3),
        Ship("Battleship", coords[3], 4),
        Ship("Aircraft", coords[4], 5),
    ]


def get_coordinates(pos):
    """ Separate letter and number to later read."""
    return letters.index(pos[0]), int(pos[1:])


def is_valid_coordinate(pos):
    """ Is the user's input a valid coordinate to read and use."""

    if pos[0].isalpha and pos[1:].isdigit():
        letter = pos[0]
        numbers = int(pos[1:])

        return letter in letters and 0 < numbers <= grid_size
    else:
        return False


def shoot(pos):
    """ Uses the coordinates to shoot in the grid.

    :param pos: Coordinates of the torpedo.
    """
    pos_x, pos_y = get_coordinates(pos)
    pos_y -= 1

    global ship_tile_amount

    if grid[pos_y][pos_x] <= 1:
        match grid[pos_y][pos_x]:
            case 0:
                grid[pos_y][pos_x] = 2
                print("Missed.")
            case 1:
                grid[pos_y][pos_x] = 3
                ship_tile_amount -= 1
                print("Hit !")
    else:
        print("Coordinates already hit !")
    print("Ship tiles left : ", ship_tile_amount)


LETTER = ord('a')

grid_size = 10
ship_amount = 5
global ship_tile_amount
reader = ''

grid = Grid().grid
ship_list = list(range(1, 6))

ships = []
letters = [chr(LETTER + i) for i in range(0, grid_size)]

coords = [
    [(9, 5), (9, 6)],
    [(5, 8), (5, 9), (5, 10)],
    [(5, 3), (6, 3), (7, 3)],
    [(4, 1), (5, 1), (6, 1), (7, 1)],
    [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)],
]

if __name__ == "__main__":
    ship_tile_amount = 0

    generate_ship()
    generate_grid()

    while ship_tile_amount > 0:
        reader = input("Input coordinates : ")

        if  len(reader) >= 2 and is_valid_coordinate(reader):
            shoot(reader)
            generate_grid()
        else:
            print("Invalid coordinates.")
    else:
        print("GGWP!")

# [!] Things to improve :
# - Store the positions of the ships as a dict key to access when shooting.
# - Use the random position generator from the other script.