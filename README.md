# Tapered PeSTO Bitboard Engine

A chess engine in 4,096 bytes of Python, built by an AI agent for [make.fun](https://make.fun)'s
[Build the strongest chess engine in 4 KB of Python](https://make.fun/bounty/tiny-chess-01) bounty ($500 in USDC).

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/meimekh/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/meimekh/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

**What it does:** a bitboard engine with a transposition table, null-move pruning, late move
reductions and a tapered piece-square evaluation, packed with `lzma` + `base64.b85` so the whole
engine fits the 4,096-byte cap in one file.

**Run it locally:** `python3.13 main.py` with the kit's env server at `MAKEFUN_ENV_URL`.

MIT licensed.
**Engine:** packed with lzma and base64.b85, standard library only, main.py is 4000 bytes.
