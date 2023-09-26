from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self, res=None, stack=None) -> list[Node]:
        if res is None:
            res = []
        if stack is None:
            stack = []
        res.append(self._root)
        for x in self._root.outbound[::-1]:
            stack.insert(0, x)
        for y in stack:
            if y not in res:
                Graph(y).dfs(res=res, stack=stack)
        return res

    def bfs(self, res=None, stack=None) -> list[Node]:
        if res is None:
            res = []
        if stack is None:
            stack = []
        res.append(self._root)
        stack.extend(self._root.outbound)
        for y in stack:
            if y not in res:
                Graph(y).bfs(res=res, stack=stack)
        return res

