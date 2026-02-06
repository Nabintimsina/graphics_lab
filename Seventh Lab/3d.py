# from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as mp
import numpy as np

theta = 30
rad = np.radians(theta)

x1 = 3
y1 = 3
z1 = 3

x2 = 70
y2 = 70
z2 = 70

sx = 2
sy = 2
sz = 1


tx = 1
ty = 2
tz = 1


input1M = np.array([[x1],[y1], [z1], [1]])
input2M = np.array([[x2],[y2], [z2], [1]])


rotationM = np.array([[1, 0, 0, 0],[0, np.cos(rad), - np.sin(rad), 0 ],[0, np.sin(rad), np.cos(rad), 0 ], [0, 0, 0, 1 ]])


# rotation about x axis
output1RM = np.round(rotationM@input1M, 2 )

output2RM = np.round(rotationM@input2M, 2 )


# Extract x, y, z (ignore homogeneous coord)
pR1 = output1RM[:3].flatten()
pR2 = output2RM[:3].flatten()

p1 = input1M[:3].flatten()
p2 = input2M[:3].flatten()

fig = mp.figure()
ax = fig.add_subplot(111, projection='3d')

# Draw line between the two points
ax.plot(
    [p1[0], p2[0]],
    [p1[1], p2[1]],
    [p1[2], p2[2]],
    marker='o'
)

ax.plot(
    [pR1[0], pR2[0]],
    [pR1[1], pR2[1]],
    [pR1[2], pR2[2]],
    marker='o'
)



ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

mp.show()
