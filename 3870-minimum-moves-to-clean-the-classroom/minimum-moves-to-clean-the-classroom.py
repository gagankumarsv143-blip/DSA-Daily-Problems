from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find start and assign an index to every litter
        litter = {}
        sr = sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        total = len(litter)

        # No litter
        if total == 0:
            return 0

        target = (1 << total) - 1

        # visited[r][c][mask] is a bitmask of energies
        #
        # Example:
        # if bit 5 is set, we have already visited
        # this (r,c,mask) with energy = 5
        visited = [
            [[0] * (1 << total) for _ in range(n)]
            for _ in range(m)
        ]

        q = deque()

        # state = (row, col, mask, energy)
        q.append((sr, sc, 0, energy))

        # Mark starting state
        visited[sr][sc][0] |= (1 << energy)

        moves = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            # Process one BFS level
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Wall
                    if classroom[nr][nc] == 'X':
                        continue

                    # No energy -> cannot move
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if (nr, nc) in litter:
                        nmask |= 1 << litter[(nr, nc)]

                        # We collected everything
                        if nmask == target:
                            return moves + 1

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    # Check if this exact energy was already visited
                    bit = 1 << ne

                    if visited[nr][nc][nmask] & bit:
                        continue

                    visited[nr][nc][nmask] |= bit

                    q.append((nr, nc, nmask, ne))

            moves += 1

        return -1

