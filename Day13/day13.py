# This solution is First part with half baked code for solving Gold Start Solution

file = open("day13_input.txt", "r")

def get_a_paper(max_x, max_y): return [[ '.' for j in range(max_y) ]for i in range(max_x)]

paper = get_a_paper(2000,2000)
folds = []
max_column = 0
max_row = 0

for line in file:
    if line == '\n':
        pass
    elif line.startswith('fold'):
        fold = line.rstrip().replace('fold along ', '').split('=')
        folds.append([fold[0],int(fold[1])])
    else:

        point = list(map(int,list(line.rstrip().split(','))))
        if max_column < point[0]: max_column = point[0]
        if max_row < point[1]:    max_row = point[1]
        paper[point[1]][point[0]] = '#'

max_row += 1
max_column += 1

def fold_over_axys(paper, axis, cut_point, max_column, max_row):
    
    new_paper = get_a_paper(4000,4000)

    if axis == 'y':
        max_row_cut = max_row - cut_point - 1
        max_column_cut = max_column

    else:
        max_row_cut = max_row
        max_column_cut = max_column - cut_point - 1

    for row in range(max_row_cut):
         for column in range(max_column_cut):
            if axis == 'y':
                if paper[row + cut_point + 1][column] == '#': 
                    new_paper[cut_point - row - 1][column] = paper[row + cut_point + 1][column]
            else:
                if paper[row][column + cut_point + 1] == '#':
                    new_paper[row][cut_point - column  - 1] = paper[row][column + cut_point + 1]
   
            if paper[row][column] == '#': 
                new_paper[row][column] = paper[row][column]
           
            
    return  { 'paper': new_paper, 'max_row': max_row_cut, 'max_column': max_column_cut }

def count_hash(paper, max_row, max_column):
    total = 0
    for row in range(max_row):
        for column in range(max_column):
            if paper[row][column] == '#':
                total += 1
    return total

# only first fold
for index in range(1):
    fold = fold_over_axys(paper, folds[index][0], folds[index][1], max_column, max_row)
    paper = fold['paper']
    max_column = fold['max_column']
    max_row = fold['max_row']

print('Silver Start Solution:', count_hash(paper, max_row, max_column))

