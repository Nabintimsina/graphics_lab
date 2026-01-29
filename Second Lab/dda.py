
def LineDraw(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))

    xinc = dx / steps
    yinc = dy / steps

    x = x1
    y = y1

    i = 0
    for i in range(steps):
        x= round(x)
        y= round(y)
        i = i + 1
        print(f"({x}, {y})")
        x = x + xinc
        y = y + yinc


LineDraw(10, 8, 18, 15)


