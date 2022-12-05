"""
Detect cycle in a directed graph
Problem Statement
Given a directed graph, detect whether the graph contains cycle or not.

Input and Output Specification

def solution(X, B)

Input 
The number of nodes and list of edges are passed as two parameters of the solution function.
The first parameter size is number of nodes in the graph.
The second parameter edges is array of integers that represents edges of the directed graph. The array may be empty (representing no edges). If the array is not empty, it will have an even number of elements. Each edge is represented by a pair of node identifiers.
This input:
4, [0,1,1,2,2,3,3,0]
Has four nodes and four edges:
[0->1], [1->2], [2->3], [3->0]
Represents this graph:
0 ------------> 1
|                             |
|                             |   
|                             |
|                             |
3 <------------ 2

This graph has cycle 0->1->2->3->0.

Output
Function solution must return true if the graph contains a cycle or false otherwise.

Example
Input 3, [0,1,1,2,2,0]
Output
true
"""

# Solution:
def solution(X, B):
    # create an adjacency list from the input
    adj_list = {}
    for i in range(0, len(B), 2):
        from_node = B[i]
        to_node = B[i+1]
        if from_node in adj_list:
            adj_list[from_node].append(to_node)
        else:
            adj_list[from_node] = [to_node]
    
    # traverse the graph and detect any cycles
    visited = set()
    for node in range(X):
        if node in visited:
            continue
        if dfs(node, adj_list, visited, [-1]):
            return True
    return False
        
def dfs(node, adj_list, visited, path):
    # base case
    if node in path:
        return True
    
    # recursive case
    visited.add(node)
    path.append(node)
    if node in adj_list:
        for neighbor in adj_list[node]:
            if dfs(neighbor, adj_list, visited, path):
                return True
    path.pop()
    return False
