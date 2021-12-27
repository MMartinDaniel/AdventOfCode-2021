import math
file = open("day10_input.txt", "r")

bracket_list = []

for index,line in enumerate(file.readlines()): 
    bracket_list.append([i for i in line.rstrip()])

total = []

total_p1 = 0
open_brackets = ['(','[','{','<']
closed_brackets = [')',']','}','>']

bracket_values = {
    ')': [3,1],
    ']': [57,2],
    '}': [1197,3],
    '>': [25137,4]
}

def calculate_p2(stack):
    total = 0
    for bracket in stack:
        total = (total * 5) + bracket_values[bracket][1]
    return total

for bracket_set in bracket_list:
    open_stack = []
    close_stack = []
    corrupt = False
    
    for index,bracket in enumerate(bracket_set):
        if bracket in open_brackets:
            open_stack.append(bracket)
            close_stack.insert(0,closed_brackets[open_brackets.index(bracket)])
        else:
            next_bracket = close_stack[0]
            if bracket == next_bracket: close_stack.pop(0)
            else:
                total_p1 += bracket_values[bracket][0]
                corrupt = True
                break
   
    if not corrupt: total.append(calculate_p2(close_stack))     

total.sort()

print('Silver Star Solution:', total_p1)
print('Gold   Star Solution:', total[math.floor(len(total)/2)])