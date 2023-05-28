#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ownLibraries.algo1 import Array
from ownLibraries.linkedList import LinkedList, length, add, Node, search, delete
from ownLibraries.myqueue import enqueue, dequeue
import random

def createGraph(vertices, edges):
    n = len(vertices)
    graph = Array(n, LinkedList())
    for i in letters:
        nodo = Node()
        nodo.value = i
        index = hash(i,n)
        graph[index] = LinkedList()
        graph[index].head = nodo

    for i in edges:
        index = hash(i[0], n)
        tupla = [i[1], i[2]]
        nodo = Node()
        nodo.value = tupla
        node = graph[index]
        if node.head.nextNode == None:
            node.head.nextNode = nodo
        else:
            node = node.head.nextNode
            while node.nextNode != None:
                node = node.nextNode
            node.nextNode = nodo
    return graph

def hash(key, n):
    return (ord(key) - ord("a") + 1) % n

'''
    Ejercicio 2
'''
def existPath(graph, v1, v2):
    bfs(graph, v1)
    n = len(graph)
    vertex = graph[hash(v2, n)].head
    for i in range(n):
        if vertex.value[0] == v1:
            return True
        else:
            vertex = graph[hash(vertex.value[2], n)].head
    return False
def bfs(graph, s):
    for i in graph:
        value = i.head.value
        i.head.value = [value, "white",None,0]
    
    n = len(graph)
    vertex = graph[hash(s,n)].head
    vertex.value[1] = "grey"
    vertex.value[3] = 0
    Q = LinkedList()
    enqueue(Q,vertex)
    while Q.head != None:
        u = dequeue(Q)
        letter = u.value[0]
        colour = u.value[1]
        distance = u.value[3]
        while u != None:
            if colour == "white":
                vertex = graph[hash(u.value,n)].head
                vertex.value[1] = "grey"
                vertex.value[2] = letter
                vertex.value[3] = distance + 1
                enqueue(Q, vertex)
            u = u.nextNode
            if u != None:
                colour = graph[hash(u.value, n)].head.value[1]
        graph[hash(letter, n)].head.value[1] = "black"

'''
    Ejercicio 3
'''
def isConnected(graph):
    a = graph[0].head.value
    bfs(graph, a)
    for i in graph:
        if i.head.value[1] == "white":
            return False
    return True

'''
    Ejercicio 4
'''
def isTree(graph):
    return isConnected(graph) and cycleVerify(graph)
def cycleVerify(graph):
    s = graph[0].head.value
    for i in graph:
        value = i.head.value
        i.head.value = [value, "white",None]
    
    n = len(graph)
    vertex = graph[hash(s,n)].head
    vertex.value[1] = "grey"
    Q = LinkedList()
    enqueue(Q,vertex)
    while Q.head != None:
        u = dequeue(Q)
        letter = u.value[0]
        colour = u.value[1]
        if u.nextNode != None:
            node = u.nextNode
            while node != None:
                if graph[hash(node.value,n)].head.value[1] == "grey":
                    return False
                node = node.nextNode
        while u != None:
            if colour == "white":
                vertex = graph[hash(u.value,n)].head
                vertex.value[1] = "grey"
                vertex.value[2] = letter
                enqueue(Q, vertex)
            u = u.nextNode
            if u != None:
                colour = graph[hash(u.value, n)].head.value[1]
        graph[hash(letter, n)].head.value[1] = "black"
    return True    

'''
    Ejercicio 5
'''
def isComplete(graph):
    n = len(graph)
    j = 0
    for i in graph:
        node = i.head
        letter = i.head.value
        while node != None:
            j += 1
            node = node.nextNode
            if node != None:
                if node.value == letter:
                    return False
        if j == n:
            j = 0
        else: 
            return False
    return True

