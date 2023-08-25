#!/usr/bin/env python

"""
Simple zipf test script for text files
based on https://hpc-carpentry.github.io/hpc-python/11-snakemake-intro/"""

import sys
from wordcount import load_word_counts

def top_two_word(counts):
    """
    Given a list of (word, count, percentage) tuples,
    return the top two word counts.
    """
    limited_counts = counts[0:2]
    count_data = [count for (_, count, _) in limited_counts]
    return count_data

if __name__ == '__main__':
    input_files = sys.argv[1:]
    print("Book\tFirst\tSecond\tRatio")
    for input_file in input_files:
        counts = load_word_counts(input_file)
        [first, second] = top_two_word(counts)
        bookname = input_file[:-4]
        print(f"{bookname}\t{first}\t{second}\t{first/second:.2}")
