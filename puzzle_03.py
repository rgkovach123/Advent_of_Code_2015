"""
Advent of Code 2015: Day 3 - Perfectly Spherical Houses in a Vacuum

--- Part 1 ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, 
and then an elf at the North Pole calls him via radio and tells him where 
to move next. Moves are always exactly one house to the north (^), 
south (v), east (>), or west (<). After each move, he delivers another 
present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, 
and so his directions are a little off, and Santa ends up visiting some 
houses more than once. How many houses receive at least one present?

For example:

    - > delivers presents to 2 houses: one at the starting location, 
        and one to the east.
    - ^>v< delivers presents to 4 houses in a square, including twice to 
      the house at his starting/ending location.
    - ^v^v^v^v^v delivers a bunch of presents to some very lucky children 
      at only 2 houses.

--- Part Two ---
The next year, to speed up the process, Santa creates a robot version 
of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two 
presents to the same starting house), then take turns moving based 
on instructions from the elf, who is eggnoggedly reading from the 
same script as the previous year.

This year, how many houses receive at least one present?

For example:

    - ^v delivers presents to 3 houses, because Santa goes north, and 
      then Robo-Santa goes south.
    - ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa 
      end up back where they started.
    - ^v^v^v^v^v now delivers presents to 11 houses, with Santa going 
      one direction and Robo-Santa going the other.

"""
from collections import defaultdict

puzzle_input = open(__file__.replace('.py', '_input.txt')).read()

position = [0, 0]
houses = defaultdict(int)

def move(direction):
    if direction == '^':
        position[1] += 1
    elif direction == 'v':
        position[1] -= 1
    elif direction == '<':
        position[0] -= 1
    elif direction == '>':
        position[0] += 1
    houses[tuple(position)] += 1

for x in puzzle_input:
    move(x)

print(f'Part 1 Answer: {len(houses.keys()) + 1}')

santa_position = [0, 0]
robo_santa_position = [0, 0]

santa_houses = defaultdict(int)
robo_santa_houses = defaultdict(int)

santa_houses[(0, 0)] = 1
robo_santa_houses[(0, 0)] = 1

santa = puzzle_input[::2]
robo_santa = puzzle_input[1::2]

def move_santa(direction):
    if direction == '^':
        santa_position[1] += 1
    elif direction == 'v':
        santa_position[1] -= 1
    elif direction == '<':
        santa_position[0] -= 1
    elif direction == '>':
        santa_position[0] += 1
    else:
        raise Exception('unrecognized input!')
    santa_houses[tuple(santa_position)] += 1

def move_robo_santa(direction):
    if direction == '^':
        robo_santa_position[1] += 1
    elif direction == 'v':
        robo_santa_position[1] -= 1
    elif direction == '<':
        robo_santa_position[0] -= 1
    elif direction == '>':
        robo_santa_position[0] += 1
    else:
        raise Exception('unrecognized input!')
    robo_santa_houses[tuple(robo_santa_position)] += 1

for x in santa:
    move_santa(x)

for x in robo_santa:
    move_robo_santa(x)

visited_houses = list(set(santa_houses.keys()).union(robo_santa_houses.keys()))
print(f'Part 2 Answer: {len(visited_houses)}')
