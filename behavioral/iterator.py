from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class StraightOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: StringsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class StringsCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> StraightOrderIterator:
        return StraightOrderIterator(self._collection)

    def get_reverse_iterator(self) -> StraightOrderIterator:
        return StraightOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = StringsCollection()
    collection.add_item("1")
    collection.add_item("2")
    collection.add_item("3")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")