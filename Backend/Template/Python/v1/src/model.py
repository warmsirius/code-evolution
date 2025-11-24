from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import NewType


Quantity = NewType('Quantity', int)
Sku = NewType('Sku', str)
Reference = NewType('Reference', str)


@dataclass(frozen=True)
class OrderLine:
    order_id: str
    sku: str
    qty: int


class Batch:
    def __init__(self, ref: Reference, sku: Sku, qty: Quantity, eta: date | None) -> None:
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty # 初始采购数量
        self._allocations: set[OrderLine] = set() # 已分配的订单行集合 type: Set[OrderLine]

    def allocate(self, line: OrderLine) -> None:
        if self.can_allocate(line):
            self._allocations.add(line)

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty

    def deallocate(self, line: OrderLine) -> None:
        """释放分配"""
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        """已分配数量"""
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        """可用数量"""
        return self._purchased_quantity - self.allocated_quantity

    def __eq__(self, value):
        if not isinstance(value, Batch):
            return False
        return self.reference == value.reference

    def __hash__(self):
        return hash(self.reference)

    def __gt__(self, other: Batch):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta


class OutOfStock(Exception):
    pass


def allocate(line: OrderLine, batches: list[Batch]) -> str:
    try:
        batch = next(
        b for b in sorted(batches) if b.can_allocate(line)
        )
        batch.allocate(line)
        return batch.reference
    except StopIteration as err:
        raise OutOfStock(f'Out of stock for sku {line.sku}') from err
