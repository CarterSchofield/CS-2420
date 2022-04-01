#graphics calculator

from graphics import *
import math
import stack

def PrintDirections():
    pass

def infixToPostfix(infix):
    #return postfix
    
    postfix = "" #change this to a [] list for double integers 
    s = stack.Stack()
    
    for c in infix:
        #c means character
        if c == 'x':
            postfix += (c)
            print(postfix)
            
        elif c.isdigit():
            #turnintofloat
            #c = float(c)
            #dont really need to make this a float if i'm doing it in EvaluatePostFix
            postfix += (c)
            print(postfix)
        elif c in "+-":
            #correct format
            while not s.isEmpty() and s.top() in "+-*/":
                postfix += s.pop()
            s.push(c)
            print(postfix)
            
        elif c in "*/":
            while not s.isEmpty() and s.top() in "*/":
                    postfix += s.pop()
            s.push(c)
            print(postfix)
            
        elif c == "(":
            s.push(c)
            print(postfix)
        
        elif c == ")":
            while not s.isEmpty() and s.top() != "(":
                postfix += s.pop()
                print(postfix)
            s.pop()
                
            #pop everything until c
        else:
            print("bad character", c)
            print(postfix)
        
        #empty stack
        
    while s.isEmpty() is not True:
        #pop everything until it is empty
            postfix += s.pop()
    return postfix
    
    

def evaluatePostfix(postfix, x):
    ''' go the extra mile and add more supported operators '''
    
    s = stack.Stack()
    ''' need to add a special case for NoneType '''
    
    for c in postfix:
        if c.isdigit():
            s.push(float(c))
        elif c == "x" or c == "X":
            s.push(x)
        elif(not s.isEmpty()):
            if c == "+":
                '''addition'''
                #right variable
                right_variable = s.pop()
                #left variable
                left_variable = s.pop()
                new_variable = left_variable + right_variable 
                s.push(new_variable)
            elif c == "-":
                ''' subtraction '''
                #right variable
                right_variable = s.pop()
                #left variable
                left_variable = s.pop()
                new_variable = left_variable - right_variable 
                s.push(new_variable)
            
            elif c == "*":
                ''' multiplication '''
                #right variable
                right_variable = s.pop()
                #left variable
                left_variable = s.pop()
                new_variable = left_variable * right_variable 
                s.push(new_variable)
                
            elif c == "/":
                ''' division '''
                #right variable
                right_variable = s.pop()
                #left variable
                left_variable = s.pop()
                new_variable = left_variable / right_variable 
                s.push(new_variable)
        
    return s.pop()
            
        

    
def main():
    PrintDirections()
    infix = input("Enter you expression (ex. x*x): ")
    postfix= infixToPostfix(infix)
    
    #generate data
    points = []
    XLOW =  -10
    XHIGH = +10
    YLOW =  -10
    YHIGH = +10
    
    for xx in range(XLOW*10, XHIGH*10+1):
        x = xx/10.0
        #y = x*2 #put equation here
        y = evaluatePostfix(postfix, x)
        p = (x,y)
        points.append(p)
    print(points)
    print(x)
    print(y)
    

    
    #draw the data
    
    win = GraphWin("My Window", 500, 500)
    win.setCoords(XLOW, YLOW, XHIGH, YHIGH)
    for i in range(len(points)-1):
        p1 = points[i]
        x1 = p1[0]
        y1 = p1[1]
        p2 = points[i+1]
        x2 = p2[0]
        y2 = p2[1]
        l = Line(Point(x1, y1), Point(x2, y2))
        l.draw(win)
    win.getMouse()
    win.close()

if __name__ == "__main__":
    
    main()  
    
        
        
    
    
    