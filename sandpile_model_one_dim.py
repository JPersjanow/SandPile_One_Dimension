import numpy as np
import matplotlib.pyplot as plt
from datetime import date

today = date.today()
date = today.strftime("%b-%d-%Y")
print("date =", date)

N = 100
E = 0.1
critical_slope = 5
n_iter = 200000
filename = "Sandpile_Plot_OneDimension_{}_{}\n".format(date,n_iter)

file = open(filename, "w+")
file.write("Number of iterations: {}".format(n_iter))
sand = np.zeros(N)
tsav = np.zeros(n_iter)
mass = np.zeros(n_iter)

for iterate in range(0, n_iter):
    move = np.zeros(N)

    for j in range(0, N-1):
        slope = abs(sand[j+1] - sand[j])
        if slope >= critical_slope:
            avrg = (sand[j] + sand[j+1])/2.
            move[j] += (avrg - sand[j])/2.
            move[j+1] += (avrg - sand[j+1])/2.
            tsav[iterate] += slope/4

    if tsav[iterate] > 0:
        sand += move
    else:
        j = np.random.random_integers(0,N-1)
        sand[j] += np.random.uniform(0, E)

    sand[N-1] = 0.
    mass[iterate] = np.sum(sand)

    output = "{0} mass {1}\n".format(iterate, mass[iterate])
    file.write(output)
    print(output)

plt.subplot(2,1,1)
plt.plot(range(0,n_iter), mass)
plt.ylabel('Sanpile Mass')
plt.subplot(2,1,2)
plt.plot(range(0, n_iter), tsav)
plt.ylabel('Displaced Mass')
plt.xlabel('Iteration')
plt.show()

file.close()