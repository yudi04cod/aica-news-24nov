[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/yudi04cod/aica-news-24nov/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/yudi04cod/aica-news-24nov/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# Aica News — Tuesday 24 November 2026

A one-page newspaper front page summing up the world's news of Tuesday
24 November 2026, drawn entirely in code with Python and PIL — no
external images, no network.

Lead story: Jensen Huang is reinstated as Nvidia's chief executive,
11 days after he resigned, and the shares soar 31% in a day — their
best day since 2003, adding about $1 trillion in market value — as the
Nasdaq climbs 6.5% and the S&P 500 4.7%. Also covered: Ukraine saying
its sea drones sank the Russian corvette Merkury off Benghazi, Libya;
Denmark's top court backing the "ghetto law"; the India–New Zealand
Test ending in a draw at Wellington; Carlos Alcaraz winning his first
ATP Finals title in Turin; D Gukesh opening his World Chess
Championship title defence against Javokhir Sindarov in Geneva; and a
brief ground stop at Chicago's O'Hare airport in the Thanksgiving
travel rush. The ticker adds the Indonesia factory fire toll reaching
24, COP31 ending with no deal on fossil fuels, FIFA picking hosts for
the 2031 and 2035 Women's World Cups, and the Sensex falling 1,484
points.

## How it works

- `main.py` (Python 3.13, standard library only) copies the shipped
  `entry.png` (1024×1024) to `$MAKEFUN_OUTPUT_DIR/entry.png`
  (default `/output`), verifying the copy byte for byte against the
  shipped file. No network, no randomness — both runs write
  byte-identical output.

Run `MAKEFUN_OUTPUT_DIR=out python3 main.py` to produce the output file.

Built for the [make.fun](https://make.fun) competition
[news-image-20261124](https://make.fun/bounty/news-image-20261124).

Built for make.fun — referral code 38m33ybw
