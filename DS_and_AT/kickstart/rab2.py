from queue import Queue
from heapq import heapify, heappop, heappush
t = int(input())

for casenum in range(1, t+1):
    r, c = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(r)]

    result = 0
    di = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    heap = []
    originals=set()
    for x in range(r):
        for y in range(c):
            if grid[x][y] > 0:
                heap.append((-grid[x][y], x, y))
                originals.add((x,y))

    heapify(heap)

    while heap:
        _, i, j = heappop(heap)
        if (i,j) not in originals:
            continue
        q = Queue()
        q.put((i,j))
        visited =set((i,j))
        while not q.empty():
            cr, cc = q.get()
            for dr, dc in di:
                nr, nc = cr + dr, cc + dc
                if nr >= 0 and nr < r and nc >= 0 and nc < c:
                    if grid[nr][nc] >= grid[cr][cc] or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    if (nr,nc) in originals:
                        originals.remove((nr,nc))
                    diff = abs(grid[cr][cc] - grid[nr][nc])
                    if diff <= 1:
                        continue
                    else:
                        grid[nr][nc] += diff - 1
                        q.put((nr,nc))
                        result += diff - 1
    print(f'Case #{casenum}: {result}')


'''
1
3 4
2 0 0 6
0 0 0 0
5 0 0 3
3
1 3
3 4 3
1 3
3 0 0
3 3
0 0 0
0 2 0
0 0 0

'''

