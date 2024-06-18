# edge.py

class AdjNode:
    def __init__(self, target, capacity, cost):
        self.target = target
        self.capacity = capacity
        self.cost = cost

    def __str__(self):
        return f"{self.target}({self.capacity}, {self.cost})"

class AdjFlow(AdjNode):
    def __init__(self, target, capacity, cost, flow=0):
        super().__init__(target, capacity, cost)
        self.flow = flow

    def __str__(self):
        return f"{self.target}({self.flow}/{self.capacity}, {self.cost})"
