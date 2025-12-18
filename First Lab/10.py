import math

def rotate_coordinate(x, y, degrees):
  
    radians = math.radians(degrees)
    cos_theta = math.cos(radians)
    sin_theta = math.sin(radians)

    x_rot = x * cos_theta - y * sin_theta
    y_rot = x * sin_theta + y * cos_theta

    return (x_rot, y_rot)

    
original_x, original_y = 10, 0
angle = 45
new_x, new_y = rotate_coordinate(original_x, original_y, angle)

print(f"Original: ({original_x}, {original_y})")
print(f"Rotated: ({new_x}, {new_y})")
    
    
    