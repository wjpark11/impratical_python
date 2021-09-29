"""convert a sentence to 'poor' occurence bar chart"""
from pprint import pprint
from collections import defaultdict

sentence = input("input a sentence: ")

word_dict = defaultdict(list)
for alphabet in sentence:
    if alphabet.lower() in 'abcdefghijklmnopqrstuvwxyz':
        word_dict[alphabet.lower()].append(alphabet.lower())

pprint(word_dict)
