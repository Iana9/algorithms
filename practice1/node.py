from typing import List
from .edge import Edge


class Node:
    def __init__(self, name):
        self.name: str = name
        self.connections: List[Edge] = []

    def connect(self, other: Node, cap: int, loss: float):
        self.connections.append(Edge(target=other, speed=cap, loss=loss))
        other.connections.append(Edge(target=self, speed=cap, loss=loss))

    def show(self):
        print(self.name + " -> ")
        for c in self.connections:
            print(f"{c} | ")
        print()