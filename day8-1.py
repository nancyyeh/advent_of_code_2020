input_file = open("day8", "r")
content = input_file.read()
list_content = content.split("\n")

instruction_dictionary = {}

for i, instruction in enumerate(list_content):
    instruction_dictionary[i] = {
        'line': i, 'command': instruction[0:3], 'signal': instruction[4], 'number': int(instruction[5:])}

visited_line = set()


def acc_at_repeat():
    curr_line = 0
    acc = 0
    while curr_line < len(instruction_dictionary)-1:
        # print(i+1, instruction_dictionary[curr_line])
        curr_line_info = instruction_dictionary[curr_line]

        if curr_line_info['line'] in visited_line:
            return acc
        else:
            visited_line.add(curr_line_info['line'])

        if curr_line_info['command'] == 'nop':
            curr_line += 1
        elif curr_line_info['command'] == 'acc':
            if curr_line_info['signal'] == '-':
                acc -= curr_line_info['number']
            if curr_line_info['signal'] == '+':
                acc += curr_line_info['number']
            curr_line += 1
        elif curr_line_info['command'] == 'jmp':
            if curr_line_info['signal'] == '-':
                curr_line -= curr_line_info['number']
            if curr_line_info['signal'] == '+':
                curr_line += curr_line_info['number']
        # print('next:', curr_line, 'acc:', acc, visited_line)


print(acc_at_repeat())
