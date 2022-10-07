graph={
    'A':[[3,'B'],[7,'D']],
    'B':[[2,'C'],[4,'D']],
    'C':[[8,'E']],
    'D':[],
    'E':[[8,'C']],
    'F':[]
}

visited = set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
            

print("Following is dbs list")
dfs(visited,graph,'A')