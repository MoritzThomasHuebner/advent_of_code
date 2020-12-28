import numpy as np


class ShipCoordinate(object):

    def __init__(self, x, y, facing_direction=90):
        self.x = x
        self.y = y
        self.facing_direction = facing_direction

    @property
    def facing_direction_rad(self):
        return self.facing_direction / 360 * 2 * np.pi

    @property
    def manhattan_metric(self):
        return np.abs(self.x) + np.abs(self.y)

    def move(self, instruction):
        action, amount = self.parse_instruction(instruction=instruction)
        if action in ['N', 'S']:
            self.move_north_south(direction=action, amount=amount)
        elif action in ['E', 'W']:
            self.move_east_west(direction=action, amount=amount)
        elif action in ['L', 'R']:
            self.move_left_right(direction=action, amount=amount)
        elif action == 'F':
            self.move_forward(amount=amount)

    def move_forward(self, amount):
        self.move_north_south(direction='N', amount=amount*np.cos(self.facing_direction_rad))
        self.move_east_west(direction='E', amount=amount*np.sin(self.facing_direction_rad))

    def move_north_south(self, direction, amount):
        if direction == 'N':
            self.y += amount
        elif direction == 'S':
            self.y -= amount

    def move_east_west(self, direction, amount):
        if direction == 'E':
            self.x += amount
        elif direction == 'W':
            self.x -= amount

    def move_left_right(self, direction, amount):
        if direction == 'L':
            self.facing_direction -= amount
        elif direction == 'R':
            self.facing_direction += amount

    @staticmethod
    def parse_instruction(instruction):
        action = instruction[0]
        amount = int(instruction[1:])
        return action, amount


instructions = []
with open('day_12_input.txt', 'r') as f:
    for i in f.readlines():
        instructions.append(i.strip('\n'))

ship = ShipCoordinate(x=0, y=0, facing_direction=90)
for instruction in instructions:
    ship.move(instruction=instruction)
    print(ship.x)
    print(ship.y)
    print(ship.manhattan_metric)
    print()

# Part 2


class ShipCoordinateWithWayPoint(object):

    def __init__(self, x_ship, y_ship, x_waypoint, y_waypoint):
        self.x_ship = x_ship
        self.y_ship = y_ship
        self.x_waypoint = x_waypoint
        self.y_waypoint = y_waypoint

    @property
    def manhattan_metric(self):
        return np.abs(self.x_ship) + np.abs(self.y_ship)

    def move(self, instruction):
        action, amount = self.parse_instruction(instruction=instruction)
        if action in ['N', 'S']:
            self.move_north_south(direction=action, amount=amount)
        elif action in ['E', 'W']:
            self.move_east_west(direction=action, amount=amount)
        elif action in ['L', 'R']:
            self.move_left_right(direction=action, amount=amount)
        elif action == 'F':
            self.move_forward(amount=amount)

    def move_forward(self, amount):
        self.x_ship += amount * self.x_waypoint
        self.y_ship += amount * self.y_waypoint

    def move_north_south(self, direction, amount):
        if direction == 'N':
            self.y_waypoint += amount
        elif direction == 'S':
            self.y_waypoint -= amount

    def move_east_west(self, direction, amount):
        if direction == 'E':
            self.x_waypoint += amount
        elif direction == 'W':
            self.x_waypoint -= amount

    def move_left_right(self, direction, amount):
        amount_rad = 2 * np.pi * amount / 360
        if direction == 'R':
            amount_rad = -amount_rad
        x_waypoint_new = self.x_waypoint * np.cos(amount_rad) - self.y_waypoint * np.sin(amount_rad)
        y_waypoint_new = self.x_waypoint * np.sin(amount_rad) + self.y_waypoint * np.cos(amount_rad)
        self.x_waypoint = x_waypoint_new
        self.y_waypoint = y_waypoint_new

    @staticmethod
    def parse_instruction(instruction):
        action = instruction[0]
        amount = int(instruction[1:])
        return action, amount


ship = ShipCoordinateWithWayPoint(x_ship=0, y_ship=0, x_waypoint=10, y_waypoint=1)
for instruction in instructions:
    ship.move(instruction=instruction)
    print(ship.x_ship)
    print(ship.y_ship)
    print(ship.x_waypoint)
    print(ship.y_waypoint)
    print(ship.manhattan_metric)
    print()
