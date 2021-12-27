file = open("day7_input.txt", "r")

class CrabAligner():

    positions = []
    total_fuel_by_position = []
    max_length = 0

    def __init__(self, fishes):
        for fish in fishes: self.positions.append(int(fish))
        self.positions = list(sorted(self.positions))
        self.max_length = max(self.positions)
    
    def calculate_distance_p1(self):
        for current_pos in range(self.max_length):
            total_distance = 0
            for new_pos in self.positions:
                if current_pos != new_pos:
                    total_distance += abs(current_pos - new_pos)
        
            self.total_fuel_by_position.append([current_pos, total_distance])


    def calculate_distance_p2(self):
        for current_pos in range(self.max_length):
            total_distance = 0
            for new_pos in self.positions:
                if current_pos != new_pos:
                    total_distance += self.calculate_fuel_consumption(current_pos - new_pos)

            self.total_fuel_by_position.append([current_pos, total_distance])

    def calculate_fuel_consumption(self, distance):
        total_cost = 0
        fuel_cost = 1
        for i in range(abs(distance)):
            total_cost += i + fuel_cost

        return total_cost

                    
    def calcuate_fuel(self):
        min = [False, 99999999999999]
        for current_pos in self.total_fuel_by_position:
            if current_pos[1] < min[1]: min = current_pos

        return min

fishes = []
for line in file: fishes = line.split(',')

crab = CrabAligner(list(map(int, fishes)))

#crab.calculate_distance_p1()
#print('Silver Star Solution:', crab.calcuate_fuel())

crab.calculate_distance_p2()
print('Gold   Star Solution:', crab.calcuate_fuel())

