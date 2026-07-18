from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: Any
    next: "Node"
    prev: "Node"


class LinkedList:
    def __init__(self):
        self.head: Node
        self.tail: Node

    def insert_node(node: Node, inserted_node: Node):
        next = node.next
        prev = next.prev
        

    def remove_node(node: Node):
        pass