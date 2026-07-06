from typing import List
from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        ans = float('inf')

        def dfs(node):
            nonlocal ans

            visited.add(node)

            for nei, dist in graph[node]:
                ans = min(ans, dist)

                if nei not in visited:
                    dfs(nei)

        dfs(1)

        return ans
    
#Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
#Output: 2
