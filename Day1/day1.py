file = open("day1_input.txt", "r")

numbers = []
for line in file: numbers.append(int(line))

def p1():
    count = 0
    prev = numbers[0]
    for number in numbers:
        if number > prev: count += 1
        prev = number
    return count

def p2():
    count = 0
    cursor = 0
    length = len(numbers)

    for index in range(length):
        if index < 2: continue
        if index < length - 1: 
            first_set = sum([numbers[cursor], numbers[cursor+1], numbers[cursor+2]])
            second_set = sum([numbers[cursor+1], numbers[cursor+2], numbers[cursor+3]])
            if second_set > first_set: count += 1
            cursor += 1
    return count
    
print('Silver Star Solution:', p1())
print('Gold   Star Solution:', p2())

