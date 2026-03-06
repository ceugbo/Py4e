import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([13, 15, 20, 30])

line_style = dict(marker=None,
                    linestyle="solid",
                    linewidth=2)

plt.title("Class Size",
          fontsize=20,
          family="Arial",
          fontweight="bold",
          color="#4248ff")
plt.xlabel("Year", fontsize=16,
          family="Arial",
          fontweight="bold",
          color="#2dbefc")
plt.ylabel("Students", fontsize=16,
          family="Arial",
          fontweight="bold",
          color="#2dbefc")

# plt.tick_params(axis="both", colors="#2dbefc")

plt.grid(linestyle="dashed",
         color="lightgray",
         linewidth=1.5)

plt.plot(x, y1, **line_style, color="#fa0202")
plt.plot(x, y2, **line_style, color="#1cd3fc")
plt.plot(x, y3, **line_style, color="#fcbf49")

plt.xticks(x)

plt.show()