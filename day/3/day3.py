from dataclasses import dataclass, field
from typing import List
from math import prod

@dataclass
class TreeLine:
    line_o_trees: List[bool]

@dataclass
class Treemap:
    tree_line: List[TreeLine]

@dataclass
class Slope:
    Right: int
    Down: int




def process_line(line: str) -> TreeLine:
    # You make a map (your puzzle input) of the open squares (.) and trees (#) you can see.
    is_tree = '#'
    line_o_trees = []
    for char in line:
        if char == is_tree:
            line_o_trees.append(True)
        elif char == '.':
            line_o_trees.append(False)
        else:
            pass
    return TreeLine(line_o_trees)

with open('input/input.txt','r', newline='\n') as file:
    lines = file.readlines()
    treemap = Treemap([])
    for line in lines:
        print(line)
        treemap.tree_line.append(process_line(line))

    # You start on the open square (.) in the top-left corner
    right_num = 0
    tree_hit_num = 0
    tree_mod = len(treemap.tree_line[0].line_o_trees)
    for tree_line in treemap.tree_line:
        right_num_w_mod = right_num % tree_mod
        print(tree_line, f'checking line on index {right_num_w_mod}')
        if tree_line.line_o_trees[right_num_w_mod]:
            # how many trees would you encounter?
            tree_hit_num += 1
            print('hit a tree on line')
        # The toboggan can only follow a few specific slopes
        # (you opted for a cheaper model that prefers rational numbers);
        # start by counting all the trees you would encounter for the slope right 3, down 1
        right_num += 3
    print(f'to get to the bottom you encounter {tree_hit_num} trees')

    # Determine the number of trees you would encounter if, for each of the following slopes
    slopes = [
        Slope(1,1),
        Slope(3, 1),
        Slope(5, 1),
        Slope(7, 1),
        Slope(1, 2)
    ]

    tree_hit_nums = []
    for slope in slopes:
        right_num = 0
        tree_hit_num = 0
        for ix, tree_line in enumerate(treemap.tree_line):
            if ix == 0 or ix % slope.Down == 0:
                right_num_w_mod = right_num % tree_mod
                # print(tree_line, f'checking line on index {right_num_w_mod}')
                if tree_line.line_o_trees[right_num_w_mod]:
                    # how many trees would you encounter?
                    tree_hit_num += 1
                # The toboggan can only follow a few specific slopes
                # (you opted for a cheaper model that prefers rational numbers);
                # start by counting all the trees you would encounter for the slope right 3, down 1
                right_num += slope.Right
        print(f'to get to the bottom you encounter {tree_hit_num} trees for Right {slope.Right} and Down {slope.Down} ')
        tree_hit_nums.append(tree_hit_num)
    print(f'The multiple of all the answers is {prod(tree_hit_nums)}')