'''
You are given a tree (a simple connected graph with no cycles). The tree has  nodes numbered from 1 to N and is rooted at node 1.

Find the maximum number of edges you can remove from the tree to get a forest such that each connected component of the forest contains an even number of vertices.

Input Format

The first line of input contains two integers  and .  is the number of vertices, and  is the number of edges.
The next  lines contain two integers  and  which specifies an edge of the tree.


Note: The tree in the input will be such that it can always be decomposed into components containing an even number of nodes.

Output Format

Print the number of removed edges.   '''
class node:

    def __init__(self, data):
        self._data = data
        self._children = []

    def getdata(self):
        return self._data

    def getchildren(self):
        return self._children

    def add(self, node):
        self._children.append(node)

class tree:

    def __init__(self):
        self._head = node('header')

    def linktohead(self, node):
        self._head.add(node)

    def countchild(self, node):
        a = 0
        a += len(node.getchildren())
        for child in node.getchildren():
            a += self.countchild(child)
        return a

n, m = map(int, input().split(" "))
a1 = node(1)
for _ in range(m):
    a, b = input().split(" ")
    exec("{0} = node({1})".format("a" + a, a))
    exec("{0}.add({1})".format("a" + b, "a" + a))

tree = tree()
tree.linktohead(a1)
# testcase
dict1 = {}
for z in range(2, n + 1):
    if (eval("tree.countchild(a{})".format(z)) + 1) % 2 == 0:
        dict1["a" + str(z)] = eval("tree.countchild(a{})".format(z)) + 1
print(len(dict1))
