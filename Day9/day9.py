file = open("day9_input.txt", "r")
matrix = []
lows = []

for index,line in enumerate(file.readlines()): 
    matrix.append([int(i) for i in line.rstrip()])
nxm = tuple([len(matrix),len(matrix[0])])   

def is_a_low(x,y):
    
    if x+1 < nxm[0]:
        if matrix[x][y] >= matrix[x+1][y]: return False
    if y-1 >= 0:
        if matrix[x][y] >= matrix[x][y-1]: return False
    
    if x-1 >= 0:
        if matrix[x][y] >= matrix[x-1][y]: return False
    if y+1 < nxm[1]:
        if matrix[x][y] >= matrix[x][y+1]: return False
    
    return True
  
def find_basin(x,y,index, mask, low_list):
    
    if x+1 < nxm[0]:
        if mask[x+1][y] != 9:
            if [x+1,y] not in low_list[index]: low_list[index].append([x+1,y])
    if y-1 >= 0:
        if mask[x][y-1] != 9:
            if [x,y-1] not in low_list[index]: low_list[index].append([x,y-1])
    
    if x-1 >= 0:
        if mask[x-1][y] != 9: 
            if [x-1,y] not in low_list[index]: low_list[index].append([x-1,y])
    if y+1 < nxm[1]:
        if mask[x][y+1] != 9: 
            if [x,y+1] not in low_list[index]: low_list[index].append([x,y+1])
    
    mask[x][y] = 9


def calculate_p1():
    for x in range(nxm[0]):
        for y in range(nxm[1]):
            if is_a_low(x,y): lows.append(matrix[x][y] + 1)
    return sum(lows) 


def calculate_p2():

    mask = [[0 for y in range(nxm[1])] for x in range(nxm[0])]

    low_list = []
    total = 1

    for i in range(nxm[0]):
        for j in range(nxm[1]):
            if matrix[i][j] == 9: mask[i][j] = 9
            elif is_a_low(i,j):
                low_list.append([[i,j]])
                mask[i][j] = 0

    for index,low in enumerate(low_list):
        for low_coord in low:
            find_basin(low_coord[0], low_coord[1], index, mask, low_list)


    largest_basins = []

    for low in low_list: largest_basins.append(len(low))

    largest_basins.sort()
    for low in largest_basins[-3:]: total = total * low  
    return total



print('Silver Star Solution:', calculate_p1())
print('Gold   Star Solution:', calculate_p2())



