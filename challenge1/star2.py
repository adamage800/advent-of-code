import re

def replaceNumberStringToNumber(inputString):
    stringsToReplace = ["five", "one", "eight", "three", "two", "one", "four", "six", "seven", "nine"]

    updatedString = inputString

    for i in range(len(stringsToReplace)):
        numberString = stringsToReplace[i]
        updatedString = re.sub(numberString, str(i + 1), updatedString)
    
    return updatedString

print(replaceNumberStringToNumber("xtwone3four"))

# Open the file
with open('input.txt', 'r') as file:
    acc = 0
    for line in file:
        pattern = r"\d+"
        line = replaceNumberStringToNumber(line)
        numbersArray = re.findall(pattern, line)
        firstDigit = numbersArray[0][0]
        lastDigit = numbersArray[-1][-1]
        number = int(firstDigit + lastDigit)
        acc += int(number)
    
    print("Solution %d" % acc)