# stack class

class Stack:
    
    def __init__(self):
        self.A = []
        self.size = 0
    
    def push(self, x):
        #adds to the top of stack
        self.A.append(x)
        self.size += 1
    
    def pop(self):
        #returns and removes from top of stack
        if self.isEmpty():
            return None
        else:
            self.size -= 1
            return self.A.pop()
        
    
    def top(self):
        #return whats on top of stack
        if self.isEmpty():
            return None
        else:
            return self.A[-1]
        
    def isEmpty(self):
        # .empty is a built in python function that will return a boolean - Doesn't work
        if self.size == 0:
            return True
        else:
            return False
            
    