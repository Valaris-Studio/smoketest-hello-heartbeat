import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="A simple greeting CLI.")
    parser.add_argument("--name", type=str, default=None, help="Name to greet.")
    parser.add_argument("--loud", action="store_true", help="Uppercase the greeting.")
    return parser.parse_args()


def format_greeting(name: str | None, loud: bool) -> str:
    greeting = f"Hello, {name}!" if name else "Hello, world!"
    return greeting.upper() if loud else greeting


def main() -> int:
    args = parse_args()
    print(format_greeting(args.name, args.loud))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
