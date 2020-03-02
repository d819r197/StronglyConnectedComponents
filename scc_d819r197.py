import sys

class Node():
    def __init__(self, n):
        print("Initilzing Node")
        self.id = n
        self.connectedNodes = []

class Graph():
    def __init__(self, nc):
        print("Initilzing Graph")
        self.nodeCount = nc
        self.nodeList = []
        for n in range(self.nodeCount):
            self.nodeList.append(Node(n))

    def printGraph(self):
        print("\n-----------------------------------")
        for node in self.nodeList:
            for cn in node.connectedNodes:
                print("("+str(cn.id)+")->", end='')
            print("\n-----------------------------------")

def importNodes(filePath):
    print("Importing: " + filePath)
    file = open(filePath, "r")
    fileLines = file.readlines()
    graphSize = int(fileLines[0])
    graph = Graph(graphSize)
    nodeIndex = 0

    #Iterate through the lines
    for line in fileLines[2:]:
        currNode = graph.nodeList[nodeIndex]
        nodeConnections = line.split(' ')
        for nc in nodeConnections:
            if nc != " " and nc != "\n":
                print("Connecting " + str(currNode.id+1) + " to " + str(graph.nodeList[int(nc)-1].id+1))
                currNode.connectedNodes.append(graph.nodeList[int(nc)-1])
        nodeIndex += 1

    return graph

def main():
    print("Starting Program")
    g = importNodes(sys.argv[1])
    g.printGraph()

if __name__ == "__main__":
    main()
