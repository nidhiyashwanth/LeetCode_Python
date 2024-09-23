class Solution:
    def hasCycle(self, N, edges):
        adjacency_list = {}
        visited = {}

        for vertex in range(N):
            adjacency_list[vertex] = []
            visited[vertex] = "white"
        
        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]

            adjacency_list[v1].append(v2)
        
        # returns true if cycle detected vice versa.
        def dfs(vertex):
            visited[vertex] = "gray"

            for neighbor_vertex in adjacency_list[vertex]:
                if visited[neighbor_vertex] == "gray":
                    return True
                if visited[neighbor_vertex] == "white" and dfs(neighbor_vertex):
                    return True
            visited[vertex] = "black"
            return False
        
        for vertex in range(N):
            if visited[vertex] == "white":
                if dfs(vertex):
                    return True
        
        return False