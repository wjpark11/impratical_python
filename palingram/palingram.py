"""find all word-pair palingrams in a dictionary file"""
from load_dictionary import load

# load digital ditionary as a list of words
word_list = load("dictionary.txt")

def find_palingrams():
    """find all word-pair palingrams in a dictionary file"""
    # start an empty list to hold palingrams
    palingram_list = []

    # for word in word list:
    for word in word_list:
    #     get length of word
        word_length = len(word)
    #     if length > 1:
        if word_length > 1:
    #         loop through the letters in the word:
            for i in range(word_length):
                front = word[:i]
                back = word[i:]
    #             if reversed word fragment at front of words is in word list
    #             and letters after form a palindromic sequence:
                if front[::-1] in word_list and back == back[::-1]:
    #                 append word and reversed word to palingram list
                    palingram_list.append(f'{word} {front[::-1]}')
    #             if reversed word fragment at end of word is in word list
    #             and letters before form a palindromic sequence:
                if back[::-1] in word_list and front == front[::-1]:
    #                 append reversed word and word to palingram list
                    palingram_list.append(f'{back[::-1]} {word}')
    # sort palingram list alphabetically
    palingram_list.sort()
    return palingram_list

# print word-pair palingrams from palingram list
if __name__ == '__main__':
    sorted_palingrams = find_palingrams()
    print(*sorted_palingrams, sep='\n')
