#!/usr/bin/env python

import re
import sys

# a matcher to get individual parts of a BED line
from GUI import GUI

matcher = re.compile("(.+)\\t(.+)\\t(.+)")
entry_path = None

# for debugging
def read_file(path):
    """
    get a path to a BED file and return a list of lines from the file
    :param path:
    :return:
    """
    with open(path, 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def read_lines():
    lines = []
    for line in sys.stdin:
        lines.append(line)

    return lines


def get_solution(lines):
    """
    get a list of lines from BED file and return a dictionary of lists.
    the keys of the dictionary is the name of the chromosome.
    the list in each key contains tuples with this format:
    (<first base in sequence>, <last base in sequence>)
    :param lines:
    :return:
    """
    start = int(matcher.match(lines[0]).group(2))
    count = 0
    solution = {}
    chrom = None
    for i in range(1, len(lines)):
        chrom = matcher.match(lines[i]).group(1)  # we get the name of the chromosome
        # if it is a new chromosome we add a new item to the dictionary
        if chrom not in solution.keys():
            solution[chrom] = []
        # we test if the sequence has ended
        k = int(matcher.match(lines[i - 1]).group(2))
        j = int(matcher.match(lines[i]).group(2))
        # if so we enter a new sequence tuple to the list in the dictionary
        if j - k > 1:
            solution[chrom].append((start, start + count))
            start = j
            i += 1
            count = 0
        else:
            count += 1

    # we add the last sequence and return the solution
    solution[chrom].append((start, start + count))
    return solution


def find_sequences():
    """
    get a path and and return the solution inthe format specified in get_solution
    :param path:
    :return:
    """
    # lines = read_file(sys.argv[1])
    lines = read_lines()
    return get_solution(lines)


def main():
    # lines = read_file(sys.argv[1])
    # make the dictionary
    lines = read_lines()
    solution = get_solution(lines)
    # open the display window
    gui = GUI(solution)


if __name__ == '__main__':
    main()
