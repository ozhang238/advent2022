#!/usr/bin/python
import advent2022 as adl
import sys

#========================DESCRIPTION============================================
name = ""
description = """\
Part1 : xxx
Part2 : xxx"""
debug = ""
#===============================================================================

def get_entries(filename): #split no empty lines, create list of lists
    return adl.read_file(filename)

def part01(filename):
    return get_entries(filename)

def part02(filename):
    return get_entries(filename)

#===============================================================================
parts = [part01, part02]