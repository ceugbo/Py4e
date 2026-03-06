import matplotlib.pyplot as plt
import numpy as np

categories = ["Grains", "Fruits", "Vegetables", "Proteins", "Dairy", "Sweets"]
values = np.array([4, 3, 2, 5, 3, 1])

def barchart(cat, val):
    plt.bar(cat, val, color="red")
    # plt.barh(categories, values, color="skyblue")
    plt.title("Daily Consumption", fontsize=20, fontweight="bold", color="#4248ff")
    plt.tick_params(axis="both", labelcolor="#2dbefc", labelsize=10)
    plt.xlabel("Food", fontsize=14, fontweight="bold", color="#2dbefc")
    plt.ylabel("Quantity", fontsize=14, fontweight="bold", color="#2dbefc")
    plt.show()
# barchart(categories, values)

cat = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
val = np.array([300, 250, 275, 225])
colors = ["purple", "orange", "blue", "green"]

def piechart(cat, val, colors):
    plt.pie(val, 
            labels=cat, 
            autopct="%1.1f%%", 
            colors=colors,
            explode=[0.05, 0.01, 0.01, 0.01],
            startangle=90)
    plt.title("ceugbo College", fontsize=20, fontweight="bold", color="#4248ff")
    plt.show()
# piechart(categories, values, colors)

#Scatter Plot
x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])
y1 = np.array([55, 60, 62, 70, 70, 75, 78, 78, 80, 82, 85])

x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8])
y2 = np.array([50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97])

def scatterplot(x1, y1, x2, y2):
    plt.scatter(x1, y1, color="#fa0202",
                s = 60,
                label="Class A")

    plt.scatter(x2, y2, color="#fcbf49",
                s = 60,
                label="Class B")

    plt.title("Test Scores", fontsize=20, fontweight="bold", color="#4248ff")
    plt.xlabel("Hour Studied", fontweight="bold", color="#2dbefc")
    plt.ylabel("Scores Obtained", fontweight="bold", color="#2dbefc")

    plt.legend()
    plt.show()
# scatterplot(x1, y1, x2, y2)


#Histogram

scores = np.random.normal(loc=60, scale=10, size=100)
scores = np.clip(scores, 0, 100)

def histogram(scores):
    plt.hist(scores, bins=10, color="#fcbf49", edgecolor="white")
    plt.title("Exam Scores", fontweight="bold", fontsize=20, color="#4248ff")
    plt.xlabel("Score", fontweight="bold", color="#2dbefc")
    plt.ylabel("No of Students", fontweight="bold", color="#2dbefc")

    plt.show()
# histogram(scores)


def barchart(ax, cat, val):
    ax.bar(cat, val, color="red")
    # plt.barh(categories, values, color="skyblue")
    ax.set_title("Daily Consumption", fontsize=20, fontweight="bold", color="#4248ff")
    ax.tick_params(axis="both", labelcolor="#2dbefc", labelsize=10)
    ax.set_xlabel("Food", fontsize=14, fontweight="bold", color="#2dbefc")
    ax.set_ylabel("Quantity", fontsize=14, fontweight="bold", color="#2dbefc")
    # ax.show()
# barchart(categories, values)

cat = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
val = np.array([300, 250, 275, 225])
colors = ["purple", "orange", "blue", "green"]

def piechart(ax, cat, val, colors):
    ax.pie(val, 
            labels=cat, 
            autopct="%1.1f%%", 
            colors=colors,
            explode=[0.05, 0.01, 0.01, 0.01],
            startangle=90)
    ax.set_title("ceugbo College", fontsize=20, fontweight="bold", color="#4248ff")
    # ax.show()
# piechart(categories, values, colors)

#Scatter Plot
x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])
y1 = np.array([55, 60, 62, 70, 70, 75, 78, 78, 80, 82, 85])

x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8])
y2 = np.array([50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97])

def scatterplot(ax, x1, y1, x2, y2):
    ax.scatter(x1, y1, color="#fa0202",
                s = 60,
                label="Class A")

    ax.scatter(x2, y2, color="#fcbf49",
                s = 60,
                label="Class B")

    ax.set_title("Test Scores", fontsize=20, fontweight="bold", color="#4248ff")
    ax.set_xlabel("Hour Studied", fontweight="bold", color="#2dbefc")
    ax.set_ylabel("Scores Obtained", fontweight="bold", color="#2dbefc")

    ax.legend()
    # ax.show()
# scatterplot(x1, y1, x2, y2)


#Histogram

scores = np.random.normal(loc=60, scale=10, size=100)
scores = np.clip(scores, 0, 100)

def histogram(ax, scores):
    ax.hist(scores, bins=10, color="#fcbf49", edgecolor="white")
    ax.set_title("Exam Scores", fontweight="bold", fontsize=20, color="#4248ff")
    ax.set_xlabel("Score", fontweight="bold", color="#2dbefc")
    ax.set_ylabel("No of Students", fontweight="bold", color="#2dbefc")

    # ax.show()
# histogram(scores)

figure, axs = plt.subplots(2, 2)
barchart(axs[0, 0], categories, values)
piechart(axs[0, 1], cat, val, colors)
scatterplot(axs[1, 0], x1, y1, x2, y2)
histogram(axs[1, 1], scores)

figure.tight_layout()
figure.savefig("subplots.png")