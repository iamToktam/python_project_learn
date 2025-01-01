import os
import time
from termcolor import colored

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self.width or point[1] < 0 or point[1] >= self.height

    def setPos(self, pos, mark):
        self.canvas[pos[1]][pos[0]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        self.clear()
        for row in self.canvas:
            print(' '.join(row))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.1
        self.pos = [0, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1] - 1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1] + 1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0] - 1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0] + 1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)  # Leave a trail
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.display()
        time.sleep(self.framerate)

    def drawSquare(self, size):
        # Set starting position in the center of the canvas
        self.pos = [self.canvas.width // 2 - size // 2, self.canvas.height // 2 - size // 2]

        # Draw the top side
        for _ in range(size):
            self.right()

        # Draw the right side
        for _ in range(size):
            self.down()

        # Draw the bottom side
        for _ in range(size):
            self.left()

        # Draw the left side
        for _ in range(size):
            self.up()

# Initialize the canvas and scribe
canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)

# Draw a square dynamically
scribe.drawSquare(10)

