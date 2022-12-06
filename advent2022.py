#!/usr/bin/python
import sys
import importlib

result_fmt = 'Part%d answer is : %s'
input_fmt = 'day%02d_part%02d.txt'
py_fmt = 'day%02d.py'

separator = "="*80

day_template = """#!/usr/bin/python
import advent2022 as adl
import sys

#========================DESCRIPTION============================================
name = ""
description = \"\"\"\\
Part1 : xxx
Part2 : xxx\"\"\"
debug = ""
#===============================================================================

def get_entries(filename): #split no empty lines, create list of lists
    return adl.read_file(filename)

def part01(filename):
    return get_entries(filename)

def part02(filename):
    return get_entries(filename)

#===============================================================================
parts = [part01, part02]"""

def read_file(filename):
    return open(filename,'r').read().rstrip()

def read_file_lines(filename):
    return [x.rstrip() for x in open(filename,'r').readlines()]

def read_file_lines_no_strip(filename):
    return [x for x in open(filename,'r').readlines()]

def print_result(day, part, part_func):
    print(result_fmt % (part, part_func(input_fmt % (day, part))))
    
def day_N(N, name, parts, description = "", debug = ""):
    print(separator + "\n"+ ("Day %d : %s" % (N, name)))
    if (description):
        print(separator+"\n"+description)
    if (debug):
        print(separator+"\n"+debug)
    print(separator)
    [print_result(N, *x) for x in zip(range(1, len(parts)+1), parts) ]


def gen_template(day):
    with open(py_fmt % day ,'w') as f:
        f.write(day_template)
    with open(input_fmt % (day, 1) ,'w') as f:
        f.write('0')
    with open(input_fmt % (day, 2) ,'w') as f:
        f.write('0')
    
def gen_template_range(start,stop):
    [gen_template(x) for x in range(start, stop)]

def import_and_exec(day):
    day_module = importlib.import_module('day%02d' % day)
    day_N(day, day_module.name, day_module.parts, description = day_module.description, debug=day_module.debug)

def main(argv):
    if (len(argv) == 2):
        import_and_exec(int(argv[1]))
    else:
        gen_template_range(int(argv[1]), int(argv[2]))

if __name__ == "__main__":
    main(sys.argv)