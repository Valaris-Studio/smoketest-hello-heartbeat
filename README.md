# hello-heartbeat

## What it does

`hello-heartbeat` is a tiny Python 3.11 CLI that prints a greeting to stdout. It accepts an optional `--name` to customize the recipient and an optional `--loud` flag to uppercase the output. The CLI is implemented with the standard library only.

## How to run

```
python -m hello_heartbeat
python -m hello_heartbeat --name=Valaris --loud
```

## How to test

```
pytest -q
```

## About

This repository is a Valaris Smoke Test #9 throwaway. Board: <https://valaris.local/boards/b2271e60-1af3-4a23-a887-2d64704729fd>.
