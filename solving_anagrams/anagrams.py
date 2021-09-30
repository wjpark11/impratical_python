"""from user input, find anagrams from a dictionary file"""
from load_dictionary import load

def find_anagram():
    # load digital dictionary file as a list of words
    word_list = load('dictionary.txt')
    # accept a word from user
    user_word = input("Enter a word for finding anagrams: ")
    # create an empty list to hold anagrams
    anagrams = []
    # sort the user-word
    sorted_user_word = sorted(user_word.lower())
    # loop through each word in the word list:
    for word in word_list:
    #     sort the word
        sorted_word = sorted(word)
    #     if word sorted is equal to user-word sorted:
        if sorted_user_word == sorted_word:
    #         append word to anagram list
            anagrams.append(word)
    return anagrams

# print anagram list
if __name__ == '__main__':
    anagram_list = find_anagram()
    print(*anagram_list, sep='\n')