'''
    Ejercicio 6
'''
def convertTree(graph):
    s = graph[0].head.value
    for i in graph:
        value = i.head.value
        i.head.value = [value, "white",None]
    
    n = len(graph)
    vertex = graph[hash(s,n)].head
    vertex.value[1] = "grey"
    Q = LinkedList()
    edges = LinkedList()
    enqueue(Q,vertex)
    while Q.head != None:
        u = dequeue(Q)
        letter = u.value[0]
        colour = u.value[1]
        if u.nextNode != None:
            node = u.nextNode
            while node != None:
                if graph[hash(node.value,n)].head.value[1] == "grey":
                    nodo = Node()
                    nodo.value = [letter,node.value]
                    add(edges, nodo)
                node = node.nextNode
        while u != None:
            if colour == "white":
                vertex = graph[hash(u.value,n)].head
                vertex.value[1] = "grey"
                vertex.value[2] = letter
                enqueue(Q, vertex)
            u = u.nextNode
            if u != None:
                colour = graph[hash(u.value, n)].head.value[1]
        graph[hash(letter, n)].head.value[1] = "black"
    return edges

'''
    Parte 2
'''
def dfs(graph):
    for i in graph:
        value = i.head.value
        i.head.value = [value,"white",None,0,0]

    n = len(graph)
    time = 0
    for i in graph:
        if i.head.value[1] == "white":
            dfsR(graph, i.head, n, time)
def dfsR(graph,u,n, time):
    time += 1
    u.value[3] = time
    u.value[1] = "gray"
    letter = u.value[0]
    while u != None:
        vertex = graph[hash(u.value[0],n)].head
        if vertex.value[1] == "white":
            vertex.value[2] = letter
            dfsR(graph, vertex, n, time)
        u = u.nextNode
    
    if letter != None:
        g = graph[hash(letter,n)].head
        g.value[1] = "black"
        time += 1
        g.value[4] = time

'''
    Ejercicio 7
'''
def countConnections(graph):
    conexNumber = 0
    for i in graph:
        value = i.head.value
        i.head.value = [value,"white",None,0,0]

    n = len(graph)
    time = 0
    for i in graph:
        if i.head.value[1] == "white":
            conexNumber += 1
            dfsR(graph, i.head, n, time)

    return conexNumber

'''
    Ejercicio 8
'''
def convertToBFSTree(graph, v):
    for i in graph:
        value = i.head.value
        i.head.value = [value, "white",None]
    
    n = len(graph)
    vertex = graph[hash(v,n)].head
    vertex.value[1] = "grey"
    Q = LinkedList()
    enqueue(Q,vertex)
    j = 0
    graphReturn = Array(n, LinkedList())
    while Q.head != None:
        u = dequeue(Q)
        letter = u.value[0]
        colour = u.value[1]
        graphReturn[j] = LinkedList()
        node = Node()
        node.value = letter
        graphReturn[j].head = node
        node = graphReturn[j].head
        while u != None:
            if colour == "white":
                vertex = graph[hash(u.value,n)].head
                lyric = vertex.value[0] 
                vertex.value[1] = "grey"
                vertex.value[2] = letter
                nodoLyric = Node()
                nodoLyric.value = lyric
                node.nextNode = nodoLyric
                node = node.nextNode
                enqueue(Q, vertex)
            u = u.nextNode
            if u != None:
                colour = graph[hash(u.value, n)].head.value[1]
        j += 1
        graph[hash(letter, n)].head.value[1] = "black"

    return graphReturn
    
'''
    Ejercicio 9
'''
def convertToDFSTree(graph, v):
    for i in graph:
        value = i.head.value
        i.head.value = [value,"white",0]

    n = len(graph)
    vertex = graph[hash(v, n)].head
    colour = vertex.value[1]
    i = vertex
    j = 0
    while vertex != None:
        if colour == "white":
            convertToDFSTreeR(graph, i, n,j)
        vertex = vertex.nextNode
        if vertex != None:
            i = graph[hash(vertex.value,n)].head
            colour = i.value[1]

    graphR = Array(n, LinkedList())
    for i in graph:
        nodo = i.head
        position = nodo.value[2]
        graphR[position] = LinkedList()
        graphR[position].head = nodo

    return graphR
