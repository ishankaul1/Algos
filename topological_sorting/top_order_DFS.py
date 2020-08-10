from collections import defaultdict

#Python3 implementation of O(V+E) topological sorting algorithm using DFS, with error checking for cycles

class Top_Sort_DFS:
    def __init__(self, vertices):
        self.vertices = vertices #number of vertices
        self.adj_list = defaultdict(list) #dictionary with key = number val of vertice, val = list of directed edges that start from key (u = key, v = values in list)
        self.visited = [False] * self.vertices #keeps track of whether each vertice has been visited by topological sort
        self.branch_visited = [False] * self.vertices #keeps track of vertices that have been visited WITHIN recursive branch; reset every time a branch is exited

    #adds one edge to adjacency list
    def addEdge(self, u, v):
        self.adj_list[u].append(v)

    def top_sort_DFS(self):
        stack = []
        for node in range(self.vertices):
            if (not self.visited[node]):
                stack = self.top_sort_util(node, stack)
        return reversed(stack)

    def top_sort_util(self, node, stack):
        self.visited[node] = True
        self.branch_visited[node] = True
        for v in self.adj_list[node]:
            if (self.branch_visited[v]):
                #cycle detected - print a flag & the nodes visited on the path
                print("Cycle detected: ", end=" ")
                for i in range(len(self.branch_visited)):
                    if (self.branch_visited[i]):
                        print(str(i), end=" ")
                print()
            if (not self.visited[v]):
                self.top_sort_util(v, stack)

        stack.append(node)
        self.branch_visited[node] = False
        return stack

# Some basic test cases that make a new Graph object, add edges according to the goal of the test, and print results.

#Tests a DAG - Ordering 0-12 in order for this case, makes it easy to check
def testDAG():
    newGraph = Top_Sort_DFS(13)
    newGraph.addEdge(0, 3)
    newGraph.addEdge(0, 2)
    newGraph.addEdge(1, 3)
    newGraph.addEdge(1, 4)
    newGraph.addEdge(1, 5)
    newGraph.addEdge(2, 10)
    newGraph.addEdge(3, 6)
    newGraph.addEdge(3, 12)
    newGraph.addEdge(4, 7) 
    newGraph.addEdge(4, 8)
    newGraph.addEdge(4, 9)
    newGraph.addEdge(7, 10)
    newGraph.addEdge(7, 11)
    newGraph.addEdge(9, 12)
    result = newGraph.top_sort_DFS()
    if (result):
        [print(i, end=" ") for i in result]
        print()

#tests whether a 2-node cycle is detected. (3,6) backedge (6, 3)
def testCycle_2Node():
    newGraph = Top_Sort_DFS(13)
    newGraph.addEdge(0, 3)
    newGraph.addEdge(0, 2)
    newGraph.addEdge(1, 3)
    newGraph.addEdge(1, 4)
    newGraph.addEdge(1, 5)
    newGraph.addEdge(2, 10)
    newGraph.addEdge(3, 6)
    newGraph.addEdge(6, 3)
    newGraph.addEdge(3, 12)
    newGraph.addEdge(4, 7) 
    newGraph.addEdge(4, 8)
    newGraph.addEdge(4, 9)
    newGraph.addEdge(7, 10)
    newGraph.addEdge(7, 11)
    newGraph.addEdge(9, 12)
    result = newGraph.top_sort_DFS()
    if (result):
        [print(i, end=" ") for i in result]
        print()

#test whether a 3-node cycle is detected. (1, 4), (4, 7), backedge (7,1)
def testCycle_3Node():
    newGraph = Top_Sort_DFS(13)
    newGraph.addEdge(0, 3)
    newGraph.addEdge(0, 2)
    newGraph.addEdge(1, 3)
    newGraph.addEdge(1, 4)
    newGraph.addEdge(1, 5)
    newGraph.addEdge(2, 10)
    newGraph.addEdge(3, 6)
    newGraph.addEdge(3, 12)
    newGraph.addEdge(4, 7)
    newGraph.addEdge(7, 1)
    newGraph.addEdge(4, 8)
    newGraph.addEdge(4, 9)
    newGraph.addEdge(7, 10)
    newGraph.addEdge(7, 11)
    newGraph.addEdge(9, 12)
    result = newGraph.top_sort_DFS()
    if (result):
        [print(i, end=" ") for i in result]
        print()


def main():
    #Run tests in main on 3 different Graph objects.
    testDAG()
    testCycle_2Node()
    testCycle_3Node()




main()
