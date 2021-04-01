from queue import Queue
t = int(input())

for casenum in range(1, t+1):
    r, c = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(r)]

    result = 0
    di = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    heap = []
    
    for i in range(r):
        for j in range(c):
            q = Queue()
            q.put((i,j))
            while not q.empty():
                cr, cc = q.get()
                for dr, dc in di:
                    nr, nc = cr + dr, cc + dc
                    if nr >= 0 and nr < r and nc >= 0 and nc < c:
                        if grid[nr][nc] >= grid[cr][cc]:
                            continue
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

'''
