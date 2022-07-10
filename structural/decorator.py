class Component:
    def operation(self) -> str:
        pass


class Person(Component):
    def operation(self) -> str:
        return "Person"


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class Sweater(Decorator):
    def operation(self) -> str:
        return f"Sweater({self.component.operation()})"


class Jacket(Decorator):
    def operation(self) -> str:
        return f"Jacket({self.component.operation()})"


def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    simple = Person()
    print("Client: There is a person:")
    client_code(simple)
    print("\n")

    decorator1 = Sweater(simple)
    decorator2 = Jacket(decorator1)
    print("Client: Now I've got the decorated (with sweater and jacket) person:")
    client_code(decorator2)
