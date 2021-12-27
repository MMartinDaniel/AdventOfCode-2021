file = open("day8_input.txt", "r")

class Clock:
    def __init__(self, input, output):
        self.input = []
        self.output = []

        for word in input: self.input.append(word)
        for word in output: self.output.append(word)
        
        self.state = {
            '2': [['1'],[]],
            '3': [['7'],[]],
            '4': [['4'],[]],
            '7': [['8'],[]],
            '5': [['2','3','5'],[]],
            '6': [['0','6','9'],[]],
        }

        self.cifers = {
            'a': False,
            'b': False,
            'c': False,
            'd': False,
            'e': False,
            'f': False,
            'g': False
        }
        
        self.solved = {
            '0': [],
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': [],
            '6': [],
            '7': [],
            '8': [],
            '9': [],
        }

    def calculate_input_p2(self):
        for input in self.input:
            length = str(len(input))
            if length in self.state:
                self.state[length][1].append(list(input))
                if len(self.state[length][0]) == 1:
                    self.solved[self.state[length][0][0]] = list(input)

        #determine A
        if self.solved['7'] and self.solved['1']:
            self.cifers['a'] = set(self.solved['7']).difference(self.solved['1']).pop()

        #Determine C, F
        abc = self.state['6'][1][0] + self.state['6'][1][1] + self.state['6'][1][2]
        
        if abc.count(self.solved['1'][0]) == 2:
            self.cifers['c'] = self.solved['1'][0]
            self.cifers['f'] = self.solved['1'][1]
        else:
            self.cifers['c'] = self.solved['1'][1]
            self.cifers['f'] = self.solved['1'][0]

        #determine 2
        for lis in self.state['5'][1]:
            if self.cifers['f'] not in lis:
                self.solved['2'] = lis

        #determine 6
        for lis in self.state['6'][1]:
            if self.cifers['c'] not in lis:
                self.solved['6'] = lis

        #determine 5
        for lis in self.state['5'][1]:
            if self.cifers['c'] not in lis:
                self.solved['5'] = lis
            if self.cifers['c'] in lis and lis != self.solved['2']:
                self.solved['3'] = lis

        #determine e
        self.cifers['e'] = set(self.solved['6']).difference(set(self.solved['5'])).pop()

        #determine 0
        for lis in self.state['6'][1]:
            if self.cifers['e'] in lis and self.solved['6'] != lis:
                self.solved['0'] = lis
            else: 
                 if self.solved['6'] != lis:
                     self.solved['9'] = lis
     
    def get_output(self):
        number = ''
        for output in self.output:
            output_lis = list(output)
            for i in range(10):
                if set(self.solved[str(i)]) == set(output_lis):
                    number += str(i)
        
        return int(number)
    
input_output = []
total_count = 0

for index, line in enumerate(file):
    stripped_line = line.strip()

    input_output = stripped_line.split(' | ')
    input = input_output[0].split(' ')
    output = input_output[1].split(' ')
    clock = Clock(input,output)
    clock.calculate_input_p2()

    total_count += clock.get_output()

print('Gold Start Solution: ', total_count)