"""
This program will read a big file (a file with lots of paragraphs)
and create a file with a list of words from the big file line by line)
"""

import argparse
import logging
import string

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# parse command line arguments
parser = argparse.ArgumentParser("python3 word_parser.py")
parser.add_argument("input_file", help=" file path of input file to read", type=str)
parser.add_argument("output_file", help=" file path of output file to write words to", type=str)
parser.add_argument("limit_words", nargs='?', help=" flag to indicate whether to limit words or not", type=bool, default=False)
parser.add_argument("word_limit", nargs='?', help=" number of words to set as limit", type=int, default=10000)
args = parser.parse_args()
logging.info(args)

INPUT_FILE_PATH = args.input_file
OUTPUT_FILE_PATH = args.output_file
LIMIT_WORDS = args.limit_words
WORD_LIMIT = args.word_limit

# word set
word_set = set()

logging.info(f'reading file {INPUT_FILE_PATH}')

with open(INPUT_FILE_PATH) as ifp:
    """ read file and create word set """
    line_count = 0

    # read line by line
    for line in ifp:
        line_count += 1
        logging.debug(f'{line_count}: {line}')
        # remove punctuation marks
        line = line.translate(str.maketrans('', '', string.punctuation))
        logging.debug(f'{line_count}: {line}')

        # create word set
        for word in line.split():
            # case insensitive
            word = word.strip().lower()
            if word:
                word_set.add(word)

        # if number of words is to be limited, exit when word limit reached
        logging.debug(f'word_set len: {len(word_set)}')
        if LIMIT_WORDS and len(word_set) >= WORD_LIMIT:
            break

logging.info(f'word set of size {len(word_set)} created')
logging.debug(f'word_set: {word_set}')

logging.info(f'writing to file {OUTPUT_FILE_PATH}')
with open(OUTPUT_FILE_PATH, 'w') as ofp:
    for word in word_set:
        ofp.write(word + "\n")

logging.info(f'word file created at {OUTPUT_FILE_PATH}')
