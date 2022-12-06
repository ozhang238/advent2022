#!/usr/bin/python
import advent2022 as adl
import sys

#========================DESCRIPTION============================================
name = "Tuning Trouble"
description = """\
Part1 : Find the first start of marker. StartOfMessage is 4unique chars.
Part2 : Message is 14 unique chars"""
debug = ""
#===============================================================================

def get_entries(filename): #split no empty lines, create list of lists
    return adl.read_file(filename)

def is_marker(char_list):
    return len(set(char_list)) == len(char_list)

def get_first_marker(marker_length, char_stream):
    cache = []
    for c,i in zip(char_stream,range(len(char_stream))):
        if len(cache) < marker_length:
            cache.append(c)
        else:
            cache = cache[1:] + [c]
        if i >= marker_length and is_marker(cache):
            return i+1
    return 0
            
        
def part01(filename):
    return get_first_marker(4, get_entries(filename))

def part02(filename):
    return get_first_marker(14, get_entries(filename))

#===============================================================================
parts = [part01, part02]