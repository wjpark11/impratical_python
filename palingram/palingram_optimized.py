"""find all word-pair palingrams in a dictionary file"""
from load_dictionary import load

word_list = load("dictionary.txt")
word_set = set(word_list)

def find_palingrams_optimized():
    """find all word-pair palingrams in a dictionary file"""

    palingram_list = []

    for word in word_list:
        word_length = len(word)
        if word_length > 1:
            for i in range(word_length):
                front = word[:i]
                back = word[i:]
                if front[::-1] in word_set and back == back[::-1]:
                    palingram_list.append(f'{word} {front[::-1]}')
                if back[::-1] in word_set and front == front[::-1]:
                    palingram_list.append(f'{back[::-1]} {word}')
    palingram_list.sort()
    return palingram_list

if __name__ == '__main__':
    sorted_palingrams = find_palingrams_optimized()
    print(*sorted_palingrams, sep='\n')