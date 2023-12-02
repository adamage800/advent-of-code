import re

# Open the file
with open('input.txt', 'r') as file:
    acc = 0
    for line in file:
        gameId = int(re.findall(r"Game \d+", line)[0].split()[1])
        reds = list(map(lambda x: int(x.split()[0]), re.findall(r"\d+ red", line)))
        greens = list(map(lambda x: int(x.split()[0]), re.findall(r"\d+ green", line)))
        blues = list(map(lambda x: int(x.split()[0]), re.findall(r"\d+ blue", line)))

        maxRed = max(reds)
        maxGreen = max(greens)
        maxBlue = max(blues)

        print("gameId %d: %d %d %d" % (gameId, maxRed, maxGreen, maxBlue))

        acc += maxRed * maxGreen * maxBlue
    
    print("Solution %d" % acc)