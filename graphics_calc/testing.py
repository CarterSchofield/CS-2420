import graphics

def main():
    win = GraphWin("My Circle")
    c = Circle(Point(50,50),10)
    c.draw(win)
    win.getMouse()
    win.close()

main()