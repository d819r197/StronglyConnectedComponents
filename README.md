# StronglyConnectedComponents
Implementation of an algorithm that identifies strongly connected components in a given graph. Developed for Algorithms at the University of Kansas.

## EECS 660 Homework 2: Strongly Connected Components
The goal of this assignment is to implement an algorithm to find all Strongly Connected
Components (SCC) in a given graph. Find the algorithm on Page 98 of the book
Algorithm Design. You may also need the DFS/BFS algorithm on page 90-93.

For a directed graph, a strongly connected component is defined as a subgraph that for
any of its two nodes u and v, there exists a path from u to v and a path from v to u. Note
that a single node itself can be a valid SCC because, by definition, it can always go to
itself.

For example, the graph below exists a path from node 3 to node 4 and also a path from
node 4 to node 3, then nodes 3 and 4 are in the same SCC. There is a path from node 4
to node 2, but a 2-4 path does not exist. So, node 2 and 4 are not in the same SCC.
Your program should read in an input file which has the following format:
For example,
```
4 // there are 4 nodes in the graph
// an empty line, separating the graph size field and the graph field
2 3 // node 1 has two outgoing edges, one connects node 2 and the other connects 3
// an empty line, indicating node 2 has no outgoing edge
2 4
3 // do NOT include newline here
```

The first argument represents the number of nodes in the graph. In this case, there are
4 nodes. The second argument represents the directed connected nodes to each node. In
this example, the first node connects to node 2 and node 3, the second node has no node
to connect, the third node connects to node 2 and node 4, and the last node connects to
node 3.
