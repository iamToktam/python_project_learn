import os
import time
from termcolor import colored
import math
import random
from threading import Thread

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsVerticalWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x

    def hitsHorizontalWall(self, point):
        return round(point[1]) < 0 or round(point[1]) >= self._y

    def hitsWall(self, point):
        return self.hitsVerticalWall(point) or self.hitsHorizontalWall(point)

    def getReflection(self, point):
        return [
            -1 if self.hitsVerticalWall(point) else 1,
            -1 if self.hitsHorizontalWall(point) else 1
        ]

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def go(self):
        max_moves = max(len(scribe.moves) for scribe in self.scribes)
        for i in range(max_moves):
            for scribe in self.scribes:
                threads = []
                if len(scribe.moves) > i:
                    args = scribe.moves[i][1] + [self]
                    threads.append(Thread(target=scribe.moves[i][0], args=args))
                [thread.start() for thread in threads]
                [thread.join() for thread in threads]
            self.print()
            time.sleep(self.framerate)

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
    def __init__(self, canvas, color='red', mark='*', trail='.', pos=(0, 0), framerate=.05, direction=[0, 1]):
        self.canvas = canvas
        self.trail = trail
        self.mark = mark
        self.framerate = framerate
        self.pos = pos
        self.color = color
        self.direction = direction
        self.moves = []  # Initialize the moves attribute

    def setPosition(self, pos):
        self.pos = pos

    def setDegrees(self, degrees):
        radians = (degrees / 180) * math.pi
        self.direction = [math.sin(radians), -math.cos(radians)]

    def bounce(self, pos):
        reflection = self.canvas.getReflection(pos)
        self.direction = [self.direction[0] * reflection[0], self.direction[1] * reflection[1]]

    def forward(self, distance):
        for i in range(distance):
            pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            if self.canvas.hitsWall(pos):
                self.bounce(pos)
                pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            self.draw(pos)

        for i in range(distance):
            self.moves.append((self.forward, [self]))

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, self.color))
        self.canvas.print()
        time.sleep(self.framerate)

class PlotScribe(TerminalScribe):
    def plotX(self, function):
        for x in range(self.canvas._x):
            pos = [x, function(x)]
            if pos[1] and not self.canvas.hitsWall(pos):
                self.draw(pos)

class RobotScribe(TerminalScribe):
    def up(self, distance=1):
        self.direction = [0, -1]
        self.forward(distance)

    def down(self, distance=1):
        self.direction = [0, 1]
        self.forward(distance)

    def right(self, distance=1):
        self.direction = [1, 0]
        self.forward(distance)

    def left(self, distance=1):
        self.direction = [-1, 0]
        self.forward(distance)

    def drawSquare(self, size):
        self.right(size)
        self.down(size)
        self.left(size)
        self.up(size)

class RandomWalkScribe(TerminalScribe):
    def __init__(self, canvas, degrees=135, max_bounces=10, **kwargs):
        super().__init__(canvas, **kwargs)
        self.degrees = degrees
        self.bounces = 0
        self.max_bounces = max_bounces  # Limit the number of bounces

    def randomizeDegreeOrientation(self):
        self.degrees = random.randint(self.degrees - 10, self.degrees + 10)
        self.setDegrees(self.degrees)

    def bounce(self, pos):
        reflection = self.canvas.getReflection(pos)
        if reflection[0] == -1:
            self.degrees = 360 - self.degrees
        if reflection[1] == -1:
            self.degrees = 180 - self.degrees
        self.direction = [
            self.direction[0] * reflection[0],
            self.direction[1] * reflection[1],
        ]
        self.bounces += 1  # Increment bounce count

    def forward(self, distance):
        for i in range(distance):
            if self.bounces >= self.max_bounces:  # Stop after max bounces
                print("Max bounces reached. Stopping random walk.")
                return
            self.randomizeDegreeOrientation()
            super().forward(1)

def sine(x):
    return 5 * math.sin(x / 4) + 15

def cosine(x):
    return 5 * math.cos(x / 4) + 15

# Initialize canvas
canvas = CanvasAxis(30, 30)

# Use the PlotScribe to draw a sine wave
plotScribe = PlotScribe(canvas)
plotScribe.plotX(sine)

# Use the RobotScribe to draw a square
robotScribe = RobotScribe(canvas, color='blue')
robotScribe.drawSquare(10)

# Use the RandomWalkScribe for random bouncing
randomScribe = RandomWalkScribe(canvas, color='green', pos=(0, 0), max_bounces=10)
randomScribe.forward(100)