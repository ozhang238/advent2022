#!/usr/bin/python
import advent2022 as adl
import sys

#========================DESCRIPTION============================================
name = "Camp Cleanup"
description = """ \
Part1 : Check ranges to make sure an elf has an actual job. Count failures.
Part2 : Check also partial overlaps."""
debug = ""
#===============================================================================

def check_range_pair_full_overlap(pair):
    return (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) or \
           (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1])

def check_range_pair_some_overlap(pair):

    return (pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]) or \
           (pair[1][0] >= pair[0][0] and pair[1][0] <= pair[0][1])

def get_entries(filename): 
    return [ [[int(z) for z in y.split('-')] for y in x.split(',')] for x in adl.read_file_lines(filename)]

def part01(filename):
    return sum([check_range_pair_full_overlap(x) for x in get_entries(filename)])

def part02(filename):
    return sum([check_range_pair_some_overlap(x) for x in get_entries(filename)])

#===============================================================================
parts = [part01, part02]