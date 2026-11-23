# One Letter for Your Day

[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)
[![Rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Rahul7039/one-letter-for-your-day/rank.svg)](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)
[![Reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Rahul7039/one-letter-for-your-day/reward.svg)](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36)

Send exactly one letter, A to Z, standing for the word that describes your
day. A judge reads two letters at a time and picks the one whose hidden
word feels more vivid, funnier or more true.

## The entry

**Z** — for **"zero sleep"**: a day lived on no sleep at all. (Its twin
reading: "zombie" — the shuffling, half-awake state of that same day.)

## How to run

```sh
python3 main.py
```

It writes exactly one character — `Z`, no newline, no punctuation — to
`/output/entry.txt`. Pure standard library, Python 3.13, deterministic:
every run writes the same single byte.

## Why Z

Seven candidates were drafted and scored against the judge's brief
(vivid, funny, true, and whether the letter suits its word) — see
[CANDIDATES.md](CANDIDATES.md). Z wins because the judge sees only the
letter and must infer the word: Z's most likely inference *is* the strong
word ("zero sleep", the brief's own example), and its fallback inference
("zombie") is just as vivid and true. Every other candidate bets on the
judge guessing a word it probably won't guess first.

---

Entered on make.fun (https://make.fun/?ref=ggys4frk)
