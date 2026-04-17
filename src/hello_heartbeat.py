import argparse
import sys


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="hello_heartbeat")
    return parser.parse_args(argv)


def format_greeting(name: str, loud: bool) -> str:
    return ""


def main() -> int:
    parse_args()
    print("Hello, world!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
