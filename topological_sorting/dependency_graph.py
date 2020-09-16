from collections import defaultdict
from collections import deque
#Problem: given a graph of library dependencies in a system, output a list describing the order these libraries should be loaded
#Basically the same idea as topological sort, except in this implementation we are given a list of DEPENDENCIES to start off with, not ADJACENCIES (the opposite)

#Method 1: run Dependency Resolving DFS algorithm directly on the dependency list
def dep_resolve_DFS(dep_graph):
    resolved = []
    seen_but_unresolved = []
#dependency is resolved if all if its dependencies have been resolved, or if it has none
    def dep_resolve_DFS_helper(node):
        seen_but_unresolved.append(node)
        for dep in dep_graph[node]:
            if dep not in resolved:
                if dep in seen_but_unresolved:
                    #cycle detected
                    raise Exception('Cycle detected: ' + dep + ", " + node) #need to break out of the function to avoid getting stuck in infinite loop
                dep_resolve_DFS_helper(dep)

        resolved.append(node)
        

    for node in dep_graph:
        if node not in resolved:
            dep_resolve_DFS_helper(node)

    return resolved


#Method 2: Convert dependency list to adjacency list representation, then run topological sort using Kahn's algorithm or DFS with keeping track of visited nodes

def convert_dep_adj(dep_graph):
    adj_list = defaultdict(list)
    for u in dep_graph:
        for v in dep_graph[u]:
            adj_list[v].append(u)

    return adj_list
    
def dep_resolve_Kahns(dep_graph):
    resolved = []    
    adj_list = convert_dep_adj(dep_graph)
    indegree_map = {}
    zero_degree_list = deque()
    num_visited = 0

    #calculate indegrees and create zero degree list
    for node in dep_graph:
        node_indegree = len(dep_graph[node])
        indegree_map[node] = node_indegree
        if node_indegree == 0:
            zero_degree_list.append(node)



    #while zero degree list exists
    while zero_degree_list:
        #get element from zero degree list
        u = zero_degree_list.popleft()
        resolved.append(u)
        num_visited += 1

        #resolve adjacencies of u
        for v in adj_list[u]:
            indegree_map[v] -= 1
            if indegree_map[v] == 0:
                zero_degree_list.append(v)
    
    if num_visited != len(adj_list):
        return "Cycle detected. Visited " + str(num_visited) + " nodes, " + str(len(adj_list)) + " nodes total"
        
    return resolved
    
    

    
    


def test1():
    dep_graph = {
    "a" : ["b", "d"],
    "b" : ["c", "e"],
    "c" : ["d", "e"],
    "d" : [],
    "e" : []
    }
    print(dep_resolve_DFS(dep_graph))
    print(dep_resolve_Kahns(dep_graph))
    print()


def test2():
    dep_graph = {
            "e" : [],
            "a" : ["b", "d"],
            "b" : ["c", "e"],
            "c" : ["d", "e"],
            "d" : []
            }
    print(dep_resolve_DFS(dep_graph))
    print(dep_resolve_Kahns(dep_graph))
    print()

def test3():
    dep_graph = {
            "e" : ["b"],
            "a" : ["b", "d"],
            "b" : ["c", "e"],
            "c" : ["d", "e"],
            "d" : []
            }
    
    print(dep_resolve_Kahns(dep_graph))
    print(dep_resolve_DFS(dep_graph))
    print()


def main():
    test1()
    test2()
    test3()


main()
