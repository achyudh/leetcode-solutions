class Solution:
    
    def dfs(self, graph, visited, source):
        stack = [source]
        while stack:
            curr_node = stack.pop()
            if not visited[curr_node]:
                visited[curr_node] = True
                for neighbour in graph[curr_node]:
                    stack.append(neighbour)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        num_components = 0
        
        if grid:
            m = len(grid)
            n = len(grid[0])
            graph = [list() for x in range(m * n)]
            visited = [False for x in range(m * n)]

            for i0 in range(m):
                for j0 in range(n):
                    if grid[i0][j0]  == '1':
                        curr_node = n * i0 + j0

                        if i0 and grid[i0 - 1][j0] == '1':
                            graph[curr_node].append(n * (i0 - 1) + j0)

                        if j0 and grid[i0][j0 - 1] == '1':
                            graph[curr_node].append(n * i0 + j0 - 1)

                        if i0 < m - 1 and grid[i0 + 1][j0] == '1':
                            graph[curr_node].append(n * (i0 + 1) + j0)

                        if j0 < n - 1 and grid[i0][j0 + 1] == '1':
                            graph[curr_node].append(n * i0 + j0 + 1)

            for i0 in range(m):
                for j0 in range(n):
                    if grid[i0][j0] == '1' and not visited[n * i0 + j0]:
                        self.dfs(graph, visited, n * i0 + j0)
                        num_components += 1
                        
        return num_components
