"""
Take one of your favorite math formulas and plot it. 
The routine involves creating two lists. 
For example, to draw a circle calculate successive values in a sequence, range(360). 
Convert to radians and the put the math.sin() and math.cos() in their relative lists.
"""

#Creating a Lissajous curve 
import matplotlib.pyplot as plt
from Lab15_class import LissajousParameters

#initialize parameters
parameters = LissajousParameters()

#plot figure
fig, ax = plt.subplots(figsize=(6, 6))

#add plot curve
ax.plot(parameters.x, parameters.y, color='blue')

#label and titles
ax.set_title("Lissajous Curve")
ax.set_xlabel("x(t)")
ax.set_ylabel("y(t)")

#Grid and axis properties, create grid and aspect ratio
ax.grid(True)
ax.axis("equal")

#display
plt.show()