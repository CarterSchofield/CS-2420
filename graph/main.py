import graph

def main():
    f = open("data.txt")
    numV = int(f.readline())
    G = graph.Graph(numV)
    numE = int(f.readline())
    for i in range(numE):
        line = f.readline()
        words = line.split()
        v0 = int(words[0])
        v1 = int(words[1])
        G.addEdge(v0, v1)
    numT = int(f.readline())
    for i in range(numT):
        line = f.readline()
        words = line.split()
        v0 = int(words[0])
        v1 = int(words[1])
        G.findPath(v0, v1)

if __name__ == "__main__":
    main()