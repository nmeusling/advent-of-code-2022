def get_input():
    with open('problems/4_camp_cleanup_input.txt') as f:
        lines = f.readlines()
    return lines

def parse_input(lines):
    parsed_lines = []
    for line in lines:
        ranges = line.split(',')
        first_range_values = ranges[0].split('-')
        second_range_values = ranges[1].split('-')
        parsed_lines.append(((int(first_range_values[0]), int(first_range_values[1])), (int(second_range_values[0]), int(second_range_values[1]))))
    return parsed_lines

def range_contains_other_range(first_range, second_range):
    if first_range[0] >= second_range[0] and first_range[1] <= second_range[1]:
        return True
    elif second_range[0] >= first_range[0] and second_range[1] <= first_range[1]:
        return True
    else:
        return False

def ranges_overlap(first_range, second_range):
    if second_range[0] >= first_range[0] and second_range[0] <= first_range[1]:
        return True
    if second_range[1] >= first_range[0] and second_range[1] <= first_range[1]:
        return True
    return False

def count_ranges_fully_contained(ranges):
    count = 0
    for range in ranges:
        first_range = range[0]
        second_range = range[1]
        if range_contains_other_range(first_range, second_range):
            count += 1
    return count

def count_ranges_with_overlap(ranges):
    count = 0
    for range in ranges:
        first_range = range[0]
        second_range = range[1]
        if ranges_overlap(first_range, second_range) or range_contains_other_range(first_range, second_range):
            count += 1
    return count

def test_parse_input():
    lines = ['2-4,6-8', '2-3,4-5', '5-7,7-9']
    assert parse_input(lines) == [((2,4), (6,8)), ((2,3), (4,5)), ((5,7), (7,9))]

if __name__ == '__main__':
    ranges = parse_input(get_input())
    print(f'Part 1: {count_ranges_fully_contained(ranges)}')
    print(f'Part 2: {count_ranges_with_overlap(ranges)}')