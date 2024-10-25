import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis("off")  # Hide the axes for a cleaner look

# Generate a grid of points
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Create an initial frame for the animation
Z = np.sin(10 * np.sqrt(X**2 + Y**2))

# Initialize a 'heatmap' plot with psychedelic colors
img = ax.imshow(Z, cmap="twilight_shifted", interpolation="bilinear", extent=(-2, 2, -2, 2))

# Update function for each frame
def update(frame):
    Z = np.sin(10 * np.sqrt(X**2 + Y**2) - frame * 0.1) * np.cos(10 * np.arctan2(Y, X) + frame * 0.1)
    img.set_array(Z)
    return [img]

# Create the animation
anim = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
