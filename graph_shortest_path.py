import graph_init
import heapq


def main():
    # use graph from first task
    subway_graph = graph_init.create_subway_graph()

    # calculate path
    shortest_path = dijkstra_shortest_path(subway_graph, graph_init.peremoga)

    # display path
    print(f"Shortest path for subway graph:\n{shortest_path}")


# find shortest path to visit every node
def dijkstra_shortest_path(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0

    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths


if __name__ == '__main__':
    main()