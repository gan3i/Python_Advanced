from typing import List
def minimumCost(N: int, connections: List[List[int]]) -> int:
     parents = [x for x in range(N)]
     ranks = [1] * N
     
     def find(u):
         while u != parents[u]:
             parents[u] = parents[parents[u]]
             u = parents[u]
         return u
     
     def union(u, v):
         root_u, root_v = find(u), find(v)
         if root_u == root_v: return False
         if ranks[root_v] > ranks[root_u]:
             root_u, root_v = root_v, root_u
         parents[root_v] = root_u
         ranks[root_u] += ranks[root_v]
         return True
     
     connections.sort(key = lambda x: x[2])
     ans = 0
     for u, v, val in connections:
         if union(u-1, v-1):
              ans += val
     groups = len({find(x) for x in parents})
     return ans if groups == 1 else -1



N = 7
connections = [[2,1,87129],[3,1,14707],[4,2,34505],[5,1,71766],[6,5,2615],[7,2,37352]]

print(minimumCost(N, connections))