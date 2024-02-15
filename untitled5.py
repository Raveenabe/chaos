import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

# Define the parameter range for 'r'
r_values = np.linspace(2.5, 4.0, 10000)

# Number of iterations for each r value
num_iterations = 1000

# Number of iterations to skip before plotting
skip_iterations = 100

# Arrays to store r values and corresponding x values
r_vals = []
x_vals = []

x = 0.5  # Initial condition

for r in r_values:
    for _ in range(num_iterations):
        x = logistic_map(r, x)

    for _ in range(skip_iterations):
        x = logistic_map(r, x)
        r_vals.append(r)
        x_vals.append(x)

plt.figure(figsize=(10, 6))
plt.plot(r_vals, x_vals, ',k', alpha=0.25)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.title("Bifurcation Diagram of the Logistic Map", fontsize=16)
plt.xlabel("The Growth Rate (r)", fontsize=14)
plt.ylabel("Population (Xn)", fontsize=14)
plt.grid(True)
plt.show()
