# python3

import sys
import threading

class Node:
    def __init__(self, key):
        self.key = key
        self.childrens = []

    def __eq__(self, other):
        return self.key == other.key

    def addChildren(self, node):
        self.childrens.append(node)

    def __str__(self):
        return 'Node: %s, childrens: %s' % (self.key, self.childrens)

class Tree:
    def __init__(self, n):
        self.nodes = []
        self.root = None
        for i in range(0, n):
            node = Node(i)
            self.nodes.append(node)


    def height(self):
        max_height = 1
        level = 0
        if len(self.root.childrens) > 0:
            childrens = self.root.childrens
            ancestors = [] + self.root.childrens
            while(len(ancestors) > 0):
                max_height += 1
                new_ancestors = []
                for x in ancestors:
                    new_ancestors += x.childrens
                ancestors = new_ancestors

        return max_height

    def isEmpty(self):
        return  self.root == None

    def __str__(self):
        return 'Root %s' % self.root

def compute_height(n, parents):
    tree = Tree(n)
    for child_index in range(0, n):
        parent_index = parents[child_index]
        if parent_index == -1:
            tree.root = tree.nodes[child_index]
        else:
            tree.nodes[parent_index].addChildren(tree.nodes[child_index])

    return tree.height()


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    # print(compute_height(5, [4, -1, 4, 1, 1]))
    # print(compute_height(5, [-1, 0, 4, 0, 1]))
    # print(compute_height(10, [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
