file = open("inputs/01.txt", 'r')
lines = file.readlines()

sum = 0

for line in lines:
    firstNum = -1
    lastNum = -1
    for c in line:
        if c.isnumeric():
            if firstNum == -1:
                firstNum = c
            else:
                lastNum = c
    num = firstNum + (lastNum if lastNum != -1 else firstNum)
    sum += int(num)

file.close()
print(sum)