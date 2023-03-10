import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


xpoints = np.array([10, 11, 12, 13, 14, 15]).reshape(-1, 1)
ypoints = np.array([53, 52, 60, 63, 72, 70])


linreg = LinearRegression()
linreg.fit(xpoints, ypoints)

y_pred = linreg.predict(xpoints)

plt.scatter(xpoints, ypoints)
plt.plot(xpoints, y_pred)
plt.xlabel('x-points')
plt.ylabel('y-points')
plt.show()


print(linreg.coef_)
print(linreg.intercept_)


x_new = np.array([16]).reshape(-1, 1)
y_new = linreg.predict(x_new)
print(y_new)

linreg.score(xpoints, ypoints)
