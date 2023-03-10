import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([10, 11, 12, 13, 14, 15])
ypoints = np.array([53, 52, 60, 63, 72, 70])

w1 = 2
w2 = 0
loss = sum((ypoints-xpoints*w1 - w2)**2)/6
print(loss)
i = 0

y_pred = w1*xpoints + w2

fig, axs = plt.subplots(2)
axs[0].scatter(xpoints, ypoints)
axs[0].plot(xpoints, y_pred)
#axs[0].draw()
fig.xlabel('x-points')
fig.ylabel('y-points')
axs[0].pause(0.01)
axs[0].clf()

for i in range(600):
    y_pred = w1*xpoints + w2

    axs[0].scatter(xpoints, ypoints)
    axs[0].plot(xpoints, y_pred)
    #axs[0].draw()
    fig.xlabel('x-points')
    fig.ylabel('y-points')
    axs[0].pause(0.01)
    axs[0].clf()
    
    k1 = sum(2*(ypoints-w1*xpoints - w2)*(-xpoints))
    k2 = sum(-2*(ypoints-w1*xpoints - w2))
    
    if(k1 > 0):
        w1 -= 0.01
    elif(k1 < 0):
        w1 += 0.01
    
    if(k2 > 0):
        w2 -= 0.01
    elif(k2 < 0):
        w2 += 0.01

plt.scatter(xpoints, ypoints)
plt.plot(xpoints, y_pred)
plt.draw()
plt.xlabel('x-points')
plt.ylabel('y-points')
plt.show()
print(w1, w2, sum((ypoints-xpoints*w1 - w2)**2))