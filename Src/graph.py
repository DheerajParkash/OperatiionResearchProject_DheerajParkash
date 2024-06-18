# graph.py

from edge import AdjNode, AdjFlow

class Graph:
    def __init__(self, adjacence_list, n):
        self.n = n
        self.adjacence_list = adjacence_list

    def __str__(self):
        string = ""
        for i, adj_lts in enumerate(self.adjacence_list):
            string += f"{i} -> "
            for edge in adj_lts:
                string += str(edge) + ' , '
            string += "\n"
        return string

    def residual_graph_cost(self):
        residual_adjacency_list = [[] for _ in range(self.n)]
        for source_node, adj_lts in enumerate(self.adjacence_list):
            for edge in adj_lts:
                if not isinstance(edge, AdjFlow):
                    raise ValueError("The graph given is not a flow graph")
                forward_capacity = edge.capacity - edge.flow
                backward_capacity = edge.flow
                forward_cost = edge.cost
                backward_cost = -edge.cost
                if forward_capacity != 0:
                    forward_edge = AdjNode(edge.target, forward_capacity, forward_cost)
                    residual_adjacency_list[source_node].append(forward_edge)
                if backward_capacity != 0:
                    backward_edge = AdjNode(source_node, backward_capacity, backward_cost)
                    residual_adjacency_list[edge.target].append(backward_edge)
        return Graph(residual_adjacency_list, self.n)

    def bellman_ford_cost(self, source):
        distance = [float('inf')] * self.n
        distance[source] = 0
        predecessor = [-1] * self.n
        predecessor[source] = source
        for _ in range(self.n):
            updated = False
            for u in range(self.n):
                for edge in self.adjacence_list[u]:
                    v = edge.target
                    if distance[u] + edge.cost < distance[v]:
                        distance[v] = distance[u] + edge.cost
                        predecessor[v] = u
                        updated = True
            if not updated:
                break
        for u in range(self.n):
            for edge in self.adjacence_list[u]:
                v = edge.target
                if distance[u] + edge.cost < distance[v]:
                    raise ValueError(f"Negative cycle in edge {u} -> {v}")
        return distance, predecessor

    def max_flow_min_cost(self, source, sink):
        max_flow = 0
        min_cost = 0
        flow_values = []
        while True:
            residual_graph = self.residual_graph_cost()
            distance, predecessor = residual_graph.bellman_ford_cost(source)
            if distance[sink] == float('inf'):
                break
            bottleneck_capacity = float('inf')
            node = sink
            while node != source:
                predecessor_node = predecessor[node]
                for edge in residual_graph.adjacence_list[predecessor_node]:
                    if edge.target == node:
                        bottleneck_capacity = min(bottleneck_capacity, edge.capacity)
                        break
                node = predecessor_node
            node = sink
            while node != source:
                predecessor_node = predecessor[node]
                for i, edge in enumerate(self.adjacence_list[predecessor_node]):
                    if edge.target == node:
                        self.adjacence_list[predecessor_node][i].flow += bottleneck_capacity
                        min_cost += bottleneck_capacity * edge.cost
                        flow_values.append(self.adjacence_list[predecessor_node][i].flow)
                        break
                node = predecessor_node
            max_flow += bottleneck_capacity
        return max_flow, min_cost, flow_values

    def min_cut(self, source):
        distance, _ = self.residual_graph_cost().bellman_ford_cost(source)
        min_cut = {}
        for u, adj in enumerate(self.adjacence_list):
            for edge in adj:
                if distance[u] != float('inf') and distance[edge.target] == float('inf'):
                    if u in min_cut:
                        min_cut[u].append(edge)
                    else:
                        min_cut[u] = [edge]
        return min_cut

    def max_flow(self, source, sink):
        max_flow, _, flow_values = self.max_flow_min_cost(source, sink)
        return max_flow, flow_values
