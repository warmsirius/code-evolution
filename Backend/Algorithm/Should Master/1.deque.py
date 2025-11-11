"""
deque: 双端队列
两端皆可进出元素,两端进出时间复杂度均为O(1)
实现方式: 使用双向链表实现
"""
# from collections import deque

# deque_obj = deque()
# deque_obj.append(1)          # 右端添加元素1
# deque_obj.appendleft(2)      # 左端添加元素2

from __future__ import annotations  # 关键：延迟解析类型注解，支持直接写未定义的类型
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Sequence, TypeVar, overload

_T = TypeVar('_T') # TypeVar 允许你定义一个变量，该变量可以代表任何类型或一组类型。

@dataclass
class Node(Generic[_T]): # Generic里面参数是可以处理的类型参数
    val: _T
    last: Node[_T] | None = None
    next: Node[_T] | None = None


# 自实现deque
class Deque(Generic[_T]):
    @overload
    def __init__(self, *, max_len: int | None = None) -> None:...
    
    @overload
    def __init__(self, iterable: Iterable[_T], max_len: int | None = None) -> None:...
    
    def __init__(self, iterable: Iterable[_T] | None = None, max_len: int | None = None) -> None:
        """初始化双端队列
        :param iterable: 可选的可迭代对象，用于初始化队列内容
        :param max_len: 可选的最大长度限制
        """
        self.tail: Node[_T] | None = None
        self.head: Node[_T] | None = None
        self._max_len = max_len
        self._len = 0
        if iterable is not None:
            self._init_from_iterable(iterable)
    
    def _init_from_iterable(self, iterable: Iterable[_T]) -> None:
        """从可迭代对象初始化队列"""
        if self._max_len is not None and self._max_len <= 0:
            return  # 如果最大长度为0或负数，不添加任何元素
        
        # 使用迭代器方式，避免创建中间列表
        iterator = iter(iterable)
        
        # 如果是序列且有最大长度限制，可以直接计算起始位置
        if isinstance(iterable, Sequence) and self._max_len is not None:
            start = max(0, len(iterable) - self._max_len)
            for i in range(start, len(iterable)):
                self._append_direct(iterable[i])
        else:
            # 通用处理方式
            for item in iterator:
                if self._max_len is not None and self._len >= self._max_len:
                    # 如果队列已满，移除头部元素再添加新元素
                    self.popleft()
                self._append_direct(item)

    def _append_direct(self, val: _T) -> None:
        """直接添加元素到队列尾部，不检查长度"""
        cur = Node(val)
        if self.tail is None:
            self.head = cur
            self.tail = cur
        else:
            cur.last = self.tail
            self.tail.next = cur
            self.tail = cur
        
        self._len += 1
    
    def _prepend_direct(self, val: _T) -> None:
        """直接添加元素到头部（不检查长度限制）"""
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.last = node
            self.head = node
        self._len += 1
      
    @property
    def max_len(self) -> int | None:
        return self._max_len
    
    def __len__(self) -> int:
        """支持len()函数"""
        return self._len
    
    def __contains__(self, item: _T) -> bool:
        """支持in操作符"""
        cur = self.head
        while cur is not None:
            if cur.val == item:
                return True
            cur = cur.next
        return False
    
    def __iter__(self) -> Iterator[_T]:
        """支持迭代"""
        cur = self.head
        while cur is not None:
            yield cur.val
            cur = cur.next
    
    def _trim_to_max_len(self) -> None:
        """如果队列超过最大长度，从头部删除多余元素"""
        if self._max_len is None:
            return
        
        while self._len > self._max_len:
            self.popleft()
    
    def is_full(self) -> bool:
        """判断队列是否已满"""
        return self.max_len is not None and self._len >= self._max_len

    def is_empty(self) -> bool:
        return self.head is None
    
    def append(self, val: _T) -> None:
        """右端/从尾部添加元素"""
        # 如果队列已满，先删除头部元素
        if self.is_full():
            self.popleft()
        
        self._append_direct(val)
    
    def appendleft(self, val: _T) -> None:
        """左端/从头部添加元素"""
        # 如果队列已满，先删除尾部元素
        if self.is_full():
            self.pop()
        
        self._prepend_direct(val)
    
    def pop(self) -> _T:
        """右端/从尾部弹出元素"""
        if self.tail is None:
            raise IndexError("pop from an empty deque")
        
        val = self.tail.val
        self.tail = self.tail.last
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return val
    
    def popleft(self) -> _T:
        """左端/从头部弹出元素"""
        if self.head is None:
            raise IndexError("pop from an empty deque")
        
        val = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.last = None
        return val
    
    def peek(self) -> _T:
        """获取右端/尾部元素但不弹出"""
        if self.tail is None:
            raise IndexError("peek from an empty deque")
        return self.tail.val
    
    def peekleft(self) -> _T:
        """获取左端/头部元素但不弹出"""
        if self.head is None:
            raise IndexError("peekleft from an empty deque")
        return self.head.val


if __name__ == "__main__":
    deque_obj = Deque[int](max_len=3)
    deque_obj.append(1)
    deque_obj.append(2)
    deque_obj.append(3)
    print(list(deque_obj)) # 输出: [1, 2, 3]
    
    deque_obj.append(4)  # 队列已满，移除头部元素1
    print(list(deque_obj))  # 输出: [2, 3, 4]
    
    deque_obj.appendleft(0)  # 队列已满，移除尾部元素4
    print(list(deque_obj))  # 输出: [0, 2, 3]
    
    print(deque_obj.pop())      # 输出: 3
    print(deque_obj.popleft())  # 输出: 0
    print(list(deque_obj))      # 输出: [2]


# 问: TypeVar什么时候使用?
# 答:1.泛型函数：当函数参数和返回值的类型相关，但可以是多种类型时。
#    2.泛型类：当类中的多个方法或属性涉及相同类型，但该类型在实例化时才确定时。
#    3. 类型约束：当希望类型变量只能是某些特定类型时（使用边界或约束）。
# 使用之前询问自己几个问题：
# - "函数/方法是否处理多种类型？",
# - "输入和输出类型是否需要保持一致？", 
# - "多个参数是否需要是相同类型？",
# - "是否在创建通用数据结构？",
# - "是否需要类型约束（特定类型或子类）？"
# 记住：TypeVar 的主要价值在于在保持灵活性的同时提供类型安全。
#       当您发现自己在写重复的代码只是类型不同，或者使用 Any 丢失了类型信息时，就是使用 TypeVar 的好时机。


# 问: 什么时候需要继承Generic？
# 答: 当类的行为或存储的数据类型需要在实例化时确定，而不是在类定义时固定。
# 使用之前询问自己这几个问题:
# - 这个类的主要目的是什么？（容器/服务/工具）
# - 需要支持多少种数据类型？（单一/多种）
# - 类型一致性是否重要？（是/否）
# - 这个类会被如何重用？（单一场景/多个场景）
# 记住：Generic 是一把双刃剑。正确使用时，它能提供强大的类型安全和代码复用；错误使用时，它会增加不必要的复杂性。
# 当您不确定时，可以从简单的具体类型开始，等到真正需要泛化时再重构为 Generic。这通常比一开始就过度设计要好
