from __future__ import annotations

from typing import Any, Iterator, Optional


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None
        # Флаг «узел ещё в списке». В _remove_node нужно будет поставить False.
        self._valid = True


class Position:
    def __init__(self, node: Node, linked_list: "LinkedList") -> None:
        self._node = node
        self._list = linked_list

    def _check_valid(self) -> None:
        if not self._node._valid:
            raise ValueError("Узел удалён из списка")

    def is_end(self) -> bool:
        return self._node is self._list._tail


class LinkedList:
    def __init__(self) -> None:
        self._head: Node = Node(None)
        self._tail: Node = Node(None)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        current = self._head.next
        while current is not self._tail:
            yield current.value
            current = current.next

    # --- позиции ---

    def begin(self) -> Position:
        return Position(self._head.next, self)

    def end(self) -> Position:
        return Position(self._tail, self)

    # --- вставка ---

    def insert_begin(self, value: Any) -> Position:
        new_node = Node(value)
        new_node.next = self._head.next
        new_node.prev = self._head
        self._head.next.prev = new_node
        self._head.next = new_node
        self._size += 1
        return Position(new_node, self)

    def insert_end(self, value: Any) -> Position:
        new_node = Node(value)
        new_node.next = self._tail
        new_node.prev = self._tail.prev
        self._tail.prev.next = new_node
        self._tail.prev = new_node
        self._size += 1
        return Position(new_node, self)

    def insert_at(self, position: Position, value: Any) -> Position:
        new_node = Node(value)
        new_node.next = position._node
        new_node.prev = position._node.prev
        position._node.prev.next = new_node
        position._node.prev = new_node
        self._size += 1
        return Position(new_node, self)

    # --- удаление ---

    def remove_begin(self) -> Any:
        if self._size == 0:
            raise ValueError("Список пуст")
        node = self._head.next
        self._head.next = node.next
        node.next.prev = self._head
        node._valid = False
        self._size -= 1
        return node.value

    def remove_end(self) -> Any:
        if self._size == 0:
            raise ValueError("Список пуст")
        node = self._tail.prev
        self._tail.prev = node.prev
        node.prev.next = self._tail
        node._valid = False
        self._size -= 1
        return node.value

    def remove_at(self, position: Position) -> Any:
        if self._size == 0:
            raise ValueError("Список пуст")
        node = position._node
        node.prev.next = node.next
        node.next.prev = node.prev
        node._valid = False
        self._size -= 1
        return node.value

    # --- доступ ---

    def get_at(self, position: Position) -> Any:
        if self._size == 0:
            raise ValueError("Список пуст")
        return position._node.value

    def replace_at(self, position: Position, value: Any) -> None:
        if self._size == 0:
            raise ValueError("Список пуст")
        position._node.value = value

    def contains(self, value: Any) -> bool:
        if self._size == 0:
            return False
        current = self._head.next
        while current is not self._tail:
            if current.value == value:
                return True
            current = current.next
        return False

    def find(self, value: Any) -> Optional[Position]:
        if self._size == 0:
            return None
        current = self._head.next
        while current is not self._tail:
            if current.value == value:
                return Position(current, self)
            current = current.next
        return None

    def _remove_node(self, node: Node) -> Any:
        node.prev.next = node.next
        node.next.prev = node.prev
        node._valid = False
        self._size -= 1
        return node.value
