# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.

# Example 1:
# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.

# Example 2:
# Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.

# Notice
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is
# the same as [1, 0] and thus will not appear together in edges.


class Solution:
    def validTree(self, N, edges):
        adjacency_list = {}
        visited = {}

        for vertex in range(N):
            adjacency_list[vertex] = []
            visited[vertex] = False
        
        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]
            
            adjacency_list[v1].append(v2)
            adjacency_list[v2].append(v1)
        
        def dfs(vertex, parent): #returns true if cycle is detected vice versa
            visited[vertex] = True
            
            for neighbor_vertex in adjacency_list[vertex]:
                if not visited[neighbor_vertex]:
                    if dfs(neighbor_vertex, vertex):
                        return True
                else:
                    if neighbor_vertex != parent:
                        return True
            return False
        
        if dfs(0, -1):
            return False
        
        for vertex in range(N):
            if not visited[vertex]:
                return False
        
        return True
    
    # Time Complexity: O(V + E)
    # Space Complexity: O(V + E)