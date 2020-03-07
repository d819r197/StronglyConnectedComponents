import sys

verbose = False

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
        if verbose: print("Initilizing 2D List L, with first row: [" + str(initNode.id+1) + "]")
        L = []
        L.append([initNode])

        #Initialize Tree to Null
        T = []

        #Initialize Layer Counter to Zero
        i = 0

        #Run while L[i] is not empty
        while len(L[i]) != 0:
            if verbose: print("Current i: " + str(i))
            #Initialize New List L[i+1]
            L.append([])
            if verbose: print("New size of L: " + str(len(L)))
            #For each node U in L[i]
            for u in L[i]:
                if verbose: print("Current U: " + str(u.id+1))
                T.append(u.id+1)
                #Consider Each Edge (u,v)
                for v in u.connectedNodes:
                    if verbose: print("Current V: " + str(v.id+1))

                    if self.discovered[v.id] == False:
                        self.discovered[v.id] = True

                        #Add (u,v) to the tree
                        #if verbose: print("Adding (" + str(u.id+1) +","+str(v.id+1)+") to the tree")
                        #T.append(v.id+1)

                        #Add v to the list L[i+1]
                        if verbose: print("Adding V: "+str(v.id+1)+" to the list L")
                        L[i+1].append(v)

                        #if u.id == initNode.id:
                            #T.append(u.id)
                            #if verbose: print("INITAL NODE WAS FOUND!")
                            #return T

            #Increment Layer Counter by 1
            i += 1
        if verbose:
            print("L[i] is empty")
            print("T: " + str(T))
        return T

    def resetDiscovered(self):
        for n in self.discovered:
            n = False

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

def reverse(oldGraph):
    newGraph = Graph(oldGraph.nodeCount)
    for n in oldGraph.nodeList:
        for nc in n.connectedNodes:
            newGraph.nodeList[nc.id].connectedNodes.append(newGraph.nodeList[n.id])
    return newGraph

def main():
    global verbose
    if verbose: print("Starting Program")
    g = importNodes(sys.argv[1])
    grev = reverse(g)
    scc = []

    for n in range(len(g.nodeList)):
        bfs1 = g.bfs(g.nodeList[n])
        bfs2 = grev.bfs(grev.nodeList[n])
        intersection = []
        if verbose: print("N: "+str(n+1)+" and BFS1: "+str(bfs1)+" and BFS2: "+str(bfs2))
        #for n in bfs1:
        #    if n in bfs2:
        #        intersection.append(n)
        for n in range(g.nodeCount):
            if n+1 in bfs1 and n+1 in bfs2:
                intersection.append(n+1)
        intersection.sort()
        if intersection not in scc:
            scc.append(intersection)
        else:
            scc.append([])

        g.resetDiscovered()
        grev.resetDiscovered()

    if verbose:
        print("----------START G PRINT----------")
        g.printGraph()
        print("-----------END G PRINT-----------")
        print("---------START GREV PRINT---------")
        grev.printGraph()
        print("----------END GREV PRINT----------")

    for i in scc:
        for j in i:
            print(str(j)+" ", end = '')
        print("\n", end ='')

if __name__ == "__main__":
    main()
