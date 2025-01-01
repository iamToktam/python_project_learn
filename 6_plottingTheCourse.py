# Terminal-based sine wave display
import math

# Configuration for the sine waves

width = 80  # Number of columns for horizontal resolution

height = 20  # Number of rows for vertical resolution

x_range = 4 * math.pi  # Range for x (0 to 4π)

step = x_range / width  # Step size



# Create a grid for the sine waves

wave = [[" " for _ in range(width)] for _ in range(height)]

for col in range(width):

    x = col * step  # Calculate x value



    # First sine wave

    y1 = math.sin(x)

    row1 = int((y1 + 1) / 2 * (height - 1))

    wave[row1][col] = "."  # Mark the first sine wave with '*'



    # Second sine wave (shifted)

    y2 = math.sin(x + math.pi / 2)

    row2 = int((y2 + 1) / 2 * (height - 1))

    wave[row2][col] = "."  # Mark the second sine wave with '*'



# Print the sine waves

for row in wave:

    print("".join(row))
