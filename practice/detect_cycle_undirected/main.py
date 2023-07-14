class Solution:
    def hasCycle(self, N, edges):
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
        
        for vertex in range(N):
            if not visited[vertex]:
                if dfs(vertex, -1):
                    return True
        return False
    

    # Time complexity : O(V + E)
    # Space complexity : O(V + E)
    