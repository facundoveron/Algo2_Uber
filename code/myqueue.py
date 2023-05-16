import linkedList

def enqueue(Q,element):
    linkedList.add(Q,element)

def dequeue(Q):
    currentNode = Q.head
    if currentNode == None: return
    while currentNode != None:
        if currentNode.nextNode == None:
            break
        currentNode = currentNode.nextNode
    value = currentNode.value
    linkedList.delete(Q, value)
    return value    