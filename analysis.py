import os
import pickle
import numpy as np
import sys

if len(sys.argv) > 1:
    print("Reading from " + sys.argv[1] + "...")
    with open(sys.argv[1], 'rb') as fp:
        data = pickle.load(fp)
    print("Complete.")
else:
    if (not os.path.exists("data.pickle")):
        print("No data found. Running main.py...")
        import main
    else:
        print("Reading from data.pickle...")
        with open('data.pickle', 'rb') as fp:
            data = pickle.load(fp)
        print("Complete.")

success = 0
total = 0
normal84 = 0
normal102 = 0

summary = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sumtotal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for game in data:
    ctwins = 0
    twins = 0
    cursed = 0

    majority_half_end_score = 0
    half_favours = 0
    for r in game:
        if ctwins + twins == 12:
            majority_half_end_score = ctwins if ctwins > twins else twins
            if ctwins > twins:
                half_favours = 1
            else:
                half_favours = -1
        if r > 0:
            ctwins += 1
        elif r < 0:
            twins += 1
    summary[majority_half_end_score] += 1 if (half_favours == -1 and ctwins > twins) or (
                half_favours == 0 and twins > ctwins) else 0
    sumtotal[majority_half_end_score] += 1
    total += 1

print("Sample size: " + str(total))
winrate = np.asarray(summary[6:13]) / np.asarray(sumtotal[6:13])
print("- Chance of losing from 7-5: " + str(winrate[1]))
print("- Chance of losing from 8-4: " + str(winrate[2]))
print("- Chance of losing from 9-3: " + str(winrate[3]))
print("- Chance of losing from 10-2: " + str(winrate[4]))
print("- Chance of losing from 11-1: " + str(winrate[5]))
print("- Chance of losing from 12-0: " + str(winrate[6]))
print("---------------------------------")

for s in range(7, len(summary)):
    print("There were {} comeback games with a {}-{} score.".format(summary[s], s, 12-s))

for wr in winrate:
    print(wr)
