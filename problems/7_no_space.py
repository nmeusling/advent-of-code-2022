CHANGE_DIR = '$ cd'
UP_DIR_LEVEL = '..'
LIST_COMMAND = '$ ls'

def get_input():
    with open('problems/7_no_space_input.txt') as f:
        lines = f.readlines()
    return lines

def get_path_sizes(lines):
    current_directory = []
    sizes = {}
    for line in lines:
        if line.startswith(CHANGE_DIR):
            tokens = line.split()
            next_directory = tokens[2]
            if next_directory == UP_DIR_LEVEL:
                current_directory.pop()
            else:
                current_directory.append(next_directory)
        elif line.startswith(LIST_COMMAND):
            continue
        else: 
            tokens = line.split()
            if tokens[0].isnumeric():
                file_size = int(tokens[0])
                for i in range(len(current_directory)):
                    path = "/" + "/".join(current_directory[1:i+1])
                    if sizes.get(path):
                        sizes[path] += file_size
                    else:
                        sizes[path] = file_size
    return sizes

def sum_sizes_under_threshold(sizes):
    total = 0
    threshold = 100000
    for size in sizes.values():
        if size < threshold:
            total += size
    return total

def find_smallest_directory_that_contains_needed_space(sizes):
    total_file_system = 70000000
    update_size = 30000000
    # space under root directory
    used_space = sizes['/']
    unused_space = total_file_system - used_space
    additional_space = update_size - unused_space

    possible_files_to_delete = []
    for size in sizes.values():
        if size > additional_space:
            possible_files_to_delete.append(size)
    return min(possible_files_to_delete)

        
if __name__ == '__main__':
    sizes = get_path_sizes(get_input())
    print(f'Part 1: {sum_sizes_under_threshold(sizes)}')
    print(f'Part 2: {find_smallest_directory_that_contains_needed_space(sizes)}')
