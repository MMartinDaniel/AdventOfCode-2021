file = open("day11_input.txt", "r")

matrix = []
for index,line in enumerate(file.readlines()): 
    matrix.append([int(i) for i in line.rstrip()])

class FlashLightBoard:
    total_flashes = 0
    full_cleared_after_day = 0

    will_flash_stack = []
    already_flashed = []
    size = 10

    def __init__(self,matrix):
        self.matrix = matrix

    def pass_day(self): 
        for x in range(self.size):
            for y in range(self.size):
                self.matrix[x][y] += 1        

    def increase_adjacent(self, x,y):

        if x+1 < self.size : self.matrix[x+1][y] += 1
        if y+1 < self.size : self.matrix[x][y+1] += 1
        if y-1 >= 0:         self.matrix[x][y-1] += 1
        if x-1 >= 0:         self.matrix[x-1][y] += 1

        if x+1 < self.size and y+1 < self.size: self.matrix[x+1][y+1] += 1
        if y+1 < self.size and x-1 >= 0 :       self.matrix[x-1][y+1] += 1
        if y-1 >= 0 and x+1 < self.size :       self.matrix[x+1][y-1] += 1
        if x-1 >= 0 and y-1 >= 0:               self.matrix[x-1][y-1] += 1

    def will_flash(self):
        for x in range(self.size):
            for y in range(self.size):
                if [x,y] not in self.already_flashed:
                    if self.matrix[x][y] > 9 and [x,y] not in self.will_flash_stack:
                            self.will_flash_stack.append([x,y])
    
    def flash(self):
        while len(self.will_flash_stack) > 0:
            coor = self.will_flash_stack.pop(0)
            self.already_flashed.append(coor)
            self.increase_adjacent(coor[0], coor[1])
            self.will_flash()

    def clear(self):
        full_clear = True
        for x in range(self.size):
            for y in range(self.size):
                if self.matrix[x][y] > 9:
                    self.total_flashes += 1
                    self.matrix[x][y] = 0
                else:
                    full_clear = False
        self.already_flashed = []
        self.will_flash_stack = []

        return full_clear

    def pass_days(self, days: int):
        for day in range(days):
            self.pass_day()
            self.will_flash()
            self.flash()
            is_fully_cleared = self.clear()
            if is_fully_cleared:
                self.full_cleared_after_day = day + 1
                break  

flashLightBoard = FlashLightBoard(matrix)

#flashLightBoard.pass_days(100)
#print('Silver Star Solution:', flashLightBoard.total_flashes)

flashLightBoard.pass_days(999)
print('Gold   Star Solution:', flashLightBoard.full_cleared_after_day)
