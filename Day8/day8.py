file = open("day8_input.txt", "r")

class Clock:

    def __init__(self, input, output):
        self.input = []
        self.output = []

        for word in input: self.input.append(word)
        for word in output: self.output.append(word)
        self.known_inputs = {
            '1': [2,['c','f']],
            '4': [4,['b','c','d','f']],
            '7': [3,['a','c','f']],
            '8': [7,['a','b','c','d','e','f','g']],
        }
        self.guessed = {
            '1': [[],0],
            '4': [[],0],
            '7': [[],0],
            '8': [[],0]
        }

        self.state = {
            '2': ['1',[]],
            '4': ['4',[]],
            '3': ['7',[]],
            '7': ['8',[]]
        }
        self.total = 0


    def calculate_input_p1(self):
        for input in self.input:
            length = len(input)
            if str(length) in self.state:
                self.state[str(length)][1].append(list(input))

        self.calculate_solution_p1()
    
    def calculate_solution_p1(self):
        for length_key in self.state:
            if len(self.state[length_key][1]) == 1:
                self.guessed[self.state[length_key][0]][0] = (self.state[length_key][1][0])

        for output in self.output:
            length_key = len(output)
            if str(length_key) in self.state:
                match_length = self.state[str(length_key)][0]
                if all(item in list(output) for item in self.guessed[match_length][0]):
                    self.guessed[self.state[str(length_key)][0]][1] += 1 

    def get_total(self):
        self.total = 0
        for amount in self.guessed:
            self.total += self.guessed[amount][1]

        return self.total

input_output = []
total_count = 0

for index, line in enumerate(file):
    stripped_line = line.strip()

    input_output = stripped_line.split(' | ')
    input = input_output[0].split(' ')
    output = input_output[1].split(' ')
    
    clock = Clock(input,output)
    clock.calculate_input_p1()
    total_count += clock.get_total()

print('Silver Start Solution: ', total_count)
