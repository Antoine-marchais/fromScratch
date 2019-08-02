from graphics import *
import matplotlib.pyplot as plt
import numpy as np

X=np.linspace(-1,1,100)
Y=2*X
fig = plt.figure()
ax = fig.add_subplot(111)
cv = Canvas(ax)

def inBall(point):
    if np.sqrt(np.sum((point-np.array([0.5,0.5]))**2))<0.2:
        return True

cv.fillIf(inBall)
plt.show()
