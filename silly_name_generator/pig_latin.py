"""convert a word to pig latin word"""

def main():
    """
    convert a word to pig latin word
    """
    print("Pig Latin Converter")
    while True:
        word = input("Type word to convert to pig latin: ")
        if word[0] in ('a', 'e', 'i', 'o', 'u'):
            pig_latin_word = word+'way'
        else:
            pig_latin_word = word[1:]+word[0]+'ay'
        print(pig_latin_word)
        answer = input("enter 'q' for quit: ")
        if answer.upper() == 'Q':
            break

    input("Good bye")

if __name__ == '__main__':
    main()
    