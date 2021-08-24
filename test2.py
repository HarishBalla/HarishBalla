from collections import defaultdict
from heapq import *



with open("inputPS6.txt") as f:
    lines = f.readlines()
    line = f.readline()
    my_edges= []
    if not lines:
        print("No data found")
    elif "servers" in line:
        numberofservers=(line.strip().split(':'))
        print(numberofservers[1])
    else:
        for line in lines:
            node1, node2, distance = (line.strip().split(' '))
            my_edges.append((node1,node2, int(distance)))
# similarly you can read other information like coordinates.

test_edges = my_edges
print(test_edges)
#print(myedges)

###########################



def dijkstra(edges, source, dest):
    graph = defaultdict(list)
    for l,r,c in edges:
        graph[l].append((c,r))

    # dist records the min value of each node in heap.
    q, seen, dist = [(0,source,())], set(), {source: 0}
    while q:
    #heappop will return vertex with least cost
        (cost,v1,path) = heappop(q)
        if v1 in seen: continue

        seen.add(v1)
        path += (v1,)
        if v1 == dest: return (dest,cost)

        for c, v2 in graph.get(v1, ()):
            if v2 in seen: continue

            # Not every edge will be calculated. The edge which can improve the value of node in heap will be useful.
            if v2 not in dist or cost+c < dist[v2]:
                dist[v2] = cost+c
                heappush(q, (cost+c, v2, path))

    return float("inf")
if __name__ == "__main__":
    file1 = open('outputPS6.txt', 'w')
    print (test_edges)
    file1.write(str(dijkstra(test_edges, 'A', 'B')) + "\n")
   # file1.write("\n")
    file1.write(str(dijkstra(test_edges, "A", "C")) + "\n")
    #file1.write("\n")
    file1.write(str(dijkstra(test_edges, 'A', 'D')) + "\n")
    #file1.write("\n")
    file1.write(str(dijkstra(test_edges, 'A', 'E')) + "\n")

