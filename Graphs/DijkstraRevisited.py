

import heapq

#Without Heap (Normal)

def dijkstras(G, start='A'):
    shortest_path = {}
    unvisited = dict.fromkeys(G.keys())

    for node in unvisited:
        shortest_path[node] = float("inf")
    
    shortest_path[start] = 0

    '''
    
     'A': [(4, 'B'), (2, 'C')],
        'B': [(3, 'C'), (3, 'E'), (2, 'D')],
        'C': [(1, 'B'), (4, 'D'), (5, 'E')],
        'D': [],
        'E': [(1, 'D')],
    
    '''
    while unvisited:    
        min_node = None 

        # This section gets the min node of the graph 
        for node in unvisited:
            if min_node is None:
                min_node = node 
            elif shortest_path[node] < shortest_path[min_node]:
                min_node = node 
        
        for edge in G[min_node]:
            cost, to_node = edge 

            if cost + shortest_path[min_node] < shortest_path[min_node]:
                shortest_path[to_node] = cost + shortest_path[min_node]
            
        
        del unvisited[min_node]
    
    return shortest_path

def dijkstras_with_heap(G, start='A'):
    shortest_path = {}
    visited = set()
    heap = []

    for node in G.keys():
        shortest_path[node] = float("inf") 
    
    shortest_path[start] = 0
    visited.add(start) 

    heapq.heappush(heap, (0, start))

    while heap:
        (distance, node) = heapq.heappop(heap) 
        visited.add(node) 

        for edge in G[node]:
            cost, to_node = edge 

            if (to_node not in visited) and (distance + cost) < shortest_path[to_node]:
                shortest_path[to_node] = distance + cost 
                heapq.heappush(heap, (shortest_path[to_node], to_node)) 
    return shortest_path