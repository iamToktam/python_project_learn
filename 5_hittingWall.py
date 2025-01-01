import os
import time
from termcolor import colored

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[' ' for x in range(width)] for y in range(height)]

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self.width or point[1] < 0 or point[1] >= self.height

    def setPos(self, pos, mark):
        if 0 <= pos[0] < self.width and 0 <= pos[1] < self.height:
            self.canvas[pos[1]][pos[0]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        self.clear()
        for row in self.canvas:
            print(' '.join(row))

class Scribe:
    def __init__(self, name, start_pos, direction, mark='*'):
        self.name = name
        self.pos = start_pos
        self.direction = direction
        self.mark = mark
        self.trail = '.'
        self.moves = {'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]}

    def move(self, canvas):
        new_pos = [self.pos[0] + self.moves[self.direction][0], self.pos[1] + self.moves[self.direction][1]]

        if canvas.hitsWall(new_pos):
            if self.direction == 'left':
                self.direction = 'right'
            elif self.direction == 'right':
                self.direction = 'left'
            elif self.direction == 'up':
                self.direction = 'down'
            elif self.direction == 'down':
                self.direction = 'up'

            # Recompute new_pos after bounce
            new_pos = [self.pos[0] + self.moves[self.direction][0], self.pos[1] + self.moves[self.direction][1]]

        self.draw(canvas, new_pos)

    def _bounce_direction(self):
        if self.direction == 'left':
            return 'right'
        elif self.direction == 'right':
            return 'left'
        elif self.direction == 'up':
            return 'down'
        elif self.direction == 'down':
            return 'up'

    def draw(self, canvas, new_pos):
        canvas.setPos(self.pos, self.trail)
        self.pos = new_pos
        canvas.setPos(self.pos, colored(self.mark, 'red'))
        canvas.display()
        time.sleep(0.5)

def create_and_move_scribes(canvas, scribes_data):
    scribes = [Scribe(data['name'], data['start_pos'], data['direction']) for data in scribes_data]
    for _ in range(50):  # Number of moves, can be adjusted
        for scribe in scribes:
            scribe.move(canvas)

canvas = Canvas(30, 30)
scribes_data = [
    {'name': 'Scribe1', 'start_pos': [0, 0], 'direction': 'right'},
    {'name': 'Scribe2', 'start_pos': [10, 10], 'direction': 'down'},
    {'name': 'Scribe3', 'start_pos': [20, 20], 'direction': 'left'},
]

create_and_move_scribes(canvas, scribes_data)

