from practice1.solution import Solution


def main():
    print("Визуализация представления графа")
    print("\n\nСпособ 1. Массив:")
    net = Solution.matrixNet()
    print(net)

    for i in range(6):
        for j in range(6):
            val = net[i][j]
            cell = val if val is not None else "[---------]"
            print(f"{cell!s:<12}", end="")
            print()

    print("\n\nСпособ 2. Узлы:")
    print_node(Solution.nodeNet())

def print_node(node):
    visited = set()
    dfs(node, visited)

def dfs(node, visited: set):
    if node is None or node in visited:
        return

    visited.add(node)
    node.show()

    for edge in node.connections:
        dfs(edge.target, visited)


main()