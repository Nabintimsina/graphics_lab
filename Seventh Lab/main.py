import numpy as np

import matplotlib.pyplot as mp


theta = 30
rad = np.radians(theta)

x1 = 4
y1 = 5
z1 = 3

x2 = 100
y2 = 67
z2 = 67

sx = 2
sy = 2
sz = 1


tx = 1
ty = 2
tz = 1


input1M = np.array([[x1],[y1], [z1], [1]])
input2M = np.array([[x2],[y2], [z2], [1]])


rotationM = np.array([[1, 0, 0, 0],[0, np.cos(rad), - np.sin(rad), 0 ],[0, np.sin(rad), np.cos(rad), 0 ], [0, 0, 0, 1 ]])
scalingM = np.array([[sx, 0, 0, 0], [0, sy, 0,0], [0, 0, sz,0], [0, 0, 0, 1]])
translationM = np.array([[1, 0, 0 , tx], [0, 1, 0, ty], [0, 0, 1, tz],[0, 0, 0, 1]])



# rotation about x axis
output1RM = np.round(rotationM@input1M, 2 )
output1SM = scalingM@input1M
output1TM = translationM @ input1M

output2RM = np.round(rotationM@input2M, 2 )
output2SM = scalingM@input2M
output2TM = translationM @ input2M

