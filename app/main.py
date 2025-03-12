def hello_world(phrase: str) -> None:
    if phrase:
        print(f"Hello {phrase}!")
    else:
        print("Hello World!")


def main() -> None:
    hello_world("")
    hello_world("Pymentos")


if __name__ == "__main__":
    main()
