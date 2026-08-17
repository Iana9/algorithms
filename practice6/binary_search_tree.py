from __future__ import annotations

from typing import Generic, Optional, TypeVar

KEY = TypeVar("KEY")
VALUE = TypeVar("VALUE")


class BinarySearchTree(Generic[KEY, VALUE]):
    """
    Бинарное дерево поиска (BST).

    Для каждого узла:
    - все ключи слева меньше ключа узла
    - все ключи справа больше ключа узла
    """

    class Node:
        """Узел дерева. Хранит ключ, значение и ссылки на дочерние узлы."""

        def __init__(self, key: KEY, value: VALUE) -> None:
            self.key = key
            self.value = value
            self.left: BinarySearchTree.Node | None = None
            self.right: BinarySearchTree.Node | None = None

    class _RemovedValue:
        """Вспомогательный класс, чтобы вернуть значение из рекурсивного remove_node."""

        def __init__(self) -> None:
            self.value: VALUE | None = None

    def __init__(self) -> None:
        # Корень дерева. Если дерево пустое, root is None.
        self._root: BinarySearchTree.Node | None = None

    def get(self, key: KEY) -> Optional[VALUE]:
        """Поиск значения по ключу. Если ключ не найден — None."""
        current = self._root

        # Идем по дереву, пока не дойдем до None или нужного ключа
        while current is not None:
            if key == current.key:
                # Ключ найден
                return current.value
            if key < current.key:
                # Искомый ключ меньше текущего -> идем влево
                current = current.left
            else:
                # Искомый ключ больше текущего -> идем вправо
                current = current.right

        # Дошли до None, значит ключ не найден
        return None

    def add(self, key: KEY, value: VALUE) -> None:
        """Вставка пары ключ-значение. Если ключ уже есть — перезапись."""
        # Если дерево пустое, создаем первый узел
        if self._root is None:
            self._root = self.Node(key, value)
            return

        current = self._root

        while True:
            if key == current.key:
                # Такой ключ уже есть -> просто меняем значение
                current.value = value
                return
            if key < current.key:
                # Новый ключ меньше -> пробуем вставить слева
                if current.left is None:
                    current.left = self.Node(key, value)
                    return
                current = current.left
            else:
                # Новый ключ больше -> пробуем вставить справа
                if current.right is None:
                    current.right = self.Node(key, value)
                    return
                current = current.right

    def remove(self, key: KEY) -> Optional[VALUE]:
        """Удаление узла по ключу. Возвращает значение удаленного узла или None."""
        # В этой переменной сохраним значение удаленного узла
        removed_value = self._RemovedValue()
        self._root = self._remove_node(self._root, key, removed_value)
        return removed_value.value

    def _remove_node(
        self,
        node: Node | None,
        key: KEY,
        removed_value: _RemovedValue,
    ) -> Node | None:
        """Рекурсивное удаление узла из поддерева с корнем node."""
        # Базовый случай: поддерево пустое, ключ не найден
        if node is None:
            return None

        if key < node.key:
            # Ключ меньше текущего -> ищем в левом поддереве
            node.left = self._remove_node(node.left, key, removed_value)
            return node

        if key > node.key:
            # Ключ больше текущего -> ищем в правом поддереве
            node.right = self._remove_node(node.right, key, removed_value)
            return node

        # key == node.key -> нашли узел, который нужно удалить
        removed_value.value = node.value

        # Случай 1: нет левого ребенка
        if node.left is None:
            # Поднимаем правое поддерево на место текущего узла
            return node.right

        # Случай 2: нет правого ребенка
        if node.right is None:
            # Поднимаем левое поддерево на место текущего узла
            return node.left

        # Случай 3: два ребенка
        # Берем минимальный ключ из правого поддерева (самый левый узел справа)
        min_in_right = self._find_min_node(node.right)

        # Копируем ключ и значение преемника в текущий узел
        node.key = min_in_right.key
        node.value = min_in_right.value

        # Удаляем преемника из правого поддерева
        node.right = self._remove_node(
            node.right,
            min_in_right.key,
            self._RemovedValue(),
        )

        return node

    def _find_min_node(self, node: Node) -> Node:
        """Находит узел с минимальным ключом в поддереве. В BST это самый левый узел."""
        current = node
        while current.left is not None:
            current = current.left
        return current
