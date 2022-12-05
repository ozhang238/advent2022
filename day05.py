#!/usr/bin/python
import advent2022 as adl
import sys
import re

#========================DESCRIPTION============================================
name = "Supply Stacks"
description = """\
Part1 : Find what crate is on top after moves
Part2 : Multiple crates are moved at once"""
debug = ""
#===============================================================================

def get_entries(filename): #split no empty lines, create list of lists
    lines = adl.read_file_lines(filename)
    num_stacks=  int(len(lines[0])/4)
    stacks = []
    instructions = []
    for n in range(num_stacks):
        stacks.append([])
    for l in adl.read_file_lines(filename):
        if ('[' in l):
            for n in range(num_stacks):
                if l[n*4+1] != ' ':
                    stacks[n].append(l[n*4+1])
        if 'move' in l:
            m = re.match(r'move (\d+) from (\d) to (\d)',l)
            instructions.append([int(m.group(1)),int(m.group(2))-1,int(m.group(3))-1])
    return (stacks, instructions)

# take one instruction and use it
def process_stack(stacks, instruction, reverse=False):
    stack_slice = stacks[instruction[1]][:instruction[0]]
    if (reverse):
        stack_slice.reverse()
    stacks[instruction[1]] = stacks[instruction[1]][instruction[0]:]
    stacks[instruction[2]] = stack_slice + stacks[instruction[2]]
    return(stacks)

def get_top_of_stacks(stacks):
    return ''.join([s[0] if s[0] else ' ' for s in stacks])

def part01(filename):
    (stacks,instructions) =  get_entries(filename)
    for i in instructions:
        stacks = process_stack(stacks,i, reverse=True)
    return get_top_of_stacks(stacks)

def part02(filename):
    (stacks,instructions) =  get_entries(filename)
    for i in instructions:
        stacks = process_stack(stacks,i, reverse=False)
    return get_top_of_stacks(stacks)

#===============================================================================
parts = [part01, part02]