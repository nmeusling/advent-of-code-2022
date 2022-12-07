import string

def get_input():
    with open('problems/3_rucksack_reorganization_input.txt') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def get_repeat_item(rucksack_contents):
    second_compartment_index = int(len(rucksack_contents) / 2)
    first_compartment = set(rucksack_contents[0:second_compartment_index])
    second_compartment = set(rucksack_contents[second_compartment_index:])
    return next(iter(first_compartment.intersection(second_compartment)))

def get_badge_item(rucksack_group):
    return next(iter(set(rucksack_group[0]) & set(rucksack_group[1]) & set(rucksack_group[2])))

def get_letter_priorities():
    letter_priority = dict()
    for index, letter in enumerate(string.ascii_letters):
        letter_priority[letter] = index + 1
    return letter_priority

def sum_priorities(rucksacks):
    total_priority = 0
    letter_priorities = get_letter_priorities()
    for rucksack in rucksacks:
        repeat_item = get_repeat_item(rucksack)
        total_priority += letter_priorities[repeat_item]
    return total_priority

def sum_group_priorities(rucksacks):
    total_priority = 0
    letter_priorities = get_letter_priorities()
    group_size = 3
    number_of_groups = int(len(rucksacks)/group_size)
    for i in range(number_of_groups):
        group = rucksacks[i*group_size:i*group_size+3]
        badge_item = get_badge_item(group)
        total_priority += letter_priorities[badge_item]
    return total_priority

def test_get_letter_priority():
    letter_priorities = get_letter_priorities()
    assert letter_priorities['a'] == 1
    assert letter_priorities['z'] == 26
    assert letter_priorities['A'] == 27
    assert letter_priorities['Z'] == 52

def test_get_repeat_item():
    assert get_repeat_item('vJrwpWtwJgWrhcsFMMfFFhFp') == 'p'
    assert get_repeat_item('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL') == 'L'
    assert get_repeat_item('PmmdzqPrVvPwwTWBwg') == 'P'
    assert get_repeat_item('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn') == 'v'
    assert get_repeat_item('ttgJtRGJQctTZtZT') == 't'
    assert get_repeat_item('CrZsJsPPZsGzwwsLwLmpwMDw') == 's'

def test_get_badge_item():
    group_one = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg']
    group_two = ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
    assert get_badge_item(group_one) == 'r'
    assert get_badge_item(group_two) == 'Z'

if __name__ == '__main__':
    print(f'Part 1: {sum_priorities(get_input())}')
    print(f'Part 2: {sum_group_priorities(get_input())}')
    pass