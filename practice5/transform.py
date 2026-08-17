from typing import List


def adjacency_matrix_to_edge_list(matrix: List[List[int]]) -> List[List[int]]:
    """
    Преобразование матрицы смежности в список ребер
    """
    edges: List[List[int]] = []

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 1:
                edges.append([i, j])

    return edges


def topological_sort(matrix: List[List[int]]) -> List[int]:
    """
    Топологическая сортировка ориентированного ациклического графа,
    заданного в виде матрицы смежности.
    """
    n = len(matrix)
    in_degree = [0] * n

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                in_degree[j] += 1

    queue = [node for node in range(n) if in_degree[node] == 0]
    result: List[int] = []

    while queue:
        node = queue.pop(0)
        result.append(node)

        for next_node in range(n):
            if matrix[node][next_node] == 1:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    queue.append(next_node)

    return result
