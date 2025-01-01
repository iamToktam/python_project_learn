import os
import time
import math
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
        self.mark = '*'
        self.framerate = 0.05  # Adjust speed of animation
        self.pos = [canvas.width // 2, canvas.height // 2]  # Start at the canvas center

    def draw_line(self, angle, steps):
        """Draws a single continuous line."""
        rad = math.radians(angle)  # Convert the angle to radians

        for _ in range(steps):
            # Calculate the next position
            next_x = self.pos[0] + round(math.cos(rad))
            next_y = self.pos[1] + round(math.sin(rad))  # Add for downward y-direction

            # Stop if the next position hits the wall
            if self.canvas.hitsWall((next_x, next_y)):
                break

            # Draw the mark at the current position
            self.canvas.setPos(self.pos, colored(self.mark, 'red'))
            self.pos = [next_x, next_y]  # Update the position

            # Display the canvas
            self.canvas.display()
            time.sleep(self.framerate)

# Initialize the canvas and scribe
canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)

# Draw the line at a 45° downward angle
scribe.draw_line(45, 20)  # Adjust the steps to control the line length
