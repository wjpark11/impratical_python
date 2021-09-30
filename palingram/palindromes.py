"""find palindromes in a ditionary file"""
from load_dictionary import load

def is_palindrome(word):
    """determine a word is palindrome using recursion"""
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    else:
        stripped = word[1:-1]
        return is_palindrome(stripped)

def find_palindromes():
    """find palindromes in a ditionary file"""
    # Load digital dictionary file as a list of words
    word_list = load('dictionary.txt')

    # Create an empty list to hold palindromes
    palindromes_list = []

    # Loop through each word in the word list:
    for word in word_list:
    #     If word sliced forward is the same as word sliced backward:
        # if len(word) > 1 and word == word[::-1]:
        if is_palindrome(word):
    #         Append word to palindrome list
            palindromes_list.append(word)
    return palindromes_list


# Print palindrome list
if __name__ == '__main__':
    palindromes = find_palindromes()
    print(*palindromes, sep='\n')
