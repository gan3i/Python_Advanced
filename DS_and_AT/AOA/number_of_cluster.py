

def get_cluster(grid):
    def mark_cluster(row, col, current_letter):
        grid[row][col] = 'A'

        for dr, dc in direction:
            nr, nc = row + dr, col + dc
            if 0<= nr  < R and 0 <= nc < C and grid[nr][nc] == current_letter:
                mark_cluster(nr, nc, current_letter)
                
    if not grid or not grid[0]:
        return 0
    R = len(grid)
    C = len(grid[0])
    direction = [[0,1], [0,-1], [1,0],[-1,0]]
    cluster_count = 0

    for row in range(R):
        for col in range(C):
            curr_letter = grid[row][col]
            if curr_letter != 'A':
                mark_cluster(row, col, curr_letter)
                cluster_count +=1

    return cluster_count

cluster = [["a","a", "a"]
          ,["a","a", "a"]
          ,["a","a", "a"]]

print(get_cluster([[]]))




