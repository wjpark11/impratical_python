import sys
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

def process_choice(name):
    """
    Check user choice validity
    return - choice, leftover letters
    """
    while True:
    #     ask user to input word or start over
        choice = input("Make a word choice(Enter for start over, # for to end): ")
        if choice == "":
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
    #     if user input can be made from remaining letters:
        if len(name) - len(left_over_list) == len(candidate):
            break
    #     if choice is not a valid selection:
        else:
    #         ask user for new choice or let user start over
            print("Error! Make another choice")
    #         accept choice of new word or words from user
    #         remove letters in choice from letters in name
    name = ''.join(left_over_list)
    #         return choice and remaining letters in name
    return choice, name

# load a dictionary file
dictionary = load('dictionary.txt')
dictionary.append('a')
dictionary.append('i')
dictionary = sorted(dictionary)

def main():
    # accept a name from user
    input_name = input("input a name to make anagram phrase: ")
    name = ''.join(input_name.lower().split())
    name = name.replace('-','')
    # set limit = length of name
    limit = len(name)
    # start empty list to hold anagram phrase
    phrase = ""
    # while length of phrase < limit:
    running = True
    while running:
        temp_phrase = phrase.replace(' ','')
        if len(temp_phrase) < limit:
    #     generate list of dictionary words that fit in name
            word_list = find_anagrams(dictionary, name)
    #     present words to user
            print(f"Length of anagram phrase = {len(temp_phrase)}")
            print(f"Number of remaining characters : {limit-len(temp_phrase)}")
            print(f"Current phrase = {phrase}")
            print("Here are available words for phrase")
            print(*word_list, sep='\n')
    #     present remaining letters to user
            choice, name = process_choice(name)
    #     add choice to phrarse and show to user
            phrase += choice+' '
    #     generate new list of words and repeat process
    # when phrase length equals limit value:
        elif len(temp_phrase) == limit:
    #     display final phrase
            print("FINISHED!!")
            print(f"Anagram Name : {input_name}")
            print(f"Your Phrase : {phrase}")
            print()
    #     ask user to start over to exit
            try_again = input("Try again?(Enter to try again, 'n' to quit): ")
            if try_again.lower() == 'n':
                running = False
                sys.exit()
            else:
                main()

if __name__ == '__main__':
    main()

