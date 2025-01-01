import os
import time

class Canvas:
    def __init__(self, size):
        self.size = size
        self.canvas = [[' ' for _ in range(size + 1)] for _ in range(size + 1)]

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_square(self):
        # Draw the border of the square
        for x in range(self.size + 1):
            self.canvas[0][x] = '.'  # Top border
            self.canvas[self.size][x] = '.'  # Bottom border
        for y in range(self.size + 1):
            self.canvas[y][0] = '.'  # Left border
            self.canvas[y][self.size] = '.'  # Right border

    def set_point(self, x, y, char):
        if 0 <= x <= self.size and 0 <= y <= self.size:
            self.canvas[y][x] = char

    def render(self):
        self.clear()
        for row in self.canvas:
            print(''.join(row))

class MovingMarker:
    def __init__(self, canvas, start_x, start_y, marker='*', trail='.'):
        self.canvas = canvas
        self.x = start_x
        self.y = start_y
        self.marker = marker
        self.trail = trail

    def move_diagonal(self, steps):
        for _ in range(steps):
            # Leave a trail
            self.canvas.set_point(self.x, self.y, self.trail)

            # Update position
            self.x += 1
            self.y += 1

            # Draw the marker
            self.canvas.set_point(self.x, self.y, self.marker)

            # Render the canvas
            self.canvas.render()
            time.sleep(0.2)

# Initialize canvas and marker
canvas = Canvas(size=20)
canvas.draw_square()
canvas.render()  # Render the square first

time.sleep(1)  # Pause for visual clarity

# Now move the marker diagonally
marker = MovingMarker(canvas, start_x=0, start_y=0)
marker.move_diagonal(steps=15)
