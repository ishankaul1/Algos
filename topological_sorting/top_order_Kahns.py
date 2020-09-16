from collections import defaultdict
from collections import deque

#Python3 implementation of O(V+E) topological sorting of a DAG using Kahn's algorithm, with error checking for cycles.

class Top_Sort_Kahns:
    def __init__(self, vertices):
        self.vertices = vertices #number of vertices
        self.adj_list = defaultdict(list) #dictionary with key = number val of vertice, val = list of directed edges that start from key (u = key, v = values in list)
        self.indegrees = [0 for _ in range(self.vertices)] #keeps track of indegrees for each vertice - used for Kahn's topological sorting
        self.num_visited = 0 #keep track of number of visited nodes; need to detect cycles
        
    #adds one edge to adjacency list
    def addEdge(self, u, v):
        self.adj_list[u].append(v)

    #calculates indegrees of each edge; called right at the beginning of top_sort() method
    def calc_indegrees(self):
        #iterate through adjacency list graph
        for u in self.adj_list:
        #every time a value appears in an adjacency list, +1 to its indegree
            for v in self.adj_list[u]:
                self.indegrees[v] += 1

    #find nodes with 0 indegree at the start
    def init_zero_degree_list(self):
        zero_degree_list = deque() #deque needs to be used in python, because of O(1) popleft() and append(). List would work in terms of correctness, but pop(0) runs O(N) instead of O(1)
        for i in range(len(self.indegrees)):
            if self.indegrees[i] == 0:
                zero_degree_list.append(i)
        return zero_degree_list

    #where the logic happens
    def top_sort_Kahns(self):
        #get the initial indegrees calculated
        self.calc_indegrees()

        #create array for final result ordering
        top_sorted = []

        #create a list of the initial indegrees
        zero_degree_list = self.init_zero_degree_list() 

        #run while the list still has elements
        while zero_degree_list:
            #take first elem
            u = zero_degree_list.popleft()
            top_sorted.append(u)
            self.num_visited += 1

            #find adjacencies of u
            for v in self.adj_list[u]:
                self.indegrees[v] -= 1
                if self.indegrees[v] == 0:
                    zero_degree_list.append(v)

        if self.num_visited == self.vertices:
            return top_sorted
        else:
            print("Cycle detected. Number of vertices visited = " + str(self.num_visited) + ", number of vertices total = " + str(self.vertices))
            return False


# Some basic test cases that make a new Graph object, add edges according to the goal of the test, and print results.

#Tests a DAG - Ordering 0-12 in order for this case, makes it easy to check
def testDAG():
    newGraph = Top_Sort_Kahns(13)
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
    result = newGraph.top_sort_Kahns()
    if (result):
        [print(i, end=" ") for i in result]
        print()

#tests whether a 2-node cycle is detected. (3,6) backedge (6, 3)
def testCycle_2Node():
    newGraph = Top_Sort_Kahns(13)
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
    result = newGraph.top_sort_Kahns()
    if (result):
        [print(i, end=" ") for i in result]
        print()

#test whether a 3-node cycle is detected. (1, 4), (4, 7), backedge (7,1)
def testCycle_3Node():
    newGraph = Top_Sort_Kahns(13)
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
    result = newGraph.top_sort_Kahns()
    if (result):
        [print(i, end=" ") for i in result]
        print()


def main():
    #Run tests in main on 3 different Graph objects.
    testDAG()
    testCycle_2Node()
    testCycle_3Node()




main()
