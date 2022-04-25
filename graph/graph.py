from queue import Empty
import queue

class Graph:
    def __init__(self, numVertices):
        self.mNeighbors = []
        for i in numVertices:
            self.mNeighbors.append([])

    def addEdge(self, v0, v1):
        self.mNeighbors[v0].append(v1)

    def getNeighbors(self, v):
        pass

    def isEdge(self, v0, v1):
        pass

    def findPath(self, v0, v1):
        Q = queue.Queue()
        xfrom = [-1] * len(self.mNeighbors)
        xfrom [v0] = v0
        Q.enqueue(v0)
        while Q is not Empty:
            c = Q.dequeue()
            if c == v1:
                pass
                #build path and return it
            for n in self.mNeighbors[c]:
                pass
                #if n not vistited 
                    #enqueue n
                    #make that n was vistited from c
        return None


    

