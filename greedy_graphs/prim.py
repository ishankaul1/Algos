from collections import defaultdict
import heapq
import sys

def prims(n, edges, start):
    adj_lists = defaultdict(list)
    visited = [False for _ in range(n)]
    dists = {} #cost of edge leading into each node in MST
    for i in range(n):
        dists[i+1] = sys.maxsize
    dists[start] = 0
    for edge in edges:
        adj_lists[edge[0]].append((edge[1], edge[2]))
        adj_lists[edge[1]].append((edge[0], edge[2]))
        
    edgeQueue = [(cost, v) for v, cost in adj_lists[start]] #heap to hold edge cost and ending node for each edge on the fringe
    heapq.heapify(edgeQueue)
    visited[start-1] = True
    #print(edgeQueue)
    while edgeQueue:
        
        cost, v = heapq.heappop(edgeQueue) #get min from heap
        
        
        #neighboring nodes 
        if not visited[v-1]:
            visited[v-1] = True
            if cost < dists[v]: #change in-value of path to node if less than what was previously calculated
                dists[v] = cost
            for v_next, nextCost in adj_lists[v]: #add unvisited neighbors to queue
                if not visited[v_next-1]:
                    heapq.heappush(edgeQueue, (nextCost, v_next))
        #print(edgeQueue)
    return sum(dists.values())


def test1():
    n = 5
    edges = [(1, 2, 3), (1, 3, 4), (4, 2, 6), (5, 2, 2), (2, 3, 5), (3, 5, 7)]
    start = 5
    print("Correct: 15")
    print("Solution: " + str(prims(n, edges, start)))
    print()

def test2():
    n = 4
    edges = [(1, 2, 5), (1, 3, 3), (4, 1, 6), (2, 4, 7), (3, 2, 4), (3, 4, 5)]
    start = 1
    print("Correct: 12")
    print("Solution: " + str(prims(n, edges, start)))
    print()

def test3():
    n = 5
    edges = [(1, 2, 20), (1, 3, 50), (1, 4, 70), (1, 5, 90), (2, 3, 30), (3, 4, 40), (4, 5, 60)]
    start = 1
    print("Correct: 150")
    print("Solution: " + str(prims(n, edges, start)))
    print()

def test4():
    n = 5
    edges = [(1, 2, 1), (1, 3, 1), (2, 4, 6), (3, 5, 6), (4, 5, 1)]
    start = 1
    print("Correct: 9")
    print("Solution: " + str(prims(n, edges, start)))
    print()

test1()
test2()
test3()
test4()

