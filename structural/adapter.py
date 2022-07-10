class BritishPlug:
    def request(self) -> str:
        return "British Plug: I work well with standard socket in the UK."


class PolishPlug:
    def specific_request(self) -> str:
        return "Polish Plug: I work well with standard socket in Poland."


class Adapter(BritishPlug, PolishPlug):
    def request(self) -> str:
        return f"Adapter: {self.specific_request()[:-8:]} the UK."


def client_code(target: "BritishPlug") -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client (UK): I can work just fine with the British plug:")
    target = BritishPlug()
    client_code(target)
    print("\n")

    adaptee = PolishPlug()
    print("Client (UK): But the Polish plug doesn't work:")
    print(f"{adaptee.specific_request()}", end="\n\n")

    print("Client (UK): But I can work with it via the adapter:")
    adapter = Adapter()
    client_code(adapter)
