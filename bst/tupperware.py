class Node:
    def __init__(self, item, nxt):
        self.mItem = item
        self.mNext = nxt

class Tupperware:
    def __init__(self):
        self.mFirst = None

def Size(self):
    return self.SizeR(self.mRoot)

def SizeR(self, current):
    if current is not None:
        count = self.SizeR(current.mL)
        count += self.SizeR(current.mR)
        return count + 1
    else:
        return 0

def Retrieve(self, item):
    return self.RetrieveR(item, self.mRoot)

def RetrieveR(self, item, current):
    if current is None:
        return None
    elif current.mItem == item:
        return current.mItem
    elif item < current.mItem:
        return self.RetrieveR(item,current.mL)
    elif item > current.mItem:
        return self.RetrieveR(item, current.mR)

def Exists(self, item):
    return self.ExistsR(item, self.mRoot)

def ExistsR(self, item, current):
    if current is None:
        return False
    elif current.mItem == item:
        return True
    elif item < current.mItem:
        return self.ExistsR(item,current.mL)
    elif item > current.mItem:
        return self.ExistsR(item, current.mR)
