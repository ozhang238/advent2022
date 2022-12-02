#!/usr/bin/python
import advent2022 as adl
import sys

#========================DESCRIPTION============================================
name = "Rock Paper Scissors"
description = """\
Part1 : Calculate according to the strategy.
Part2 : Actually X(lose) Y(tie) Z(win) means how you need to win lose or draw..."""
debug = ""
#===============================================================================

#rock = A    X   1
#paper = B   Y   2
#scissor = C Z   3
score_dict = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}
win_tuples = [('A','Y'),('B','Z'),('C','X')]
tie_tuples = [('A','X'),('B','Y'),('C','Z')]
lose_tuples = [('A','Z'),('B','X'),('C','Y')]
win_score = 6
tie_score = 3

def tuple_to_dict(tuples):
    new_dict = dict()
    for t in tuples:
        new_dict[t[0]] = t[1]
    return new_dict

win_dict = tuple_to_dict(win_tuples)
tie_dict = tuple_to_dict(tie_tuples)
lose_dict = tuple_to_dict(lose_tuples)

def calc_duel_score(strat_tuple):
    if (strat_tuple in win_tuples):
        return win_score
    elif (strat_tuple in tie_tuples):
        return tie_score
    else:
        return 0
    
def calc_score(strat_tuple):
    return calc_duel_score(strat_tuple) + score_dict[strat_tuple[1]]

def calc_choice(strat_tuple):
    if (strat_tuple[1] == 'X'): #lose
        return lose_dict[strat_tuple[0]]
    elif (strat_tuple[1] == 'Y'): #tie
        return tie_dict[strat_tuple[0]]
    elif (strat_tuple[1] == 'Z'): #lwin
        return win_dict[strat_tuple[0]]
    
def calc_score2(strat_tuple):
    return calc_score(tuple([strat_tuple[0],calc_choice(strat_tuple)]))

def get_entries(filename): #split no empty lines, create list of lists
    return [tuple(x.rstrip().split(' ')) for x in adl.read_file_lines(filename)]

def part01(filename):
    return sum([calc_score(x) for x in get_entries(filename)])

def part02(filename):
    return sum([calc_score2(x) for x in get_entries(filename)])

#===============================================================================
parts = [part01, part02]