def convertToDFSTreeR(graph,u,n,j):
    u.value[1] = "gray"
    u.value[2] = j
    while u != None:
        vertex = graph[hash(u.value[0],n)].head
        if vertex.value[1] == "white":
            j += 1
            sentinel = convertToDFSTreeR(graph, vertex, n, j)
            if sentinel > j:
                j = sentinel
        u = u.nextNode
    return j

'''
    Ejercicio 10
'''
def bestRoad(graph, v1, v2):
    bfs(graph,v1)
    n = len(graph)
    edges = LinkedList()
    vertex = graph[hash(v2,n)].head    
    letter = vertex.value[2]
    while True:
        add(edges, (letter,vertex.value[0]))
        vertex = graph[hash(letter, n)].head
        if letter == v1:
            return edges
        letter = vertex.value[2]

'''
    Ejercicio 11
'''
'''
    Ejercicio 12

Supongamos que tenemos un grafo G que es un árbol y se le agrega una arista nueva entre cualquier par de vértices. Queremos demostrar que el grafo resultante deja de ser un árbol y se forma exactamente un ciclo.

    Dado que G es un árbol, sabemos que es un grafo conexo y acíclico.

    Ahora, supongamos que agregamos una arista nueva entre dos vértices distintos en el grafo G. Llamemos a estos vértices v1 y v2.

    Al agregar la arista entre v1 y v2, se crea una conexión directa entre ellos, lo que implica que hay al menos un camino entre v1 y v2.

    Sin embargo, dado que G es un árbol, solo puede haber un único camino entre cualquier par de vértices. Si agregamos una arista entre v1 y v2, habrá dos caminos posibles para ir de v1 a v2: uno a través de la nueva arista y otro a través del camino existente en el árbol.

    La existencia de dos caminos entre v1 y v2 implica que se ha formado un ciclo en el grafo resultante. Podemos seguir el camino desde v1 a v2 a través de la nueva arista y luego volver de v2 a v1 a través del camino existente en el árbol, formando así un ciclo cerrado.

    Por lo tanto, el grafo resultante ya no es acíclico, lo que contradice la definición de un árbol.

    Concluimos que si el grafo G es un árbol y se le agrega una arista nueva entre cualquier par de vértices, se forma exactamente un ciclo y el grafo deja de ser un árbol.

La demostración muestra que agregar una arista nueva entre cualquier par de vértices en un grafo árbol siempre resultará en la formación de un ciclo y la pérdida de la propiedad de ser un árbol.

'''
'''
    Ejercicio 13

Supongamos que tenemos un árbol BFS y una arista (u, v) que no pertenece a este árbol. Queremos demostrar que los niveles de los vértices u y v difieren a lo sumo en 1.

    En un árbol BFS, los niveles de los vértices se definen como la distancia más corta desde el vértice raíz hasta cada vértice en términos de la cantidad de aristas que se recorren.

    Supongamos que los niveles de u y v difieren en más de 1. Es decir, el nivel de u es mayor que el nivel de v más 1, o el nivel de v es mayor que el nivel de u más 1.

    Si el nivel de u es mayor que el nivel de v más 1, significa que en el árbol BFS, u se encuentra a una distancia mayor que v+1 desde el vértice raíz.

    Como (u, v) no pertenece al árbol BFS, la única forma en que u puede estar a una distancia mayor que v+1 desde el vértice raíz es si existe una arista más corta que conecta u directamente con un vértice que se encuentra más cerca del vértice raíz que v.

    Sin embargo, esto contradice la propiedad de que el árbol BFS representa la distancia más corta desde el vértice raíz. Si existiera una arista más corta entre u y un vértice más cercano al vértice raíz que v, entonces esa arista debería haber sido incluida en el árbol BFS en lugar de la arista (u, v).

    De manera similar, si el nivel de v es mayor que el nivel de u más 1, se llegaría a una contradicción similar.

    Por lo tanto, concluimos que si la arista (u, v) no pertenece al árbol BFS, los niveles de u y v difieren a lo sumo en 1.

La demostración muestra que si una arista no está presente en el árbol BFS, los niveles de los vértices que conecta difieren a lo sumo en 1. Esto se debe a que el árbol BFS representa la distancia más corta desde el vértice raíz, y cualquier arista que tenga una longitud menor que la distancia entre los vértices en términos de niveles debería haber sido incluida en el árbol BFS.

'''
'''
    Parte 3
'''

