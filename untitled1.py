import matplotlib.pyplot as plt

Iterations = 120
Initial_x = 0.7
growth_rate = 3.4
X=[]
It=[]
X = [Initial_x]
It = [1]

for n in range (1,Iterations):
    y = growth_rate*X[n-1]*(1-X[n-1])
    X.append(y)
    It.append(n+1)

plt.scatter(It, X, color = 'red');
plt.plot(It, X, color = 'blue');
plt.xticks(fontsize=12)
plt.yticks(fontsize=11)
plt.xlabel('Number of Iterations', fontsize=14)
plt.ylabel('Population', fontsize=14)
plt.title('Population Vs Iterations - Quadratic Map', fontsize=16)
plt.show()

# a1, a2, a3, ... are stabalize states of population
a1 = X[Iterations-1]
a2 = X[Iterations-2]
a3 = X[Iterations-3]
a4 = X[Iterations-4]
a5 = X[Iterations-5]
a6 = X[Iterations-6]
a7 = X[Iterations-7]
a8 = X[Iterations-8]
