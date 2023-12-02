import re

maxRed = 12
maxGreen = 13
maxBlue = 14

# Open the file
with open('input.txt', 'r') as file:
    acc = 0
    for line in file:
        gameId = int(re.findall(r"Game \d+", line)[0].split()[1])
        reds = list(map(lambda x: int(x.split()[0]), re.findall(r"\d+ red", line)))
        greens = list(map(lambda x: int(x.split()[0]), re.findall(r"\d+ green", line)))
        blues = list(map(lambda x: int(x.split()[0]), re.findall(r"\d+ blue", line)))

        isRedPossile = max(reds) <= maxRed
        isGreenPossile = max(greens) <= maxGreen
        isBluePossile = max(blues) <= maxBlue

        print(isRedPossile, isGreenPossile, isBluePossile)

        if isRedPossile and isGreenPossile and isBluePossile:
            print("gameId %d is possible" % gameId)
            acc += gameId
        else:
            print("gameId %d is not possible" % gameId)
    
    print("Solution %d" % acc)