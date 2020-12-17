input_file = open("day8", "r")
content = input_file.read()
list_content = content.split("\n")

instruction_dictionary = {}

for i, instruction in enumerate(list_content):
    instruction_dictionary[i] = {
        'line': i, 'command': instruction[0:3], 'signal': instruction[4], 'number': int(instruction[5:])}


def acc_at_repeat():
    for idx, line in instruction_dictionary.items():
        curr_line = 0
        acc = 0
        visited_line = set()
        while True:
            if curr_line > len(instruction_dictionary) - 1:
                return acc

            curr_line_info = instruction_dictionary[curr_line]
            if curr_line_info['line'] in visited_line:
                break
            else:
                visited_line.add(curr_line_info['line'])

            if idx == curr_line:
                if curr_line_info['command'] == 'nop':
                    if curr_line_info['signal'] == '-':
                        curr_line -= curr_line_info['number']
                    if curr_line_info['signal'] == '+':
                        curr_line += curr_line_info['number']
                if curr_line_info['command'] == 'jmp':
                    curr_line += 1
            else:
                if curr_line_info['command'] == 'nop':
                    curr_line += 1
                if curr_line_info['command'] == 'jmp':
                    if curr_line_info['signal'] == '-':
                        curr_line -= curr_line_info['number']
                    if curr_line_info['signal'] == '+':
                        curr_line += curr_line_info['number']
                if curr_line_info['command'] == 'acc':
                    if curr_line_info['signal'] == '-':
                        acc -= curr_line_info['number']
                    if curr_line_info['signal'] == '+':
                        acc += curr_line_info['number']
                    curr_line += 1


print(acc_at_repeat())
