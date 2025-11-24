import heapq
from typing import TypeVar, Generic

_T = TypeVar('_T')


class PriorityQueue(Generic[_T]):

    def __init__(self):
        self._queue = []
        self._index = 0 # 将具有相同优先级的元素以适当的顺序排列

    def push(self, item: _T, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self) -> _T:
        return heapq.heappop(self._queue)[-1]
