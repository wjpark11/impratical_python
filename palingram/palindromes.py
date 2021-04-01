from load_dictionary import load

# Load digital dictionary file as a list of words
dict = load('dictionary.txt')

# Create an empty list to hold palindromes
palindromes = []

# Loop through each word in the word list:
for word in dict:
#     If word sliced forward is the same as word sliced backward:
    if len(word) > 1 and word == word[::-1]:
#         Append word to palindrome list
        palindromes.append(word)

# Print palindrome list
print(*palindromes, sep='\n')
