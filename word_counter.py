"""
This program will read a file with a list of predefined words written line by line.
It will then read another sample file and count the number of times each predefined word appears.
"""

import argparse
import logging
import string

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# parse command line arguments
parser = argparse.ArgumentParser("python3 word_counter.py")
parser.add_argument("predefined_words_file", help=" file path of predefined words", type=str)
parser.add_argument("input_file", help=" file path of input file to match words", type=str)
parser.add_argument("sort_flag", nargs='?', help=" flag indicating whether to sort word counts or not", type=str, default='True')
args = parser.parse_args()
logging.info(args)

PREDEFINED_WORDS_FILE_PATH = args.predefined_words_file
SAMPLE_FILE_PATH = args.input_file

# A hashmap to store the words as key and their frequency as value
word_count = dict()

logging.info(f'reading file {PREDEFINED_WORDS_FILE_PATH}')
with open(PREDEFINED_WORDS_FILE_PATH) as fp:
    """ read predefined words file line by line and store words """
    for line in fp:
        # assuming one word per line
        # case insensitive
        word = line.strip().lower()
        word_count[word] = 0

logging.info(f'done reading predefined words file')
logging.debug(f'word_count: {word_count}')

logging.info(f'reading file {SAMPLE_FILE_PATH} to match predefined words')
with open(SAMPLE_FILE_PATH) as fp:
    """ read predefined words file line by line and store words """
    for line in fp:
        # remove punctuation marks
        line = line.translate(str.maketrans('', '', string.punctuation))
        # read word by splitting line based on spaces
        for word in line.split():
            # case insensitive
            word = word.strip().lower()
            if word in word_count:
                word_count[word] += 1

logging.info(f'done reading sample file')
logging.info(f'matched and counted all words')
logging.debug(f'word_count: {word_count}')

if args.sort_flag == 'True':
    logging.info(f'sorting word counts in descending order')
    word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    logging.info(f'word counts sorted and ready')

logging.info(f'Predefined Word : Match Count')
for word in word_count:
    """ print output """
    print(f'{word} : {word_count[word]}')

logging.info(f'word counts printed')
