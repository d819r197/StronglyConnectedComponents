import sys

verbose = True

class Node():
    def __init__(self, n):
        global verbose
        if verbose: print("Initilzing Node")
        self.id = n
        self.connectedNodes = []

class Graph():
    def __init__(self, nc):
        global verbose
        if verbose: print("Initilzing Graph")
        self.nodeCount = nc
        self.nodeList = []
        self.discovered = []
        for n in range(self.nodeCount):
            self.nodeList.append(Node(n))
            self.discovered.append(False)

    def printGraph(self):
        print("\n-----------------------------------")
        for node in self.nodeList:
            for cn in node.connectedNodes:
                print("("+str(cn.id+1)+") ", end='')
            print("\n-----------------------------------")

    def bfs(self, initNode):
        global verbose

        if verbose: print("starting dfs")

        #Initialize Discover List
        if verbose: print("Initilizing Descovered List")
        for d in range(len(self.discovered)):
            if d == initNode.id:
                self.discovered[d] = True
            else:
                self.discovered[d] = False

        #Initialize Layer 2D List
        if verbose: print("Initilizing 2D List L, with first row: [" + str(initNode.id) + "]")
        L = []
        L.append([initNode])

        #Initialize Tree to Null
        T = []

        #Initialize Layer Counter to Zero
        i = 0

        #Run while L[i] is not empty
        while len(L[i]) != 0:
            print("Current i: " + str(i))
            #Initialize New List L[i+1]
            L.append([])
            print("New size of L: " + str(len(L)))
            #For each node U in L[i]
            for u in L[i]:
                if verbose: print("Current U: " + str(u.id))
                #Consider Each Edge (u,v)
                for v in u.connectedNodes:
                    if verbose: print("Current V: " + str(v.id))
                    if self.discovered[v.id] == False:
                        self.discovered[v.id] = True

                        #Add (u,v) to the tree
                        if verbose: print("Adding (" + str(u.id) +","+str(v.id)+") to the tree")
                        T.append((u.id,v.id))

                        #Add v to the list L[i+1]
                        if verbose: print("Adding V: "+str(v.id)+" to the list L")
                        L[i+1].append(v)
            #Increment Layer Counter by 1
            i += 1
        if verbose: print("L[i] is empty")
        if verbose: print(T)

    def deriveConnectedComponents(self):
        global verbose

def importNodes(filePath):
    global verbose
    if verbose: print("Importing: " + filePath)
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
                if verbose: print("Connecting " + str(currNode.id+1) + " to " + str(graph.nodeList[int(nc)-1].id+1))
                currNode.connectedNodes.append(graph.nodeList[int(nc)-1])
        nodeIndex += 1

    return graph

def main():
    global verbose
    if verbose: print("Starting Program")
    g = importNodes(sys.argv[1])
    g.bfs(g.nodeList[2])
    g.printGraph()

if __name__ == "__main__":
    main()
