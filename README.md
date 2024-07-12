Illumio Technical Assessment


Program: word_counter.py
This program reads a file and finds matches against a predefined set of words.
It will output each word and the number of matches in descending order.

Note:
    The program "word_counter.py" has been written in Python version 3.9.6. 
    So, make sure to install python version 3.9 or above before running the program.





How to run the program?

To run the program, unzip the file and execute the following from the folder where "word_counter.py" is present:

    python3 word_counter.py {predefined_words_file} {input_file}

The program takes two command line arguments.
predefined_words_file: The file that contains the predefined set of words (one word per line).
input_file: The file that needs to used to match the predefined words.
Provide the file names/paths of the predefined words file and the input file as arguments as shown in the command above.
Output will be printed to the console in the format "Predefined Word : Match Count".

If the output is too long, execute the following to redirect it to a file (if mac or linux/unix):

    python3 word_counter.py {predefined_words_file} {input_file} > output.txt

This will write the output to a file named "output.txt". Open it to check the output.





What has been tested?

To test the program, the given example from the email has been taken and tested.
The words have been kept in util/words.txt file and the lines in util/test.txt file.
The following test has been carried out to verify:

    python3 word_counter.py util/words.txt util/test.txt > output.txt

Sample output:

    name : 2
    ai : 1
    detect : 0

In addition, a large sample text file has been taken from the internet (https://norvig.com/big.txt).
A parser program is written which will read this text file and create a words file to use as predefined set of words.
This program (word_parser.py) is placed in "util" folder. It will create a words file with list of words line by line.
To run this program, execute the following:

    python3 util/word_parser.py {input_file} {words_file_name}

The program takes two command line arguments.
input_file: The file that contains the sample text.
words_file_name: The output file where the words will be written to line by line.

The sample text file is attached in the util folder as "big.txt". 
The following test has been carried out to verify:

    python3 util/word_parser.py util/big.txt util/word.txt
    python3 word_counter.py util/word.txt util/big.txt > output.txt

Sample output:

    the : 79379
    of : 39996
    and : 38092
    to : 28611
    in : 21776





Assumptions: The following assumptions have been made while coding the program.

1. The predefined words file will contain words listed one per line.
2. The predefined words file does not contain duplicates.
3. There can be up to 10k words. It is reasonably assumed that they will fit in memory while testing.
4. Matches should be case-insensitive. So, all words are printed in lower case in the output for convenience.
5. The match should be word-to-word match, no substring matches.
6. Matches should ignore immediate punctuation marks (string.punctuation) like full-stops(.), commas(,)etc.
7. The output is expected to be in descending order of the match count.
8. Any more output requirements expected were not catered to, as they weren't clear from the email.
