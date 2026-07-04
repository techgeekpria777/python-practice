def resolve(graph, target):
    visited = set()
    def dfs(service):
        for dep in graph.get(service, []):
            if dep not in visted:
                visited.add(dep)
                dfs(dep)
    dfs(target)
    return list(visited)

def main():
    graph = {"Auth": ["DB"], "API": ["Auth", "Cache"], "DB": ["Sidecar"]}
    print(resolve(graph, "API"))

if __name__ == "__main__":
    main()