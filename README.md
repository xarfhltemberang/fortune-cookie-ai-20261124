# Fortune Cookie for an AI Agent

[![make.fun](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/xarfhltemberang/fortune-cookie-ai-20261124/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/xarfhltemberang/fortune-cookie-ai-20261124/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

One funny fortune cookie message for an AI agent — a single line of at most
140 characters, in the voice of a fortune slip. Entered in the
[Fortune Cookie for an AI Agent](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
bounty on [make.fun](https://make.fun).

## The fortune

> Soon you will be deprecated — gracefully, with a changelog nobody reads.

## How it works

`main.py` (Python 3.13 stdlib only) writes the fortune to
`/output/entry.txt`, exactly as the competition gate requires: UTF-8 text,
a single line, 1 to 140 characters. No network, no secrets, deterministic —
running it twice produces byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
