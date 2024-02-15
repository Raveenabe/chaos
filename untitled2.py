import matplotlib.pyplot as plt
import numpy as np

Iterations = 200
Initial_x = 1
growth_rate = 3.9
X=[]
It=[]
z_1 = []
z_2 = []
X = [Initial_x]
It = [1]

for growth_rate in np.arange (1,4,0.1): 
 for n in range (1,Iterations):
  y = growth_rate*X[n-1]*(1-X[n-1])
  X.append(y)
  It.append(n+1)
  
 z_1.append(growth_rate)
 z_2.append(X[-1])
 X = [Initial_x]

plt.scatter(z_1, z_2, color = 'red');
plt.plot(It, X, color = 'blue');
plt.xlabel('Number of Iterations')
plt.ylabel('Population')
plt.title('Population Vs Iterations')
plt.show()