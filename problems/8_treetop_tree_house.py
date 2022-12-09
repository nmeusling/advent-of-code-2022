def get_input():
    with open('problems/8_treetop_tree_house_input.txt') as f:
        lines = f.readlines()
    return lines

def get_forest(lines):
    forest = []
    for i, row in enumerate(lines):
        forest.append([])
        for tree in row.strip():
            height = int(tree)
            forest[i].append(height)
    return forest

def count_visible_trees(forest):
    count = 0
    for i, row in enumerate(forest):
        for j, column in enumerate(row):
            if tree_is_visible(i, j, forest):
                count += 1
    return count


def tree_is_visible(row, column, forest):
    if row == 0 or column == 0:
        return True
    # if it's in last row of forest
    if row == len(forest) - 1:
        return True
    # if it's in last column of forest
    if column == len(forest[0]) - 1:
        return True

    tree_height = forest[row][column]
    # check from left
    is_visible = True
    for i in range(column):
        if forest[row][i] >= tree_height:
            is_visible = False
    if is_visible:
        return True

    # check from right
    is_visible = True
    for i in range(column + 1, len(forest[0])):
            if forest[row][i] >= tree_height:
                is_visible = False
    if is_visible:
        return True

    # check from up
    is_visible = True
    for i in range(row):
            if forest[i][column] >= tree_height:
                is_visible = False
    if is_visible:
        return True
    
    # check from down
    is_visible = True
    for i in range(row+1, len(forest)):
            if forest[i][column] >= tree_height:
                is_visible = False
    if is_visible:
        return True

    # if it is not an edge, and not visible from any direction
    return False

def get_scenic_score(row, column, forest):
    tree_height = forest[row][column]

    # looking left
    trees_visible_to_left = 0
    for i in range(column -1, -1, -1):
        trees_visible_to_left += 1
        if forest[row][i]>= tree_height:
            break

    trees_visible_to_right = 0
    for i in range(column + 1, len(forest[0])):
        trees_visible_to_right += 1
        if forest[row][i]>= tree_height:
            break

    trees_visible_up = 0
    for i in range(row-1, -1, -1):
        trees_visible_up += 1
        if forest[i][column]>= tree_height:
            break
    
    trees_visible_down = 0
    for i in range(row+1, len(forest)):
        trees_visible_down += 1
        if forest[i][column]>= tree_height:
            break

    return trees_visible_to_left * trees_visible_to_right * trees_visible_up * trees_visible_down
    
def get_max_scenic_score(forest):
    # don´t need to calculate for edges since it has 0 trees in one direction
    max_scenic_score = 0
    for i in range(1, len(forest) -1):
        for j in range(1, len(forest[0])-1):
            scenic_score = get_scenic_score(i, j, forest)
            max_scenic_score = max(max_scenic_score, scenic_score)
    return max_scenic_score

def test_get_forest():
    lines = ["30373", "25512", "65332", "33549", "35390"]
    expected_forest = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]
    assert get_forest(lines) == expected_forest

def test_tree_is_visible_for_edges():
    forest = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]
    # Check edges are visible
    assert tree_is_visible(0,0,forest) == True
    assert tree_is_visible(4,4,forest) == True
    assert tree_is_visible(4,2,forest) == True
    assert tree_is_visible(2,4,forest) == True
    assert tree_is_visible(2,0,forest) == True
    assert tree_is_visible(0,3,forest) == True

def test_tree_is_visible_interior():
    forest = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]
    assert tree_is_visible(1,1,forest) == True
    assert tree_is_visible(1,2,forest) == True
    assert tree_is_visible(1,3,forest) == False
    assert tree_is_visible(2,1,forest) == True
    assert tree_is_visible(2,2,forest) == False
    assert tree_is_visible(2,3,forest) == True
    assert tree_is_visible(4,1,forest) == True

def test_count_visible_trees():
    forest = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]
    assert count_visible_trees(forest) == 21

def test_get_scenic_score():
    forest = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]
    assert get_scenic_score(0,0,forest) == 0
    assert get_scenic_score(1,2,forest) == 4
    assert get_scenic_score(3,2,forest) == 8

if __name__ == '__main__':
    forest = get_forest(get_input())
    print(f'Part 1: {count_visible_trees(forest)}')
    print(f'Part 2: {get_max_scenic_score(forest)}')