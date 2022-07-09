from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class ConcreteCreator1(AbstractCreator):
    def factory_method(self) -> AbstractProduct:
        return ConcreteProduct1()


class ConcreteCreator2(AbstractCreator):
    def factory_method(self) -> AbstractProduct:
        return ConcreteProduct2()


class AbstractProduct(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(AbstractProduct):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(AbstractProduct):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: AbstractCreator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
