import os
import pickle

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

for game in data:
    ctwins = 0
    twins = 0
    cursed = 0
    for r in game:
        if ctwins == 9 and twins == 3:
            cursed = 1
        elif ctwins == 3 and twins == 9:
            cursed = -1
        if r < 0:
            twins += 1
        elif r > 0:
            ctwins += 1
    if (ctwins < twins and cursed == 1) or (ctwins > twins and cursed == -1):
        success += 1
    total += 1
print(success)
print(total)
print(success/total)