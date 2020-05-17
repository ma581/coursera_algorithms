import random
from typing import Set, Tuple

f = open('kargerMinCut.txt', 'r')
lines = f.read().splitlines()
f.close()
adjacenty_matrix = list(map(lambda line: [int(x) for x in line], map(lambda x: x.split(), lines)))


def min_cut(graph) -> int:
    minimum = len(graph)
    nodes = {x for x in range(1, len(graph) + 1)}
    edges = set()
    for i in range(0, len(graph)):
        for j in range(1, len(graph[i])):
            if (i + 1) != j:
                edges.add((i + 1, j))

    # print(f'Initials edges {edges}')

    edges_to_remove = set()
    for src, dest in edges:
        if (dest, src) in edges and (dest, src) not in edges_to_remove:
            edges_to_remove.add((src, dest))

    edges.difference_update(edges_to_remove)
    # N = len(graph) ** 2
    N = 1

    # print(f'Trimmed edges {edges}')
    for i in range(N):
        m = contract(set(edges), nodes)
        if m < minimum:
            minimum = m

    return minimum


def contract(edges: Set[Tuple[int, int]], nodes: Set):
    while len(nodes) > 2:
        print(f'Edges: {edges}')
        edge = random.choice(list(edges))
        print(f'Removing {edge}')
        edges.remove(edge)
        print(f'After removing {edges}')
        deleted_node = edge[0]
        nodes.remove(deleted_node)
        new_target_node = edge[1]

        edges_to_remove = set()
        edges_to_add = set()
        for src, dest in edges:
            if src == deleted_node:
                edges_to_remove.add((src, dest))
                print(f'Reworking edge ({src},{dest})')
                print(f'Adding edge ({new_target_node},{dest})')
                edges_to_add.add((new_target_node, dest))
            elif dest == deleted_node:
                print(f'Reworking edge ({src},{dest})')
                print(f'Adding edge ({src},{new_target_node})')
                edges_to_remove.add((src, dest))
                edges_to_add.add((src, new_target_node))

        print(f'Edges to remove {edges_to_remove}')
        edges.difference_update(edges_to_remove)
        print(f'Edges after removing changed ones {edges}')
        print(f'Edges to add {edges_to_add}')
        edges.union(edges_to_add)
        print(f'Edges after readding changed ones {edges}')

    return len(edges)


def test_one():
    graph = [[1, 2, 3],
             [2, 1, 3],
             [3, 2, 1]]

    assert 2 == min_cut(graph)


# def test_two():
#     graph = [[1, 2, 3, 4],
#              [2, 1, 3],
#              [3, 2, 1],
#              [4, 1]
#              ]
#
#     assert 1 == min_cut(graph)

# def test_real():
#     print(min_cut(adjacenty_matrix))
#     assert False
