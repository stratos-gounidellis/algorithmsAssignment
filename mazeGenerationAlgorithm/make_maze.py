import random
import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
nodes_list = deque([])


# Method to check if the user's input is integer!
def checkInteger(argument):
    # if it is integer return the input
    if argument.isdigit():
        return int(argument)
    # else print error and exit the program!
    else:
        print("Error! Check the type of the arguments!" +
              "The number of rows, the coordinates and" +
              "the seed should be integers!")
        sys.exit(2)


# Method to create the neighbouring nodes
def createGraph(n):
    graph = {}
    neighbouring_nodes_tuple = ()
    neighbouring_nodes = []
    for x in range(n):
        for y in range(n):
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                # check if the coordinates of the node are greater than zero
                # and smaller than the number of rows/columns
                if new_x >= 0 and new_y >= 0 and new_x < n and new_y < n:
                    # create a tuble with coordinates of this tuple
                    neighbouring_nodes_tuple = (new_x, new_y)
                    key = (x, y)
                    graph.setdefault(key, [])
                    # add this node in the neighbouring list
                    graph[key].append(neighbouring_nodes_tuple)
    return graph


# Method to save the connection between the nodes
def makeMaze(start_x, start_y):
    key = (start_x, start_y)
    neighbouring_nodes = graph[key]
    # delete the key from the graph
    del graph[key]
    # randomly generate a list
    random_neighbours = random.sample(neighbouring_nodes,
                                      len(neighbouring_nodes))
    while len(random_neighbours) > 0:
        random_neighbour = random_neighbours.pop()
        # if this node is not in the list
        if random_neighbour not in nodes_list:
            # add the current key to the queue
            nodes_list.append(key)
            # add the node with which it is connected in the queue
            nodes_list.append((random_neighbour[0], random_neighbour[1]))
            # recursively call the method
            makeMaze(random_neighbour[0], random_neighbour[1])
    return nodes_list


# Method to write the connections between the nodes into a file
def writeOutput(output_file, nodeList):
    outputFile = open(output_file, 'w')
    while len(nodeList) > 0:
        tuple1 = nodeList.popleft()
        string1 = str(tuple1) + ", "
        outputFile.write(string1)
        tuple2 = nodeList.popleft()
        string2 = str(tuple2) + "\n"
        outputFile.write(string2)
    outputFile.close()
# print error if the user enters less than six errors
if len(sys.argv) < 6:
    print("Error! You should enter 5 parametres!")
    sys.exit(2)
n = checkInteger(sys.argv[1])
start_x = checkInteger(sys.argv[2])
start_y = checkInteger(sys.argv[3])
# print error if the coordinates are not between zero
# and the number of rows/columns.
if start_x >= n or start_x < 0 or start_y >= n or start_y < 0:
    print("Error! Each coordinate of the starting node" +
          "must be between zero and the number of rows" +
          "and columns of the graph!")
    sys.exit(2)
seed = checkInteger(sys.argv[4])
output_file = str(sys.argv[5])

random.seed(seed)
graph = createGraph(n)
node_list = makeMaze(start_x, start_y)
writeOutput(output_file, node_list)
