## Maze generation algorithm

It is known that if we want to traverse a graph we can use either the depth first or the breath first search. Additionally, those methods correspond to ways of exploring a maze. Ιn this project used the reverse way. Let's consider a graph nxn, in which the nodes correspond to the rooms of the maze. Initially we consider that each node is connected to all its neighboring nodes. The corner nodes have two neighbors, nodes on the periphery of the graph but not in the corners have three neighbors and internal nodes have four neighbors.

Consider a maze as shown in the following image:

![alt text](https://github.com/dmst-algorithms-course/assignment-2015-1/raw/master/grid_graph.png)

### Algorithm

1. We begin from a graph's node.

2. We note that we visited this node and retriev the list of neighboring nodes. We choose randomly neighboring elements and then:

  * If we have not visited the neighboring node, move to this node, store the edge between two nodes and recursively continue the procedure from step 2 with the neightboring element.

Basically, we implement a depth first search of the graph.

When the algorithm terminates, one new graph is created. The vertices are the vertices of the original graph and the edges are the edges we followed. The resulting graph is a maze.
