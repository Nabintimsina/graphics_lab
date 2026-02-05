import numpy as np


theta = 30
rad = np.radians(theta)

x = 4
y = 5
z = 3

sx = 2
sy = 2
sz = 1


tx = 1
ty = 2
tz = 1


inputM = np.array([[x],[y], [z], [1]])


rotationM = np.array([[1, 0, 0, 0],[0, np.cos(rad), - np.sin(rad), 0 ],[0, np.sin(rad), np.cos(rad), 0 ], [0, 0, 0, 1 ]])
scalingM = np.array([[sx, 0, 0, 0], [0, sy, 0,0], [0, 0, sz,0], [0, 0, 0, 1]])
translationM = np.array([[1, 0, 0 , tx], [0, 1, 0, ty], [0, 0, 1, tz],[0, 0, 0, 1]])



# rotation about x axis
outputRM = np.round(rotationM@inputM, 2 )
outputSM = scalingM@inputM
outputTM = translationM @ inputM





print("Rotation about x axis: ")
print(outputRM)

print("Scaling: \n")
print(outputSM)


print("Translation: \n")
print(outputTM)
