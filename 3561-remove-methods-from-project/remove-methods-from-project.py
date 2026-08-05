from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build directed graph
        adj = [[] for _ in range(n)]

        for u, v in invocations:
            adj[u].append(v)

        # Find all suspicious methods using DFS
        suspicious = [False] * n

        def dfs(node):
            suspicious[node] = True
            for nei in adj[node]:
                if not suspicious[nei]:
                    dfs(nei)

        dfs(k)

        # Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return all non-suspicious methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans