import stack
import graphics
import math

def print_directions():
    pass

def main():
    print_directions()
    infix = input("Enter your expression here: ")
    #Generate the data
    point = []
    xLow = -10
    xHigh = 10
    yLow = -10
    yHigh = 10

    for xx in range(xLow*10, xHigh*10 +1):
        x = xx/10.0
        y = x * x # <=== Put equation here
        p = (x,y)
        points.append(p)
    print(points)

    #Draw the data
    win = GraphWin("My Circle", 500, 500)
    win.setCoords(xLow, yLow, xHigh, yHigh)
    for i in range(len(points)-1):
        p1 = points[i]
        x1 = p1[0]
        y1 = p1[1]
        p2 = points[i+1]
        x2 = p2[0]
        y2 = p2[1]
        l = Line(Point(x1,y1), Point(x2, y2))
        l.draw(win)
    win.getMouse() # Pause to view results
    win.close() # Close window when done

main()