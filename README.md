# covid_announcer

A small, loud piece of software from the first week of India's national lockdown.

In late March 2020, everyone in the house was refreshing the same COVID numbers on their phones, several times an hour, and reading them out to each other in the kitchen. This script replaced that. It ran on a laptop in the corner, checked India's numbers every two minutes between 9am and 10pm, and spoke any change out loud through the speakers. If the numbers did not move for three hours, it said so.

I wrote it over two days, 23 to 25 March 2020. It is about 70 lines of Python and it did exactly what it needed to do.

## What it did

- Every two minutes, between 9am and 10pm, it fetched India's totals from `api.covid19india.org`.
- Whenever active cases, deaths, or recoveries changed, it played a short chime (`open.mp3`) and then a spoken announcement through `ffplay`.
- Decreases and recoveries got "A good news". Increases and deaths got "A bad news". The exact phrasing is in `covid19.py` and it is very much of its moment.
- If nothing changed for three hours, it announced that too, so silence meant the script was still alive.
- Outside those hours it went quiet and slept, so it would not wake anyone up at night.
- The whole thing sat in a `while True` loop with exception handling, because the API and the network were both unreliable and the laptop needed to keep going unattended.

At startup it also read out the current totals, so the first thing you heard in the morning was where things stood.

## How it worked

The pieces were deliberately simple:

- `urllib` for the HTTP call, plus `COVID19Py` (imported at the time; the actual fetch went straight to the India API).
- `gTTS` for text to speech, writing each message to `corona.mp3`.
- `ffplay` from FFmpeg to play the chime and then the generated clip.
- `datetime` and `time.sleep` for the schedule and the two minute cadence.

To hear it as it ran:

```bash
python -m venv .venv
.venv/bin/pip install gTTS COVID19Py
.venv/bin/python covid19.py
```

That will not produce useful output today. The data source is gone.

## Why it no longer runs

`api.covid19india.org` shut down in 2021. It was a volunteer effort that many people relied on during the pandemic, and the endpoint this script calls no longer returns data. Even with FFmpeg, gTTS, and a virtualenv, the first fetch fails.

This repository is archived as a time capsule. I am leaving it exactly as it was: the original commits, the typo-tolerant phrasing, the chime, the 3am-proof retry loops. It is a record of a specific week more than a working tool.

If you want to run something like it today, you would need a current data source and a small rewrite of `fetch_data()`. The scheduling, speech, and chime logic would still work.

## Files

- `covid19.py`: the script.
- `open.mp3`: the chime played before each announcement.

## A note

It was built in a hurry, in a frightening week, for one household. It is not elegant and it was never meant to be published as anything polished. It just needed to tell us the news out loud.
