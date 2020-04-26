


adj =  {"s":["a","x"],
        "a":["z","s"],
        "z":[],
        "x":["s","d","c"],
        "d":["x","c","f"],
        "c":["x","d","f","v"],
        "f":["c","d","v"],
        "v":["f","v"]}

def bfs(s,adj):
    level = {s : 0}
    parent = {s : None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                 if v not in level:
                     level[v] = i
                     parent[v] = u
                     next.append(v)
        frontier = next
        i= i+1
    print(level)
    print(parent)
bfs("s",adj)




