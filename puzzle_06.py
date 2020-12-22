"""
Advent of Code 2015: Day 6 - Probably a Fire Hazard

--- Part 1 ---
Because your neighbors keep defeating you in the holiday house decorating 
contest year after year, you've decided to deploy one million lights in a 
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has 
mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the 
lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions 
include whether to turn on, turn off, or toggle various inclusive ranges 
given as coordinate pairs. Each coordinate pair represents opposite corners 
of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore 
refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights 
by doing the instructions Santa sent you in order.

For example:

    - turn on 0,0 through 999,999 would turn on (or leave on) every light.
    - toggle 0,0 through 999,0 would toggle the first line of 1000 lights, 
      turning off the ones that were on, and turning on the ones that were off.
    - turn off 499,499 through 500,500 would turn off (or leave off) the 
      middle four lights.

After following the instructions, how many lights are lit?

--- Part 2 ---
You just finish implementing your winning light pattern when you realize 
you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; 
each light can have a brightness of zero or more. The lights all start 
at zero.

The phrase turn on actually means that you should increase the brightness 
of those lights by 1.

The phrase turn off actually means that you should decrease the brightness 
of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness 
of those lights by 2.

What is the total brightness of all lights combined after following 
Santa's instructions?

For example:

    - turn on 0,0 through 0,0 would increase the total brightness by 1.
    - toggle 0,0 through 999,999 would increase the total brightness by 2000000.

"""
import collections
import enum
import re

puzzle_input = open(__file__.replace('.py', '_input.txt')).read()

class LightState(enum.Enum):
    OFF = 0 
    ON = 1
    TOGGLE = 2

# Parse the Puzzle Input and create a list of operations to perform
# on the lights.
actions = []

pattern = re.compile(r'([0-9]+,[0-9]+)')
for line in puzzle_input.splitlines():
    action = None
    startPos = None
    endPos = None
    if line.startswith('turn on'):
        action = LightState.ON
    elif line.startswith('turn off'):
        action = LightState.OFF
    elif line.startswith('toggle'):
        action = LightState.TOGGLE
    
    coordinates = re.findall(pattern, line)
    startPos = tuple([int(x)for x in coordinates[0].split(',')])
    endPos = tuple([int(x)for x in coordinates[1].split(',')])
    actions.append([action, startPos, endPos])

# Lights default to off.
lights = collections.defaultdict(bool)

def set_light_status(startPos, endPos, action):
    global lights
    x1, y1 = startPos
    x2, y2 = endPos
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if action == LightState.ON:
                lights[(x, y)] = True
            elif action == LightState.OFF:
                lights[(x, y)] = False
            elif action == LightState.TOGGLE:
                lights[(x, y)] = not lights[(x, y)]

for action, startPos, endPos in actions:
    set_light_status(startPos, endPos, action)

print(f'Part 1 Answer: {sum(lights.values())}')

# --- Part 2 ------------------------------------------------------------------
lights = collections.defaultdict(int)

def set_light_brightness(startPos, endPos, action):
    global lights
    x1, y1 = startPos
    x2, y2 = endPos
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if action == LightState.ON:
                lights[(x, y)] += 1
            elif action == LightState.OFF:
                lights[(x, y)] = max(lights[(x, y)] - 1, 0)
            elif action == LightState.TOGGLE:
                lights[(x, y)] += 2

for action, startPos, endPos in actions:
    set_light_brightness(startPos, endPos, action)

print(f'Part 2 Answer: {sum(lights.values())}')
