import collections

class Solution:
    def orangesRotting(self, grid) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        arr = []

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    arr.append((i, j))
                    visited.add((i, j))

        if arr != []:
            q.append(arr)
        print("Initial q", q)

        def make_neighbors_rot(r, c):
            four_nebrs = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]
            arr = []
            for i, j in four_nebrs:
                if i in range(ROWS) and j in range(COLS) and grid[i][j] == 1 and (i, j) not in visited:
                    grid[i][j] = 2
                    visited.add((i, j))
                    arr.append((i, j))
            return arr

        while q:
            #print("while loop", q)
            arr = q.popleft()
            arr1 = []
            for r, c in arr:
                x = make_neighbors_rot(r, c)
                if x != []:
                    arr1.extend(x)
            if arr1 != []:
                q.append(arr1)
            res += 1

        res -= 1
        return res if res != 0 else -1

s = Solution()
print(s.orangesRotting(grid=[[1,1,0],[0,1,1],[0,1,2]]))