file = open("inputs/01.txt", 'r')
lines = file.readlines()

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0

for line in lines:
    indexOfFirst = -1
    firstNum = -1
    indexOfLast = -1
    lastNum = -1

    for i,n in enumerate(numbers):
        index = line.find(n)
        if index != -1:
            if firstNum == -1 or index < indexOfFirst:
                firstNum = str(i+1)
                indexOfFirst = index
        index = line.rfind(n)
        if index != -1:
            if lastNum == -1 or index > indexOfLast:
                lastNum = str(i+1)
                indexOfLast = index

    for i,c in enumerate(line):
        if c.isnumeric():
            if firstNum == -1 or i < indexOfFirst:
                firstNum = c
                indexOfFirst = i
            if lastNum == -1 or i > indexOfLast:
                lastNum = c
                indexOfLast = i

    num = firstNum + lastNum
    sum += int(num)

file.close()
print(sum)