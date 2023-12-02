import re

# Open the file
with open('input.txt', 'r') as file:
    acc = 0
    for line in file:
        pattern = r"\d+"
        numbersArray = re.findall(pattern, line)
        firstDigit = numbersArray[0][0]
        lastDigit = numbersArray[-1][-1]
        number = int(firstDigit + lastDigit)
        acc += int(number)
    
    print("Solution %d" % acc)