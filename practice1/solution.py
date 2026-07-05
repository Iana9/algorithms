from .value import Value
from .node import Node
from typing import Optional, List


class Solution:
    @staticmethod
    def matrixNet() -> List[List[Optional[Value]]]:
        net: List[List[Optional[Value]]] = [[None] * 6 for _ in range(6)]

        def add(pair, data) -> None:
            a, b = pair
            w, p = data
            v = Value(int(w), float(p))
            net[a][b] = v
            net[b][a] = v

        # связи
        add((0, 1), (1500, 0.9))
        add((0, 2), (2000, 0.1))
        add((0, 3), (1000, 0.5))
        add((1, 4), (1500, 0.6))
        add((2, 4), (900, 0.05))
        add((2, 5), (500, 0.2))
        add((3, 4), (2500, 0.01))
        add((4, 5), (300, 0.85))

        return net

    @staticmethod
    def nodeNet() -> Node:
        # создаём узлы
        A = Node("A")
        B = Node("B")
        C = Node("C")
        D = Node("D")
        E = Node("E")
        F = Node("F")

        # соединяем их
        A.connect(B, 1500, 0.9)
        A.connect(C, 2000, 0.1)
        A.connect(D, 1000, 0.5)
        B.connect(F, 1500, 0.6)
        C.connect(E, 900, 0.05)
        C.connect(F, 500, 0.2)
        D.connect(E, 2500, 0.01)
        E.connect(F, 300, 0.85)

        # возвращаем ссылку на первый
        return A