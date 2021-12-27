class Mapper():
    file = open("day5_input.txt", "r")
    coordinates = []

    def __init__(self, columns):
        self.num_columns = columns
        self.map = [[ 0 for x in range(0, columns)] for y in range(0, columns)]
        for line in self.file:
            x12_y12 = line.rstrip().split(' -> ')
            pair = []
            for i in range(2):
                num = x12_y12[i].split(',')
                pair.append(int(num[0]))
                pair.append(int(num[1]))
            self.coordinates.append(pair)

       
    def calculate_line(self, with_cross=False):
        
        for coordinate_pairs in self.coordinates:
            #x2 == y2
            if coordinate_pairs[1] == coordinate_pairs[3]:
                #x1 > y1
                if coordinate_pairs[0] < coordinate_pairs[2]:
                    self.draw_in_map(coordinate_pairs[2] - coordinate_pairs[0], 'row', [coordinate_pairs[1], coordinate_pairs[0]])
                if coordinate_pairs[0] > coordinate_pairs[2]: 
                    self.draw_in_map(coordinate_pairs[0] - coordinate_pairs[2], 'row', [coordinate_pairs[1], coordinate_pairs[2]])
            #x1 == y1
            elif coordinate_pairs[0] == coordinate_pairs[2]: 
            #x2 > y2
                if coordinate_pairs[1] < coordinate_pairs[3]:
                    self.draw_in_map(coordinate_pairs[3] - coordinate_pairs[1], 'column', [coordinate_pairs[0], coordinate_pairs[1]])
                if coordinate_pairs[3] < coordinate_pairs[1]: 
                    self.draw_in_map(coordinate_pairs[1] - coordinate_pairs[3], 'column', [coordinate_pairs[0], coordinate_pairs[3]])
            
            elif with_cross: self.calculate_cross(coordinate_pairs)
        
    def calculate_cross(self, coordinate_pairs):

        counter = 0
        new_coord = [coordinate_pairs[0], coordinate_pairs[1]]

        while new_coord[0] != coordinate_pairs[2] and new_coord[1] != coordinate_pairs[3]:

            if coordinate_pairs[0] > coordinate_pairs[2] and coordinate_pairs[1] < coordinate_pairs[3]:
                # x less, y plus
                self.map[coordinate_pairs[0]-counter][coordinate_pairs[1]+counter] += 1
                new_coord[0] = coordinate_pairs[0] - counter
                new_coord[1] = coordinate_pairs[1] + counter

            if coordinate_pairs[0] > coordinate_pairs[2] and coordinate_pairs[1] > coordinate_pairs[3]:
                #x less, y less
                self.map[coordinate_pairs[0]-counter][coordinate_pairs[1]-counter] += 1
                new_coord[0] = coordinate_pairs[0] - counter
                new_coord[1] = coordinate_pairs[1] - counter

            if coordinate_pairs[0] < coordinate_pairs[2] and coordinate_pairs[1] < coordinate_pairs[3]:
                # x plus, plus
                self.map[coordinate_pairs[0]+counter][coordinate_pairs[1]+counter] += 1
                new_coord[0] = coordinate_pairs[0] + counter
                new_coord[1] = coordinate_pairs[1] + counter

            if coordinate_pairs[0] < coordinate_pairs[2] and coordinate_pairs[1] > coordinate_pairs[3]:
                #x plus, less
                self.map[coordinate_pairs[0]+counter][coordinate_pairs[1]-counter] += 1
                new_coord[0] = coordinate_pairs[0] + counter
                new_coord[1] = coordinate_pairs[1] - counter

            counter += 1

    def draw_in_map(self, distance, type, blocked_index):
        for i in range(distance+1):
            if type == 'column':
                self.map[blocked_index[0]][blocked_index[1]+i] += 1
            elif type == 'row': 
                self.map[blocked_index[1]+i][blocked_index[0]] += 1
   
    def calculate_olverlaps(self):
        total = 0
        for i in range(self.num_columns):
            for j in range(self.num_columns):
                if self.map[i][j] > 1: total += 1
        return total

map = Mapper(999)

#map.calculate_line()
#print('Silver Star Solution:', map.calculate_olverlaps())

map.calculate_line(with_cross=True)
print('Gold   Star Solution:', map.calculate_olverlaps())