'''
    Ejercicio 14
'''
def prim(graph):
    n = len(graph)
    v = graph[0].head
    w = graph[0].head.nextNode
    visited = LinkedList()
    add(visited, v.value)
    Q = LinkedList()
    graphR = Array(n, LinkedList())
    
    j = 0
    for i in graph:
        graphR[j] = LinkedList() 
        node = Node()
        node.value = i.head.value
        graphR[j].head = node
        j += 1    

    while w != None:
        enqueue(Q, [(v.value,w.value),random.randint(1,9)])
        w = w.nextNode

    u = dequeue(Q)
    node = Node()
    node.value = (u[0][1],u[1])
    graphR[0].head.nextNode = node
    while u != None:
        w = u
        add(visited, w[0][1])

        r = graphR[hash(w[0][0],n)]

        if r.head.nextNode == None:
            node = Node()
            node.value = (w[0][1], w[1])
            r.head.nextNode = node
        elif r.head.nextNode.value[1] > u[1]:
            node = Node()
            node.value = (w[0][1],w[1])
            r.head.nextNode = node   

        v = graph[hash(w[0][1],n)].head
        w = graph[hash(w[0][1],n)].head.nextNode

        while w != None:
            if search(visited, w.value) == None:
                enqueue(Q, [(v.value,w.value), random.randint(1,9)])
            w = w.nextNode

        u = dequeue(Q)

    return graphR 

'''
    Ejercicio 15
'''
def kruskal(graph):
    n = len(graph)
    sets = Array(n,("",""))
    j = 0
    A = LinkedList()
    B = LinkedList()
    for i in  graph:
        add(A,(i.head.value))
        sets[j] = (i.head.value, i.head.value)
        j += 1

    edges = LinkedList()
    sortEdges(graph, edges)
    nodo = edges.head
    while nodo != None:
        if find(sets,nodo.value[0],n) != find(sets, nodo.value[1],n):
            add(B,((nodo.value[0], nodo.value[1])))
            union(sets, nodo.value[0], nodo.value[1], n)
        nodo = nodo.nextNode

    return createGraph(A,B)
def sortEdges(graph, edges):
    visited = LinkedList()
    for i in graph:
        nodo = i.head
        vertex = nodo.value
        nodo = nodo.nextNode
        while nodo != None:
            if search(visited, nodo.value[0]) == None:
                enqueuePriority(edges, (vertex, nodo.value[0], nodo.value[1]))
            nodo = nodo.nextNode
        add(visited, vertex)
def union(sets, u, v, n):
    newGroup = find(sets, u, n)
    otherGroup = find(sets, v, n)
    sets[hash(otherGroup,n)] = (otherGroup,newGroup)
def find(sets,vertex,n):
    if sets[hash(vertex, n)][1] == vertex:
        return vertex

    group = find(sets, sets[hash(vertex,n)][1], n)
    sets[hash(vertex,n)] = (vertex,group)
    return group
def enqueuePriority(Q, value):
    node = Node() 
    node.value = value
    head = Q.head
    flag = True
    if head == None:
        Q.head = node
    else:
        pre = head
        while head != None:
            if head.value[2] > node.value[2]:
                if head.value == Q.head.value:
                    node.nextNode = Q.head
                    Q.head = node
                else:   
                    nodo = pre.nextNode
                    pre.nextNode = node
                    node.nextNode = nodo
                flag = False
                break
            pre = head
            head = head.nextNode
        if flag:
            pre.nextNode = node

'''
def ponderar(graph):
    visited = LinkedList()
    for i in graph:
        nodo = i.head
        nodo = nodo.nextNode
        while nodo != None:
            if search(visited, nodo.value[0]) == None:
                nodo.value = (nodo.value, random.randint(1,9))
            nodo = nodo.nextNode
        add(visited, i.head.value)
'''

