file = open("day2_input.txt", "r")

move_sets = []

for line in file:
    move_and_amount = line.split()
    move_sets.append([move_and_amount[0], int(move_and_amount[1])])

def p1():

    pos = {
        'depth': 0,
        'horizontal': 0,
    }

    movements = {
        'forward': ('horizontal','+'),
        'down': ('depth', '+'),
        'up': ('depth', '-'),
    }
    
    for movement, amount in move_sets:
        
        variable = movements[movement][0]
        operator = movements[movement][1]

        if   operator == '+': pos[variable] +=  amount
        elif operator == '-': pos[variable] -=  amount


    return pos['depth'] * pos['horizontal']

def p2():

    pos = {
        'depth': 0,
        'horizontal': 0,
        'aim': 0
    }

    movements = {
        'forward': ('horizontal','+'),
        'down': ('aim', '+'),
        'up': ('aim', '-'),
    }

    for movement, amount in move_sets:

        variable = movements[movement][0]
        operator = movements[movement][1]

        if operator == '+':
            pos[variable] +=  amount
            if movement == 'forward': pos['depth'] += (pos['aim'] * amount)
            
        elif operator == '-': pos[variable] -=  amount
    
    return pos['depth'] * pos['horizontal']


print('Silver Star Solution:', p1())
print('Gold   Star Solution:', p2())

