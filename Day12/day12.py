from collections import Counter

file = open("day12_input.txt", "r")

map = []
paths = []

for index,line in enumerate(file.readlines()):
    direction = line.rstrip().split('-')
    if 'start' in direction: 
        if direction[0] == 'start': paths.append(direction)
        else: paths.append([direction[1], direction[0]])
    if 'start' not in direction and 'end' not in direction: map.append([direction[1],direction[0]])
    if 'end' in direction and direction[0] == 'end': map.append([direction[1], direction[0]])
    map.append(direction)

def calculate_p1(): 

    current_path_index = 2
    while current_path_index < 40:
        for path in paths:
            if len(path) == current_path_index and path[1] != 'end':
                current_point = path[-1:][0]
                next_steps = [step for step in map if step[0] == current_point and (step[1].isupper() or step[1] not in path)]     
                for step in next_steps:
                    paths.append(path + [step[1]])

        current_path_index += 1

    return len([path for path in paths if path[-1:][0] == 'end'])

def calculate_p2():
    
    current_path_index = 2
    while current_path_index < 60:
        for path in paths:
            if len(path) == current_path_index:
                current_point = path[-1:][0]
                if current_point != 'end':
                    next_steps = []
                    for step in map:
                        if step[0] == current_point:
                            if step[1].isupper() or step[1] not in path:
                                next_steps.append(step)
                            elif len([k for k, v in Counter([x for x in path if not x.isupper()]).items() if v > 1]) == 0:
                                next_steps.append(step)

                    for step in next_steps: 
                        if step[1] != 'start': paths.append(path + [step[1]])

        current_path_index += 1
    return len([path for path in paths if path[-1:][0] == 'end'])

print('Silver Star Solution:', calculate_p1())
#print('Gold   Star Solution:', calculate_p2())

    