'''
    Ejercicio 16

    Supongamos que el árbol abarcador de costo mínimo de G, denotado como T, no contiene la arista (u, v). Esto significa que hay otro camino en T que conecta el nodo u con el nodo v, y este camino tiene un costo menor que el costo de la arista (u, v).

Ahora, consideremos el conjunto de nodos U en el camino de u a v en T. Dado que v pertenece a V - U, hay al menos un nodo en V - U que está conectado a un nodo en U en el camino de u a v en T. Llamemos a este nodo w.

Si eliminamos la arista (w, v) de T y agregamos la arista (u, v) en su lugar, obtendremos un nuevo árbol abarcador, que denotaremos como T'. Dado que el costo de la arista (u, v) es menor que el costo de la arista (w, v), el costo total de T' será menor que el costo total de T. Esto contradice nuestra suposición inicial de que T es un árbol abarcador de costo mínimo.

Por lo tanto, nuestra suposición de que la arista (u, v) de costo mínimo no pertenece a un árbol abarcador de costo mínimo es incorrecta. Concluimos que si la arista (u, v) de costo mínimo tiene un nodo en U y otro en V - U, entonces la arista (u, v) pertenece a un árbol abarcador de costo mínimo.

'''
'''
    Parte 4
'''
'''
    Ejercicio 17
    Supongamos que tenemos un grafo G(V, A) y una arista e que pertenece a algún ciclo de G y tiene el mayor costo entre todas las aristas del ciclo. Queremos demostrar que existe un árbol abarcador de costo mínimo de G, denotado como AACM(V, A-e), que también es un árbol abarcador de costo mínimo de G.

Para demostrarlo, utilizaremos el método de contradicción. Supongamos que no existe un árbol abarcador de costo mínimo AACM(V, A-e) que también sea un árbol abarcador de costo mínimo de G. Esto significa que hay otro árbol abarcador de costo mínimo de G, denotado como T, que tiene un costo menor que el AACM(V, A-e).

Dado que T es un árbol abarcador de costo mínimo de G, sabemos que no contiene ningún ciclo. Si eliminamos la arista e de T, obtenemos un nuevo árbol abarcador de costo mínimo de G, denotado como T'. Dado que T no contiene ningún ciclo, la arista e no es necesaria para mantener la conectividad de T y, por lo tanto, se puede eliminar sin afectar la propiedad de ser un árbol abarcador.

El costo total de T' será menor que el costo total de T, ya que eliminamos la arista de mayor costo del ciclo. Esto contradice nuestra suposición inicial de que T es un árbol abarcador de costo mínimo.

Por lo tanto, nuestra suposición de que no existe un árbol abarcador de costo mínimo AACM(V, A-e) que también sea un árbol abarcador de costo mínimo de G es incorrecta. Concluimos que existe un árbol abarcador de costo mínimo AACM(V, A-e) que también es un árbol abarcador de costo mínimo de G.
'''
'''
    Ejercicio 18
    Para demostrar que unir dos Árboles Abarcadores de Costo Mínimo (AACM) mediante una arista de costo mínimo resulta en un nuevo AACM, podemos utilizar el método de contradicción.

Supongamos que tenemos dos AACM, denominados T1 y T2, y queremos unirlos mediante una arista de costo mínimo. Denotemos esta arista como (u, v), donde u es un nodo en T1 y v es un nodo en T2.

Primero, observemos que tanto T1 como T2 son árboles acíclicos y contienen todos los nodos del grafo original. Esto se debe a que son AACM, lo que implica que tienen la mínima cantidad de aristas necesarias para conectar todos los nodos sin formar ciclos.

Ahora, si unimos T1 y T2 mediante la arista (u, v), debemos asegurarnos de que el resultado no contenga ciclos y siga siendo un árbol. Si se formara un ciclo, no cumpliría con la propiedad de ser un AACM.

Supongamos que después de unir T1 y T2, se forma un ciclo C en el resultado. Esto implicaría que había una ruta entre u y v en alguno de los AACM anteriores (T1 o T2). Sin pérdida de generalidad, supongamos que había una ruta entre u y v en T1 antes de unirlos.

Si había una ruta entre u y v en T1, entonces podríamos haber utilizado esa ruta en lugar de la arista (u, v) para conectar T1 y T2. Sin embargo, la arista (u, v) fue elegida por ser de costo mínimo, lo que significa que cualquier otra ruta entre u y v en T1 tendría un costo mayor.

Esto contradice la suposición inicial de que se formaba un ciclo al unir T1 y T2. Por lo tanto, concluimos que la unión de dos AACM mediante una arista de costo mínimo resulta en un nuevo AACM.

Esta propiedad es la base del funcionamiento del algoritmo de Kruskal, que busca unir los AACM de manera incremental, comenzando por las aristas de costo mínimo, para construir el AACM global de costo mínimo.
'''
'''
    Ejercicio 19

    1. Obtener un árbol de recubrimiento de costo máximo.
        Para eso en vez de iterar y buscar la arista de costo minimo, busco la arista de costo máximo
    
    2. Obtener un árbol de recubrimiento cualquiera
        No buscaria la arista de costo maximo ni minimo, si no mas bien agarraria sus valores y aplicaria un ramdon e eligiria 1

    3. Dado un conjunto de aristas E ∈ A, que no forman un ciclo, encontrar el árbol de recubrimiento mínimo Gc(V,AC) tal que E ∈ Ac.
        Inicializar las distancias de los vértices en E a 0 y las distancias de los vértices no en E a un valor muy grande o infinito.
        Considerar las aristas de E primero
        Actualizar las distancias solo si el peso de la arista candidata es menor
'''
'''
    Ejercicio 20

    Algoritmo matriz_AACM(G)
    n = número de vértices en G
    M = matriz de tamaño n x n inicializada con ceros
    
    Para cada vértice u de 0 a n-1:
        Para cada vértice v de u+1 a n-1:
            M[u, v] = 1
    
    Devolver M
'''
'''
    Ejercicio 21
'''
'''
def deleteBidirecction(graph):
    for i in graph:
        nodo = i.head.nextNode
        letter = nodo.value
        while nodo != None:
            if isinstance(letter, str):
                delete(i, letter)
            nodo = nodo.nextNode
            if nodo != None:
                letter = nodo.value
'''

