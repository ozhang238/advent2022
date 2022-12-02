#!/usr/bin/python
import advent2022 as adl
import sys


#========================DESCRIPTION============================================
name = "Calorie Counting"
description = """\
Part1 : Find the max number of calories that an elf is carrying. 
        Each group of numbers is a bag of calories.
Part2 : Find the sum of the three largest bags of calories."""
debug = ""
#===============================================================================

def get_entries(filename): #split no empty lines, create list of lists
    return [[int(x) for x in y.split('\n')] for y in adl.read_file(filename).split('\n\n')]

def part01(filename):
    return max([sum(x) for x in get_entries(filename)])

def part02(filename):
    return sum(sorted([sum(x) for x in get_entries(filename)],reverse=True)[0:3])

#================================================================================
parts = [part01, part02]