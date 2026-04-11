import matplotlib.pyplot as plt
import numpy as np

#Inputting the data points and parameters
m = int(input("Enter the number of data points: "))
test_times = int(input("How many values of w and b do you want to test(Note that the first value of w and b\nwill be computed as the accurate parameters and the rest as the test parameters)? "))

#Declaring the lists to store the values of w, b, x and y
w = []
b = []
x = []
y = []

#Colours for scatter plot
colors = [
    '#fa0202',  # red
    '#fcbf49',  # warm yellow
    '#90be6d',  # green
    '#eae2b7',  # light cream
    '#43aa8b',  # teal green
    '#4d908e',  # muted teal
    '#577590',  # blue-grey
    '#277da1',  # blue
    '#9d4edd',  # purple
    '#f72585'   # pink
]

#Inputting the values of w, b and x
for i in range(test_times):
    w_in = float(input(f"Enter w[{i}]: ").strip())
    b_in = float(input(f"Enter b[{i}]: ").strip())
    w.append(w_in)
    b.append(b_in)
    
for j in range(m):
        x_in = float(input(f"Enter x[{j}]: ").strip())
        x.append(x_in)

#Computing the values of y for each value of w and b
for k in range(test_times):
    for i in range(len(x)):
        x_in = x[i]
        y_compute = w[k] * x_in + b[k]
        y.append(y_compute)

x = np.array(x)
y = np.array(y)

# print(x, y[:2])

# j_w_b = 
# f"j_w_b[{i}]"

#Splitting the values of y into parts according to the number of test parameters and computing the cost function for each part
parts = np.array_split(y, test_times)
j_w_b = []

#Calculating the cost function for each value of w and b
for i in range(test_times):
    j_w_b.append(sum(((x * w[i] + b[i]) - parts[0]) ** 2)*0.5/m)

for i in range(test_times):
    plt.figure()
    plt.plot(x, parts[i], color=colors[i],
                    label=f"w={w[i]} b={b[i]}")

    
    plt.xlabel("X", fontweight="bold", color="#2dbefc")
    plt.ylabel(f"y for values of w{i} and b{i}", fontweight="bold", color="#2dbefc")
    plt.title(f"ML Model X against y{i}", fontsize=20, fontweight="bold", color="#4248ff")

    plt.legend()
    plt.savefig(f"regress{i}")
    plt.close()

plt.plot(w, j_w_b, color="#fcbf49",
                    label="Jwb, w")

    
plt.xlabel("X", fontweight="bold", color="#2dbefc")
plt.ylabel("Jwb", fontweight="bold", color="#2dbefc")
plt.title("Cost Function", fontsize=20, fontweight="bold", color="#fa0202")

plt.legend()
plt.savefig("cost_function")
plt.close()