from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractChairFactory(ABC):
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass

    @abstractmethod
    def create_armchair(self) -> AbstractArmchair:
        pass


class ConcreteChairFactory1(AbstractChairFactory):
    def create_chair(self) -> AbstractChair:
        return ConcreteChair1()

    def create_armchair(self) -> AbstractArmchair:
        return ConcreteArmchair1()


class ConcreteChairFactory2(AbstractChairFactory):
    def create_chair(self) -> AbstractChair:
        return ConcreteChair2()

    def create_armchair(self) -> AbstractArmchair:
        return ConcreteArmchair2()


class AbstractChair(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class ConcreteChair1(AbstractChair):
    def useful_function_a(self) -> str:
        return "The result of the chair 1"


class ConcreteChair2(AbstractChair):
    def useful_function_a(self) -> str:
        return "The result of the chair 2"


class AbstractArmchair(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractChair) -> str:
        pass


class ConcreteArmchair1(AbstractArmchair):
    def useful_function_b(self) -> str:
        return "The result of the armchair 1"

    def another_useful_function_b(self, collaborator: AbstractChair) -> str:
        return f"Is is result of collaboration with {collaborator.useful_function_a()}"


class ConcreteArmchair2(AbstractArmchair):
    def useful_function_b(self) -> str:
        return "The result of the armchair 2"

    def another_useful_function_b(self, collaborator: AbstractChair) -> str:
        return f"Is is result of collaboration with {collaborator.useful_function_a()}"


def client_code(factory: AbstractChairFactory):
    product_a = factory.create_chair()
    product_b = factory.create_armchair()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteChairFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteChairFactory2())
