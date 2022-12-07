def get_input():
    with open('problems/2_rock_paper_scissors_input.txt') as f:
        lines = f.readlines()
    return lines

def parse_input(lines):
    parsed_lines = []
    for line in lines:
        line = line.strip('\n')
        opponent, player = line.split()
        parsed_lines.append((opponent, player))
    return parsed_lines

def score_round(opponent, player):
    shape_score = {'X': 1, 'Y': 2, 'Z': 3}
    player_winning_moves = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]
    draw_moves = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
    if (opponent, player) in draw_moves:
        outcome_score = 3
    elif (opponent, player) in player_winning_moves:
        outcome_score = 6
    else:
        outcome_score = 0   
    return shape_score[player] + outcome_score 

def score_round_part_2(opponent, outcome):
    outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
    shape_score = {'A': 1, 'B': 2, 'C': 3}
    return outcome_score[outcome] + shape_score[get_shape_for_desired_outcome(opponent, outcome)]

def get_shape_for_desired_outcome(opponent, outcome):
    # X = player loses, Y = draw, Z = player wins
    player_move_to_win = {'A': 'B', 'B': 'C', 'C': 'A'}
    player_move_to_lose = {'B': 'A', 'C': 'B', 'A': 'C'}
    if outcome == 'Y':
        return opponent
    elif outcome == 'X':
        return player_move_to_lose[opponent]
    else:
        return player_move_to_win[opponent]

def score_tournament(moves, part_two=False):
    score = 0
    for move in moves:
        if part_two:
            score += score_round_part_2(move[0], move[1])
        else:
            score += score_round(move[0], move[1])
    return score

def calculate_total_score():
    input_lines = get_input()
    parsed_lines = parse_input(input_lines)
    return score_tournament(parsed_lines)

def calculate_total_score_part_2():
    input_lines = get_input()
    parsed_lines = parse_input(input_lines)
    return score_tournament(parsed_lines, part_two=True)
            
def test_score_round():
    assert(score_round('A', 'Y') == 8)
    assert(score_round('B', 'X') == 1)
    assert(score_round('C', 'Z') == 6)

def test_parse_input():
    lines = ['A Y\n', 'B X\n', 'C Z']
    assert(parse_input(lines) == [('A', 'Y'), ('B', 'X'), ('C', 'Z')])

if __name__ == '__main__':
    print(f'Part 1: {calculate_total_score()}')
    print(f'Part 2: {calculate_total_score_part_2()}')
