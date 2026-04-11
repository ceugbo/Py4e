import matplotlib.pyplot as plt

def LinePlot(x, y, colour, labelx, labely, filename, plot_title):
    line_style = dict(marker=None,
                        linestyle="solid",
                        linewidth=2)

    plt.title(plot_title,
              fontsize=20,
              fontfamily="DejaVu Sans",
              fontweight="bold",
              color="black")
    plt.xlabel(labelx, fontsize=16,
              fontfamily="DejaVu Sans",
              fontweight="bold",
              color="#2ecc71")
    plt.ylabel(labely, fontsize=16,
              fontfamily="DejaVu Sans",
              fontweight="bold",
              color="#2ecc71")

    plt.tick_params(axis="both", colors="dimgray")
    plt.yticks(range(50, 101, 10))
    plt.ylim(50, 100)

    plt.grid(linestyle="dashed",
             color="lightgray",
             linewidth=1.5)
    plt.plot(x, y, color=colour)
    plt.savefig(filename)

#BarChart
def BarChart(x, y, colour, labelx, labely, filename, plot_title):
    plt.bar(x, y, color=colour)
    # plt.barh(categories, values, color="skyblue")
    plt.title(plot_title, fontsize=20, fontweight="bold", color="#4248ff")
    plt.tick_params(axis="both", labelcolor="#2dbefc", labelsize=10)
    plt.xlabel(labelx, fontsize=14, fontweight="bold", color="#2dbefc")
    plt.ylabel(labely, fontsize=14, fontweight="bold", color="#2dbefc")
    plt.plot()
    plt.savefig(filename)

#Histogram
def histogram(scores, colour, labelx, labely, filename, plot_title):
    if colour == "":
        colour = "#fcbf49"
    else:
        colour = colour
    plt.hist(scores, bins=10, color=colour, edgecolor="white")
    plt.title(plot_title, fontweight="bold", fontsize=20, color="#4248ff")
    plt.xlabel(labelx, fontweight="bold", color="#2dbefc")
    plt.ylabel(labely, fontweight="bold", color="#2dbefc")
    plt.savefig(filename)

# LinePlot(x, y)

# plt.plot(x, y1, **line_style, color="#fa0202")
# plt.plot(x, y2, **line_style, color="#1cd3fc")
# plt.plot(x, y3, **line_style, color="#fcbf49")

# plt.xticks(x)

# plt.show()