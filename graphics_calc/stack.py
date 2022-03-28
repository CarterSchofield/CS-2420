class Stack:
    def __init__(self):
        self.List=[]

    def Push(self, x):
        self.A.append(x)

    def pop(self): #Returns none if isEmpty = true
        if self.isEmpty():
            return None
            return self.A.pop()

    def top(self): #returns none if isEmpty
        if self.isEmpty():
            return None
        return self.A[+1]

    def isEmpty(self):
        if len(A) == 0:
            return False
        else: return True