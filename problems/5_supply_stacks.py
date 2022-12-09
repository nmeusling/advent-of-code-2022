stacks = [['Z', 'N', 'D'], ['M', 'C'],['P']]

def get_input():
    with open('problems/5_supply_stacks_input.txt') as f:
        lines = f.readlines()
    return lines

def get_line_break(lines):
    line_break = 0
    for i, line in enumerate(lines):
        if line == '\n':
            line_break = i
    return line_break

def get_moves(lines, line_break):
    moves = []
    move_lines = lines[line_break+1:]
    for move in move_lines:
        move_tokens = move.split(' ')
        quantity = int(move_tokens[1])
        origin = int(move_tokens[3]) -1
        destination = int(move_tokens[5]) -1
        moves.append((quantity, origin, destination))
    return moves

def get_stack_configuration(lines, line_break, number_of_stacks = 9):
    stack_lines = lines[:line_break]
    stacks = [[] for _ in range(number_of_stacks)]
    for stack in stack_lines:
        for i, char in enumerate(stack):
            if char.isalpha():
                stack_number = int(i/4)
                stacks[stack_number].insert(0, char)    
    return stacks

def move_crate(stacks, quantity, origin, destination):
    for i in range(quantity):
        crate = stacks[origin].pop()
        stacks[destination].append(crate)
    return stacks

def move_crate_grouped(stacks, quantity, origin, destination):
    crates_to_move = stacks[origin][-quantity:]
    stacks[origin]=stacks[origin][:-quantity]
    stacks[destination] = stacks[destination] + crates_to_move
    return stacks

def calculate_final_arrangement(grouped_crates=False):
    input = get_input()
    line_break = get_line_break(input)
    stacks = get_stack_configuration(input, line_break, 9)
    moves = get_moves(input, line_break)
    for move in moves:
        if grouped_crates:
            move_crate_grouped(stacks, move[0], move[1], move[2])
        else:
            move_crate(stacks, move[0], move[1], move[2])
    return "".join([stack[-1] for stack in stacks])


def test_move_crates():
    stacks = [['Z', 'N', 'D'], ['M', 'C'],['P']]
    move_crate (stacks, 2, 1, 2)
    assert stacks == [['Z'], ['M', 'C', 'D', 'N'], ['P']]

def test_get_stack_configuration():
    stack_lines = ["    [D]    " , "[N] [C]    ", "[Z] [M] [P]",  "1   2   3 "]
    stacks = [['Z', 'N'], ['M', 'C', 'D'],['P']]
    assert get_stack_configuration(stack_lines, 3) == stacks

if __name__ == '__main__':
    print(f'Part 1: {calculate_final_arrangement()}')
    print(f'Part 2: {calculate_final_arrangement(grouped_crates=True)}')