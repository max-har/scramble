#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %% IMPORT

import random

import nltk
#nltk.download('punkt_tab')
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# This script takes a text as input, scrambles the letters between the first and the last letter of each word in the text and outputs the modified text.

def shuffle(letter_list):
    '''Shuffle the elements between the first and last item'''
    # If the list has three or fewer elements, there is nothing to shuffle
    if len(letter_list) <= 3:
        return letter_list
    
    # Extract the first item, the middle part to shuffle, and the last item
    first_item = letter_list[0]
    middle_part = letter_list[1:-1]
    last_item = letter_list[-1]
    
    # Shuffle the middle part
    random.shuffle(middle_part)
    
    # Reconstruct the list
    shuffled_list = [first_item] + middle_part + [last_item]
    return shuffled_list

# take input
input_text = '''Melbourne’s magic coffee, a distinctive blend of double ristretto, steamed milk, and microfoam, epitomizes the city’s world-renowned coffee culture. Served in smaller cups to highlight its rich flavors, this beverage showcases Melbourne's barista expertise and commitment to quality, with beans sourced from sustainable farms. The city’s coffee shops offer a tranquil escape with stylish interiors, enhancing the overall experience. Magic coffee has become a symbol of Melbourne's dedication to excellence and community, attracting coffee enthusiasts globally. Experiencing this unique brew is essential for anyone visiting Melbourne, reflecting the city’s passion and innovation in coffee making.'''

# split input into list of words
sent_list = nltk.tokenize.sent_tokenize(input_text)
sent_list = [hyphenated_word.replace("-", " - ") for hyphenated_word in sent_list]
tok_sents_list = [nltk.tokenize.word_tokenize(sent) for sent in sent_list]

sents_list = []
for this_tok_sent_list in tok_sents_list:
    this_letter_sent_list = [[*my_str] for my_str in this_tok_sent_list]
    shuffled_lists = [shuffle(letter_list) for letter_list in this_letter_sent_list]
    shuffled_words_list = [''.join(shuffled_list) for shuffled_list in shuffled_lists]
    this_sent = nltk.tokenize.treebank.TreebankWordDetokenizer().detokenize(shuffled_words_list)
    
    sents_list.append(this_sent)
    output_text = ' '.join(sents_list)
    output_text = output_text.replace(" ’ ", "’")
    output_text = output_text.replace(" “ ", " “")
    output_text = output_text.replace(" “ ", " “")
    output_text = output_text.replace(" ” ", "” ")
    output_text = output_text.replace(" - ", "-")

print(output_text)
