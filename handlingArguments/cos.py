import os
import time
from termcolor import colored
import math

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsVerticalWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x

    def hitsHorizontalWall(self, point):
        return round(point[1]) < 0 or round(point[1]) >= self._y

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(''.join([col[y] for col in self._canvas]))

class CanvasAxis(Canvas):
    def formatAxisNumber(self, num):
        if num % 5 != 0:
            return ' '
        if num < 10:
            return ' ' + str(num)
        return str(num)

    def print(self):
        self.clear()
        for y in range(self._y):
            print(self.formatAxisNumber(y) + ' '.join([col[y] for col in self._canvas]))

        print(' '.join([self.formatAxisNumber(x) for x in range(self._x)]))

class TerminalScribe:
    def __init__(self, canvas, color='blue', mark='*', trail='.', pos=(0, 0), framerate=.05):
        self.canvas = canvas
        self.trail = trail
        self.mark = mark
        self.framerate = framerate
        self.pos = pos
        self.color = color

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)  # Leave a trail at the current position
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, self.color))  # Move the marker
        self.canvas.print()
        time.sleep(self.framerate)

class PlotScribe(TerminalScribe):
    def walkCosine(self, function, steps):
        for x in range(steps):
            y = function(x)  # Get the y-value for the cosine wave
            if 0 <= round(y) < self.canvas._y:  # Ensure y is within canvas bounds
                self.draw((x, round(y)))

# Define the cosine function
def cosine(x):
    return 5 * math.cos(x / 4) + 15  # Adjusted cosine wave to fit the canvas

# Initialize the canvas and scribe
canvas = CanvasAxis(30, 30)  # A 30x30 canvas
scribe = PlotScribe(canvas, color='blue', mark='*', trail='.')

# Walk along the cosine wave
scribe.walkCosine(cosine, steps=30)  # Walk 30 steps along the cosine wave
