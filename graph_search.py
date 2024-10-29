import graph_init
import networkx as nx

def main():
    # use graph from first task
    subway_graph = graph_init.create_subway_graph()

    # traverse subway graph via dfs and bfs algorigthms
    start_station = graph_init.peremoga
    dfs_path = dfs_path_search(subway_graph, start_station)
    bfs_path = bfs_path_search(subway_graph, start_station)

    print(f"DFS path is: {dfs_path}\n")
    print(f"BFS path is: {bfs_path}\n")

    # confirm correctness of implementations by using buit-in functions of the same algorithms
    dfs_path_check = list(nx.dfs_edges(subway_graph, source = start_station))
    bfs_path_check = list(nx.bfs_edges(subway_graph, source = start_station))

    print(f"DFS path test, path is: {dfs_path_check}\n")
    print(f"BFS path test, path is: {bfs_path_check}\n")


def dfs_path_search(graph, start, visited = None, path = None, parent = None):
    # recursive
    if visited is None:
        visited = set()
        path = []
    
    visited.add(start)
    
    if parent is not None:
        path.append((parent, start))
    for next in graph[start]:
        if next not in visited:
            dfs_path_search(graph, next, visited, path, start)

    return path


def bfs_path_search(graph, start):
    # iterative
    visited, queue = {start}, [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path.append((vertex, neighbour))

    return path


if __name__ == '__main__':
    main()