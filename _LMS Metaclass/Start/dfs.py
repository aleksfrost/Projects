from graph import *

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(d)
a.point_to(c)
g = Graph(a)


print(g.dfs())
assert g.dfs() == [a, b, d, c]
