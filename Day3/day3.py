file = open("day3_input.txt", "r")

max_line_length = 12
input = [line.rstrip() for line in open("day3_input.txt", "r")]


def get_count_per_bit(input_list, char_index):
    bit_count = [0,0]
    for line in input_list: bit_count[int(line[char_index])] += 1
    return bit_count

def p1():
    gamma_rate = ''
    epsilon_rate = ''
    char_index = 0

    while char_index < max_line_length:

        bit_count = get_count_per_bit(input, char_index)
        char_index += 1
        
        if bit_count[0] > bit_count[1]: gamma_rate = f'{gamma_rate}0'
        else: gamma_rate = f'{gamma_rate}1'

    for char in gamma_rate:
        if char == '0': epsilon_rate = f'{epsilon_rate}1'
        if char == '1': epsilon_rate = f'{epsilon_rate}0'
    
    result = int(gamma_rate,2) * int(epsilon_rate,2)
    return result


def filter_by(input_list, char_index_bit_count,char_index, sign):
    
    if char_index_bit_count[0] > char_index_bit_count[1]: filter_value = '0'
    else: filter_value = '1'
    
    if sign == '<': 
        if filter_value == '1': filter_value = '0'
        else: filter_value = '1'

    return list(filter(lambda x: (x[char_index] == filter_value), input_list))

def p2(sign = ''):
    bit_count_list = []
    input_list = input
    char_index = 0
    
    while char_index < max_line_length:
        char_index_bit_count = get_count_per_bit(input_list, char_index)
        filtered_list = filter_by(input_list, char_index_bit_count,char_index,sign)  
        bit_count_list.append(char_index_bit_count)
        input_list = filtered_list
        char_index += 1
        if len(input_list) == 1: return int(input_list[0],2)

    
print('Silver Star Solution:', p1())
print('Gold   Star Solution:', p2() * p2('<'))

