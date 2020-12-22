"""
Advent of Code 2015: Day 5 - Doesn't He Have Intern-Elves For This?

--- Part 1 ---
Santa needs help figuring out which strings in his text file are naughty 
or nice.

A nice string is one with all of the following properties:

    - It contains at least three vowels (aeiou only), like aei, xazegov, or 
      aeiouaeiouaeiou.
    - It contains at least one letter that appears twice in a row, like xx, 
      abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    - It does not contain the strings ab, cd, pq, or xy, even if they are 
      part of one of the other requirements.

For example:

    - ugknbfddgicrmopn is nice because it has at least three vowels 
      (u...i...o...), a double letter (...dd...), and none of the 
      disallowed substrings.
    - aaa is nice because it has at least three vowels and a double letter, 
      even though the letters used by different rules overlap.
    - jchzalrnumimnmhp is naughty because it has no double letter.
    - haegwjzuvuyypxyu is naughty because it contains the string xy.
    - dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

"""
import re

puzzle_input = open(__file__.replace('.py', '_input.txt')).read()

double_character = re.compile(r'(.)\1+')
invalid_substrings = ['ab', 'cd', 'pq', 'xy']

def count_vowels(string):
    return sum(map(string.count, 'aeiou'))

def contains_invalid_substrings(string):
    for substring in invalid_substrings:
        if substring in string:
            return True
    return False

def contains_doubles(string):
    results = re.search(double_character, string)
    if results:
        return True
    return False

niceCount = 0
for string in puzzle_input.splitlines():
    if (count_vowels(string) >= 3 and 
        contains_doubles(string) and 
        not contains_invalid_substrings(string)):
        niceCount += 1

print(f'Part 1 Answer: {niceCount}')

# --- Part 2 ------------------------------------------------------------------
def contains_repeat(string):
    for i in range(len(string)):
        try:
            chr = string[i+2]
        except:
            pass
        else:
            if chr == string[i]:
                return True
    return False

def contains_doubles2(string):
    for i in range(len(string)):
        try:
            testStr = string[i] + string[i+1]
        except:
            pass
        else:
            if string.count(testStr) >= 2:
                return True
    return False

niceCount = 0
for string in puzzle_input.splitlines():
    if contains_repeat(string) and contains_doubles2(string):
        niceCount += 1

print(f'Part 2 Answer: {niceCount}')

