from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class BuilderHouse(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_garage(self) -> None:
        pass

    @abstractmethod
    def produce_garden(self) -> None:
        pass

    @abstractmethod
    def produce_statue(self) -> None:
        pass


class ConcreteBuilderHouse1(BuilderHouse):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def produce_garage(self) -> None:
        self._product.add("Garage 1")

    def produce_garden(self) -> None:
        self._product.add("Garden 1")

    def produce_statue(self) -> None:
        self._product.add("Statue 1")


class Product1:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> BuilderHouse:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderHouse) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_garage()

    def build_full_featured_product(self) -> None:
        self.builder.produce_garage()
        self.builder.produce_garden()
        self.builder.produce_statue()


if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilderHouse1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Custom product: ")
    builder.produce_garage()
    builder.produce_garden()
    builder.product.list_parts()
