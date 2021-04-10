

class Solution:
    def wallsAndGates(self, rooms) :
        """
        Do not return anything, modify rooms in-place instead.
        """
        from queue import Queue
        import sys
        row, column = len(rooms), len(rooms[0])
        queue = Queue()
        # queue1 = Queue()
        for i in range(row):
            for j in range(column):
                if rooms[i][j] == 0:
                    queue.put((i,j))
                    
        distance = ((0,-1),(-1,0),(0,1),(1,0))

        while not queue.empty():
             
            r , c = queue.get()

            for d in distance:
                n_r, n_c = r+d[0],c+d[1]

                if row > n_r >= 0 and column > n_c >= 0:
                    if rooms[n_r][n_c] == sys.maxsize:
                        queue.put((n_r,n_c))
                        rooms[n_r][n_c] = rooms[r][c]+1
                    



rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

s=  Solution()

s.wallsAndGates(rooms)

print(rooms)

