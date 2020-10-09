#Goal: find the shortest path from SOURCE node to DEST node in a bidirectional graph
import sys
import heapq

#Uses map of unvisited nodes to keep track of what's on the fringe. Gets the min each time. Runtime can be saved by keeping in priority queue instead
def djikstra_sp(graph, source, dest):
    fringe_map = {}
    visited = {node: False for node in graph}
    dist_from_src = {node: sys.maxsize for node in graph}
    dist_from_src[source] = 0
    fringe_map[source] = 0
    #for node in graph:
    #    visited[node] = False
    #    if node == source:
    #        dist_from_src[node] = 0
    #    else:
    #        dist_from_src[node] = sys.maxsize
    #    unvisited_map[node] = dist_from_src[node]



    current = source
    while not visited[dest]:
        #print(unvisited_map)
        for adj_node, path_weight in graph[current]:
            if not visited[adj_node]:
                new_dist = dist_from_src[current] + path_weight
                dist_from_src[adj_node] = min(new_dist, dist_from_src[adj_node])
                fringe_map[adj_node] = dist_from_src[adj_node]
        visited[current] = True
        del fringe_map[current]
        
        #print(unvisited_map)       
        if  fringe_map:
            current = min(fringe_map.items(), key= lambda x:x[1])[0] #change to priority queue for better runtime - currently O(V^2). Priority queue must hold: dist from src (editable in O(1)!! because these values can get recalculated), name of node

    return dist_from_src[dest]
    
def djikstra_sp_pq(graph, source, dest):
    dist_from_src = {node: sys.maxsize for node in graph}
    visited = {node: False for node in graph}
    dist_from_src[source] = 0
    

    fringe_heap = [(0, source)] #stores dist_from_src, nodename tuples. ordered so we only process shortest unresolved path first
    
    #explore nodes until dest node is resolved
    while not visited[dest]:
        #print(fringe_heap)
        #get node in the fringe that is closest to the source
        cur_dist, cur_node = heapq.heappop(fringe_heap)

        #only resolve this node and neighbors if it has not already been visited. Nodes can get added to the fringe multiple times, but only want to explore through the shortest path through it. So if we have already visited, don't resolve again. We are prevented from reaching dest if there is already another shortest path to it because all other choices on the shorter path would be popped from the heap before the longer one finishes.
        if not visited[cur_node]:
            #calculate distance to all neighbors of the node through path of the node
            for adj_node, path_weight in graph[cur_node]:
                new_dist = cur_dist + path_weight
                
                #if the new calculated distance is less than the distance already calculated, make it the new distance to this node from source, and push this node onto the fringe
                if new_dist < dist_from_src[adj_node]:
                    dist_from_src[adj_node] = new_dist
                    heapq.heappush(fringe_heap, (new_dist, adj_node))

        #don't revisit a fully-resolved node
        visited[cur_node] = True

    return dist_from_src[dest]



def test1():
    graph1 = {'A': [('B', 3)],
            'B' : [('A', 3), ('C', 3), ('D', 4)],
            'C' : [('B', 2), ('D', 5), ('E', 5)],
            'D' : [('B', 4), ('C', 5), ('E', 2)],
            'E' : [('C', 5), ('D', 2)]}

    source = 'A'
    dest = 'E'
    correct = 9 #A->B->D->E

    testgraph(graph1, source, dest, correct)


def test2():
    graph1 = {'A': [('B', 3)],
            'B' : [('A', 3), ('C', 3), ('D', 4)],
            'C' : [('B', 2), ('D', 5), ('E', 5)],
            'D' : [('B', 4), ('C', 5), ('E', 2)],
            'E' : [('C', 5), ('D', 2)]}

    source = 'E'
    dest = 'A'
    correct = 9 #A->B->D->E

    testgraph(graph1, source, dest, correct)

def test3():
    graph1 = {'A': [('B', 3)],
            'B' : [('A', 3), ('C', 3), ('D', 4)],
            'C' : [('B', 2), ('D', 5), ('E', 5)],
            'D' : [('B', 4), ('C', 5), ('E', 2)],
            'E' : [('C', 5), ('D', 2)]}

    source = 'B'
    dest = 'D'
    correct = 4 #A->B->D->E

    testgraph(graph1, source, dest, correct)

def test4():
    graph1 = {'A': [('B', 3)],
            'B' : [('A', 3), ('C', 3), ('D', 4)],
            'C' : [('B', 2), ('D', 5), ('E', 5)],
            'D' : [('B', 4), ('C', 5), ('E', 2)],
            'E' : [('C', 5), ('D', 2)]}

    source = 'B'
    dest = 'E'
    correct = 6 #A->B->D->E

    testgraph(graph1, source, dest, correct)


def test5():
    graph1 = {'A': [('D', 4), ('B', 1)],
            'B': [('A', 1), ('C', 1)],
            'C': [('B', 1), ('D', 1)],
            'D': [('A', 4), ('C', 1)]}

    source = 'A'
    dest = 'D'
    correct = 3 #A->B->D->E

    testgraph(graph1, source, dest, correct)


def testgraph(graph, source, dest, correct):
    print("Correct: " + str(correct))
    print("Djikstra: " + str(djikstra_sp(graph, source, dest)))
    print("Djikstra(pq): " + str(djikstra_sp_pq(graph, source, dest)))
    print()


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
main()
