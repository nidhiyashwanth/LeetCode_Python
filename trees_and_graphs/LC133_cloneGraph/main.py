class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node):
        visited = {}
        node_clone = Node(node.val, [])
        visited[node] = node_clone
        
        stack = [node]
        while stack:
            popped = stack.pop()
            for neighbor in popped.neighbors:
                if neighbor not in visited:
                    neighbor_clone = Node(neighbor.val, [])
                    visited[neighbor] = neighbor_clone
                    stack.append(neighbor)
                visited[popped].neighbors.append(visited[neighbor])
        return node_clone
