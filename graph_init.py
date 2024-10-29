import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Kharkiv subway stations
# green line
peremoga = "Перемога"
naukova = "Наукова"
derzhprom = "Держпром"
architect = "Архітектора\nБекетова"
metro_bud = "Метробу-\nдівників"
green_line = [peremoga, naukova, derzhprom, architect, metro_bud]
green_travel_time_min = [10, 3, 5, 7]

# blue line
history_museum = "Історичний\nмузей"
university = "Університет"
yaroslav = "Ярослава\nМудрого"
kyiv = "Київська"
akademic = "Академіка\nБалашова"
student = "Студентська"
blue_line = [history_museum, university, yaroslav, kyiv, student]
blue_travel_time_min = [4, 2, 4, 9]

# red line
vokzal = "Вокзальна"
konst_maidan = "Майдан\nКонституції"
levada = "Левада"
sport = "Спортивна"
turbo_atom = "Турбоатом"
palaz_sport = "Палац\nспорту"
army = "Армійська"
red_line = [vokzal, konst_maidan, levada, sport, palaz_sport]
red_travel_time_min = [6, 3, 4, 6]

# intersections of lines
green_blue_intersection = [derzhprom, university]
green_red_intersection = [metro_bud, sport]
blue_red_intersection = [history_museum, konst_maidan]


def main():
    kharkiv_subway_stations_graph = create_subway_graph()

    display_key_graph_info(kharkiv_subway_stations_graph)

    render_graph(kharkiv_subway_stations_graph)


def create_subway_graph():
    # setup graph
    kharkiv_subway_stations_graph = nx.Graph()

    # add nodes
    kharkiv_subway_stations_graph.add_nodes_from(green_line)
    kharkiv_subway_stations_graph.add_nodes_from(blue_line)
    kharkiv_subway_stations_graph.add_nodes_from(red_line)

    # add edges for each line, with travel time as weight
    kharkiv_subway_stations_graph.add_weighted_edges_from(array_to_pairs(green_line, weights = green_travel_time_min))
    kharkiv_subway_stations_graph.add_weighted_edges_from(array_to_pairs(blue_line, weights=blue_travel_time_min))
    kharkiv_subway_stations_graph.add_weighted_edges_from(array_to_pairs(red_line, weights=red_travel_time_min))

    # add edges for line intersections
    # intersections always have travel_time = 1 minute
    kharkiv_subway_stations_graph.add_weighted_edges_from(array_to_pairs(green_blue_intersection, weights = [1]))
    kharkiv_subway_stations_graph.add_weighted_edges_from(array_to_pairs(green_red_intersection, weights = [1]))
    kharkiv_subway_stations_graph.add_weighted_edges_from(array_to_pairs(blue_red_intersection, weights = [1]))

    return kharkiv_subway_stations_graph


def display_key_graph_info(graph: nx.Graph):
    # display general info about graph

    num_nodes = graph.number_of_nodes()
    print(f"Total number of nodes: {num_nodes}")

    num_edges = graph.number_of_edges()
    print (f"Total number of edges: {num_edges}")

    # degree of each node
    for node in graph.nodes:
        degree = len(graph[node])
        print(f"Degree of node \'{node}\' is {degree}")


def render_graph(graph):
    # do this to get stable rendering of graph (instead of random each time)
    np.random.seed(43)

    # prepare colors for rendering
    node_colors = []
    for node in graph.nodes:
        if node in green_line: node_colors.append("green")
        if node in blue_line: node_colors.append("tab:blue")
        if node in red_line: node_colors.append("red")

    # display graph
    plt.figure(3, figsize=(17, 13)) 
    pos = nx.spring_layout(graph, k = 0.7)
    nx.draw(graph, pos, with_labels=True, node_size = 3000, node_color=node_colors, font_size = 8, width = 2)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size = 8)
    plt.show()


# turn arrays like '[1, 2, 3, 4]' into array of pair tuples,
# like [(1, 2), (2, 3), (3, 4)].
# in case when weights presented, adds it as third element of each tuple
def array_to_pairs(array: list, weights: list = None) -> list:
    if len(array) <= 1:
        # impossible to build arrays of pairs
        return []
    
    result = []
    for i in range(1, len(array)):
        first = array[i - 1]
        second = array[i]

        if weights is not None:
            result.append((first, second, weights[i - 1]))
        else:
            result.append((first, second))

    return result


if __name__ == '__main__':
    main()