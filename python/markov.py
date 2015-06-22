#!/usr/bin/env python


from sys import argv
import string
import random


script, input_text, output_length = argv

output_length = int(output_length)

suf_map = {}
pre = ()
list_words = []
text_block = []


def process_text(f):
    """Reads in text file, splits into words and pushes words to a list"""
    fin = open(f)
    for line in fin:
        # line = line[0].capitalize() + line[1:] # experiment with keeping capitalization
        for word in line.strip().split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            if word in ('i', "i'm", "i've"):
                word = word.replace('i', 'I')
            list_words.append(word)
    map_words(list_words)


def map_words(lst):
    """Creates suffix map, suf_map"""
    global pre
    for i in range(len(lst) - 2):
        pre = (lst[i], lst[i + 1])
        val = lst[i + 2]
        try:
            suf_map[pre].append(val)
        except KeyError:
            suf_map[pre] = [val]


def generate_text(n):
    """Generates random text"""
    start = random.choice(suf_map.keys())
    for i in range(n):
        suf = random.choice(suf_map[start])
        text_block.append(suf) 
        start = (start[1], suf)
    format_text(text_block)


#### I tried a version that kept the capitals at the beginning of each line,
#### but felt this didn't make the text random enough.
# def format_text(lst):
#     for word in lst:
#         if word[0].isupper() and word != 'I':
#             print '\n' + word,
#         else:
#             print word,


def format_text(lst):
    """Formats and prints text"""
    count = 0
    while count < len(lst):
        line_length = random.randint(3,7)
        line = lst[count : count + line_length]
        print ' '.join(line)
        count += line_length


if __name__ == '__main__':
    process_text(input_text) 
    generate_text(output_length)