def dijkstra(graph,s,r):
    n = len(graph)
    initRelax(graph, s)
    S = LinkedList()
    Q = LinkedList()
    enqueue(Q, graph[hash(s, n)].head)
    while Q.head != None:
        nodo = dequeue(Q)
        u = nodo
        add(S, u.value[0])
        nodo = nodo.nextNode
        while nodo != None:
            if search(S, nodo.value[0]) == None:
                v = graph[hash(nodo.value[0],n)]
                w = nodo.value[1]
                relax(u.value, v.head.value, w, Q, graph)
            nodo = nodo.nextNode
    return shortestPath(graph, s, r, n)
def shortestPath(graph, s, v, n):
    path = LinkedList()
    add(path,v)
    while True:
        father = graph[hash(v,n)].head.value[2]
        add(path, father)
        if father == s:
            break
        else:
            v = father
    return path
def minQueue(graph, Q):
    for i in graph:
        if i.head.value[1] != None:
            nodo = Node()
            nodo.value = i.head
            if Q.head == None:
                Q.head = nodo
                break
def initRelax(graph,s):
    n = len(graph)
    for i in graph:
        letter = i.head.value
        i.head.value = [letter, None, None]
    graph[hash(s,n)].head.value[1] = 0
def relax(u,v, w, Q, graph):
    if v[1] == None or v[1] > (u[1] + w):
        v[1] = u[1] + w
        v[2] = u[0]
        enqueue(Q, graph[hash(v[0],5)].head)
        

letters = ["a", "b", "c", "d", "e"]
tupple = [("a","b", 5),("a","c", 10),("b","c", 3),("b","d", 2),("b","e", 9),("c","b", 2),("c","e", 1),("d","a", 7),("d","e", 6),("e","d", 4)]

graph = createGraph(letters, tupple)
print(graph)
dijkstra(graph, "a", "e")
