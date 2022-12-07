def get_input():
    with open('problems/1_counting_calories_input.txt') as f:
        lines = f.readlines()
    return lines

def count_calories(lines):
    calories = []
    elf_number = 0
    for i in range(len(lines)):
        # If it's a blank line, it goes to the next elf
        if lines[i] == '\n':
            elf_number += 1
        else:
            if elf_number < len(calories):
                calories[elf_number] += int(lines[i])
            else:
                calories.append(int(lines[i]))
    return calories

def find_max_calories():
    lines = get_input()
    calory_counts = count_calories(lines)
    return max(calory_counts)

def sum_top_three_calories():
    lines = get_input()
    calory_counts = count_calories(lines)
    calory_counts.sort(reverse=True)
    return sum(calory_counts[0:3])

if __name__ == '__main__':
    print(f'Part 1: {find_max_calories()}')
    print(f'Part 2: {sum_top_three_calories()}')