from collections import Counter
from load_dictionary import load


def find_anagrams(dictionary: list, word: str):
    """
    return available anagram words list from dictionary for given counter
    """
    input_counter = Counter(word)
    anagram_list = []
    for w in dictionary:
        word_counter = Counter(w.lower())        
        if not(word_counter - input_counter):
            anagram_list.append(w)
    return anagram_list


# load a dictionary file
dictionary = load('dictionary.txt')
dictionary.append('a')
dictionary.append('i')
dictionary = sorted(dictionary)

def main():
    # accept a name from user
    input_name = input("input a name to make anagram phrase: ")
    # set limit = length of name
    limit = len(input_name.lower())
    # start empty list to hold anagram phrase
    phrase = ""
    # while length of phrase < limit:
    while len(phrase) < limit:
    #     generate list of dictionary words that fit in name
        word_list = find_anagrams(dictionary, input_name.lower())
    #     present words to user
        print("Here are available words for phrase")
        print(*word_list, sep='\n')
    #     present remaining letters to user

    #     ask user to input word or start over
    #     if user input can be made from remaining letters:
    #         accept choice of new word or words from user
    #         remove letters in choice from letters in name
    #         return choice and remaining letters in name
    #     if choice is not a valid selection:
    #         ask user for new choice or let user start over
    #     add choice to phrarse and show to user
    #     generate new list of words and repeat process
    # when phrase length equals limit value:
    #     display final phrase
    #     ask user to start over to exit

print(find_anagrams(dictionary,input_name))