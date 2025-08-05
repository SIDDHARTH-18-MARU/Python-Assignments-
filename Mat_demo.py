import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Get all available styles and pick 10
styles = plt.style.available[:10]

# Display plots with different styles
for style in styles:
    plt.style.use(style)
    plt.figure()
    plt.plot(x, y, label=f"Style: {style}")
    plt.title(f"Matplotlib Style: {style}")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)

# Show all plots
plt.show()
