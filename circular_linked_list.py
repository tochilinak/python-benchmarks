from __future__ import annotations

from collections.abc import Iterator
from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Node | None = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self) -> Iterator[Any]:
        node = self.head
        while self.head:
            yield node.data
            node = node.next
            if node == self.head:
                break

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def __repr__(self):
        return "->".join(str(item) for item in iter(self))

    def insert_tail(self, data: Any) -> None:
        self.insert_nth(len(self), data)

    def insert_head(self, data: Any) -> None:
        self.insert_nth(0, data)

    def insert_nth(self, index: int, data: Any) -> None:
        if index < 0 or index > len(self):
            raise IndexError("list index out of range.")
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node  # first node points itself
            self.tail = self.head = new_node
        elif index == 0:  # insert at head
            new_node.next = self.head
            self.head = self.tail.next = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            if index == len(self) - 1:  # insert at tail
                self.tail = new_node

    def delete_front(self):
        return self.delete_nth(0)

    def delete_tail(self) -> Any:
        return self.delete_nth(len(self) - 1)

    def delete_nth(self, index: int = 0) -> Any:
        if not 0 <= index < len(self):
            raise IndexError("list index out of range.")
        delete_node = self.head
        if self.head == self.tail:  # just one node
            self.head = self.tail = None
        elif index == 0:  # delete head node
            self.tail.next = self.tail.next.next
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
            if index == len(self) - 1:  # delete at tail
                self.tail = temp
        return delete_node.data

    def is_empty(self) -> bool:
        return len(self) == 0
