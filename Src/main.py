# main.py

from graph import Graph
from edge import AdjFlow

def parse_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    num_nodes, num_arcs, source_node, sink_node = map(int, lines[0].strip().split())
    adjacence_list = [[] for _ in range(num_nodes)]
    for line in lines[1:]:
        u, v, capacity, cost = map(int, line.strip().split())
        adjacence_list[u].append(AdjFlow(v, capacity, cost))
    return Graph(adjacence_list, num_nodes), source_node, sink_node

def main():
    filename = 'path_to_your_file.txt'  # Replace with your file path
    graph, source_node, sink_node = parse_input_file(filename)
    print("Original Graph:")
    print(graph)

    max_flow_value, flow_values = graph.max_flow(source_node, sink_node)
    print("\nMaximum Flow Value:", max_flow_value)
    print("Flow Values:", flow_values)

    min_cut_edges = graph.min_cut(source_node)
    print("\nMinimum Cut Edges:")
    for u in min_cut_edges:
        for edge in min_cut_edges[u]:
            print(f"({u}, {edge.target})")

    max_flow_value, min_cost_value, flow_values = graph.max_flow_min_cost(source_node, sink_node)
    print("\nMaximum Flow Minimum Cost Value:", max_flow_value)
    print("Minimum Cost Value:", min_cost_value)
    print("Flow Values:", flow_values)

if __name__ == "__main__":
    main()
