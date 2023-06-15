from collections import deque
import re

class Node:
    def __init__(self, val, len):
        self.val = val
        self.len = len
        self.driver = None
        self.minDist = None
        self.minDistParent = None

def createGraph(vertices, edges):
    graph = {}
    for vertex in vertices:
        graph[vertex] = []
    for edge in edges:
        edge = re.findall("\d+", edge)
        # edge[0] = source
        # edge[1] = destination
        # edge[2] = length
        graph[edge[0]].append(Node(edge[1], edge[2]))
    return graph

def relax(u, v, Q, parents):
    if v.minDist == None or v.minDist > (u.minDist + int(v.len)):
        v.minDist = u.minDist + int(v.len)
        v.minDistParent = u
        parents[v.val] = u
        Q.append(v)

def initRelax(graph, sourceNode):
    for adjList in graph.values():
        for node in adjList:
            node.minDist = None
            node.minDistParent = None
    sourceNode.minDist = 0

def dijkstra(graph, sourceNode, parents):
    initRelax(graph, sourceNode)
    S = []
    Q = []
    Q.append(sourceNode)
    while len(Q) > 0:
        u = Q.pop(0)
        S.append(u.val)
        for v in graph[u.val]:
            if v.val not in S:
                relax(u, v, Q, parents)

def shortestPath(s, v, parents):
    path = []
    #path.append(v.val)
    print(v.val)
    print(parents.items())
    parent = v.minDistParent if v.minDistParent else parents[v.val]
    while parent.val != s.val:
        path.append(parent.val)
        parent = parent.minDistParent
    path.append(s.val)
    path.reverse()
    return (path, v.minDist)

def findDrivers(graph, source, maxDepthLevel=5):
    drivers = []
    currLevel = 0
    visited = set()
    queue = deque([(source.val, currLevel)])
    visited.add(source.val)
    while queue:
        u, currLevel = queue.popleft()
        if currLevel > maxDepthLevel:
            break
        for node in graph[u]:
            if node.val not in visited:
                queue.append((node.val, currLevel + 1))
                visited.add(node.val)
                if node.driver:
                    drivers.append(node)
    return drivers