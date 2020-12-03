from itertools import combinations

with open('input/input.txt','r', newline='\n') as file:
    lines = file.readlines()
    numbers = [int(line) for line in lines]
    # find all combos
    for combo in combinations(numbers, 2):
        number = combo[0]
        other_number = combo[1]
        if(number + other_number == 2020):
            print(f'{number} and {other_number} add to be 2020, multiplied they are {number * other_number}')

    for combo in combinations(numbers, 3):
        number = combo[0]
        other_number = combo[1]
        other_other_number = combo[2]
        if(number + other_number + other_other_number == 2020):
            print(f'{number}, {other_number} and {other_other_number} add to be 2020, multiplied they are {number * other_number * other_other_number}')



