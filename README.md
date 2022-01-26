![](logo.svg)
# 93
This is a project seeking to figure out whether the 9-3 curse is real. I am using Joshua Broas' [dataset](https://www.kaggle.com/visualize25/valorant-pro-matches-full-data) to extract match IDs, then using selenium (maybe not the best idea) to scrape vlr.gg for the score timeline.

## Installation
1. `git clone https://github.com/FrankWhoee/93.git`
2. `cd 93`
3. `python3 venv venv` (requires you to have [venv](https://pypi.org/project/virtualenv/) installed)
4. `source venv/bin/activate`
5. `pip install requirements.txt`

## Running
To begin collecting data:
1. `python3 main.py`
2. Data will be saved every 50 matches to data.pickle.

To begin analysis:
1. `python3 analysis.py`

## Preliminary results
As of 6:25pm PDT I am still running the scraping program but so far these are the results:
Sample size: 840
- Chance of losing from 7-5: 0.2175925925925926
- Chance of losing from 8-4: 0.143646408839779
- Chance of losing from 9-3: 0.07453416149068323
- Chance of losing from 10-2: 0.03636363636363636
- Chance of losing from 11-1: 0.0
- Chance of losing from 12-0: 0.0

## Credits
Thanks to Joshua Broas for the [dataset](https://www.kaggle.com/visualize25/valorant-pro-matches-full-data).
