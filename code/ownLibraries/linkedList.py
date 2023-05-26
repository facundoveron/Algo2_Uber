#!/usr/bin/env python
# -*- coding: utf-8 -*-

class LinkedList:
    head=None

class Node:
    value=None
    nextNode=None

def add(L, element):
    node = Node()
    node.nextNode = L.head
    node.value = element
    L.head = node

def search(L, element):
    j = 0
    currentNode = L.head
    while currentNode != None:
        if currentNode.value == element:
            return j
        j += 1
        currentNode = currentNode.nextNode

def insert(L, element, position):
    if position == 0: 
        add(L, element)
        return position
    else: 
        length_list = length(L)
        if position <= length_list:
            nodo = Node()
            nodo.value = element            
            currentNode = L.head
            for i in range(0, position - 1):
                currentNode = currentNode.nextNode
            if currentNode.nextNode == None:
                currentNode.nextNode = nodo
                return position
            else:
                nodo.nextNode = currentNode.nextNode
                currentNode.nextNode = nodo
                return position
        else:
            return None

def delete(L, element):
    currentNode = L.head
    pre_currentNode = currentNode
    j = 0
    while currentNode != None:
        if currentNode.value == element:
            if j == 0:
                L.head = currentNode.nextNode
                return j
            else:    
                pre_currentNode.nextNode = currentNode.nextNode
            return j
        
        j += 1
        pre_currentNode = currentNode    
        currentNode = currentNode.nextNode    
    return None                

def length(L):
    j = 0
    currentNode = L.head
    while currentNode != None:
        if currentNode.value != None:
            j += 1
        currentNode = currentNode.nextNode
    return j 

def access(L, position):
    currentNode = L.head
    j = 0
    while currentNode != None:
        if j == position:
            return currentNode.value
        j += 1
        currentNode = currentNode.nextNode
    return None

def update(L, element, position):
    currentNode = L.head
    j = 0
    while currentNode != None:
        if j == position:
            currentNode.value = element
            return j
        j += 1
        currentNode = currentNode.nextNode    
    return None        


def addListBinaryTree(L ,element):
    node = Node()
    node.value = element
    if L.head == None:
        L.head = node
    else:
        currentNode = L.head
        currentNode_ant = L.head
        while currentNode != None:
            currentNode_ant = currentNode
            currentNode = currentNode.nextNode
        currentNode_ant.nextNode = node
