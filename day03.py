#!/usr/bin/python
import advent2022 as adl
import sys

#========================DESCRIPTION============================================
name = "Rucksack Reorganization"
description = """\
Part1 : What is the sum of items that appear in both compartments.
Part2 : Check badge types. Same item appears in 3 elves bags. Sum them."""
debug = ""
#===============================================================================

def char_to_prio(character):
    if ord(character) >= 97:
        return ord(character) - 96
    else:
        return ord(character) - 38
    
def split_list_into_sets(m_list):
    return [set(m_list[:int(len(m_list)/2)]),set(m_list[int(len(m_list)/2):])]

def split_list_into_N_chunks(N, l):
    return [l[i:i + N] for i in range(0, len(l), N)]

def get_intersects(set_pair):
    return set_pair[0].intersection(set_pair[1])

def get_intersects_triple(set_triple):
    return set_triple[0].intersection(set_triple[1]).intersection(set_triple[2])

def get_entries(filename): #split no empty lines, create list of lists
    return [split_list_into_sets([*x.rstrip()]) for x in adl.read_file_lines(filename)]

def get_entries2(filename): #split no empty lines, create list of lists
    return split_list_into_N_chunks(3, [set([*x.rstrip()]) for x in adl.read_file_lines(filename)])

def part01(filename):
    return sum([ sum([char_to_prio(intersect) for intersect in get_intersects(x)]) for x in get_entries(filename)])

def part02(filename):
  return sum([ sum([char_to_prio(intersect) for intersect in get_intersects_triple(x)]) for x in get_entries2(filename)])


#===============================================================================
parts = [part01, part02]