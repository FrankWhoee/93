import sqlite3
from selenium import webdriver
import pickle
import os
from selenium.webdriver.chrome.options import Options

# Data from https://www.kaggle.com/visualize25/valorant-pro-matches-full-data

# Load sqlite database and create matches.pickle if not created yet so we don't have to access the database every time.
from selenium.webdriver.common.by import By

matches = {}

if (not os.path.exists("matches.pickle")):
    print("Extracting match IDs from valorant.sqlite...")
    con = sqlite3.connect("valorant.sqlite")
    cur = con.cursor()
    for row in cur.execute("SELECT GameID, MatchID FROM Games"):
        print(row)
        if row[1] in matches:
            matches[row[1]].append(row[0])
        else:
            matches[row[1]] = [row[0]]
    with open('matches.pickle', 'wb') as fp:
        pickle.dump(matches, fp)
    print("Matches saved to matches.pickle.")
else:
    print("Reading from matches.pickle...")
    with open('matches.pickle', 'rb') as fp:
        matches = pickle.load(fp)
print("Complete.")
# print(matches)

# Set up selenium

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

data = []
limit = 100000
print("Scraping vlr.gg for score timeline... limit={}".format(limit))
# Scrape vlr.gg for score timeline.
limit = max(limit,len(matches))
progress = 0
report_interval = 25
for match in matches.keys():
    if(int(progress/limit * 100) % report_interval == 0):
        print("Progress: " + str(progress/limit * 100))
    driver.get('https://vlr.gg/{}'.format(match))
    h1 = driver.find_element(By.CLASS_NAME, "vm-stats-container")
    c1 = h1.find_elements(By.CLASS_NAME, "vm-stats-game")
    for game in c1:
        if(game.get_attribute("data-game-id") == "all"):
            continue
        g = []
        cols = game.find_elements(By.CLASS_NAME, "vlr-rounds-row-col")
        for i in range(1,len(cols)):
            res = cols[i].find_elements(By.CLASS_NAME, "rnd-sq")
            if len(res) == 0:
                continue
            ctwin = len(res[0].find_elements(By.CSS_SELECTOR, "*")) == 1
            twin = len(res[1].find_elements(By.CSS_SELECTOR, "*")) == 1
            if not (ctwin or twin):
                break
            else:
                g.append(1 if ctwin else -1)
        data.append(g)
    if progress >= limit:
        break
    progress+= 1
print("Complete. Saving to data.pickle.")
with open('data.pickle', 'wb') as fp:
    pickle.dump(data, fp)
print("Complete.")