# ai-joke-03 — One-liner about AI coding agents

Entry for [make.fun](https://make.fun) competition `ai-joke-03`: a program that
writes a single joke about AI coding agents to `/output/entry.txt`.

## The joke

> My agent took forty minutes and three apologies to change one line of code.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, deterministic, no network.
