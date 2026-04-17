import os
import subprocess
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
ENV = {**os.environ, "PYTHONPATH": str(SRC_DIR)}
CLI = [sys.executable, "-m", "hello_heartbeat"]


def test_default_greeting() -> None:
    result = subprocess.run(CLI, capture_output=True, text=True, env=ENV)
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, world!"


def test_named_greeting() -> None:
    result = subprocess.run([*CLI, "--name=Valaris"], capture_output=True, text=True, env=ENV)
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, Valaris!"


def test_loud_greeting() -> None:
    result = subprocess.run([*CLI, "--name=Valaris", "--loud"], capture_output=True, text=True, env=ENV)
    assert result.returncode == 0
    assert result.stdout.strip() == "HELLO, VALARIS!"


def test_help_mentions_flags() -> None:
    result = subprocess.run([*CLI, "--help"], capture_output=True, text=True, env=ENV)
    assert "--name" in result.stdout
    assert "--loud" in result.stdout
