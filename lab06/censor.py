#!/usr/bin/env python3

# Michael Gates
# 9 October 2017
# Takes a string input and prints a 'censored' version as per user request



def replaceWord(sentence, word):
    """ Replaces a single word in a sentence with dashes"""
    return sentence.replace(word, "-"*len(word))

def replaceMultipleWords(sentence, words):
    """ Replaces one or more words in a sentence with dashes"""    
    splitWords = words.split()
    for i in range(0, len(splitWords)):
        word = splitWords[i]
        sentence = replaceWord(sentence, word)
    return sentence

def main():
    sentence = input("Enter a sentence: ")
    toReplace = input("Enter word(s) to replace: ")
    replacedSentence = replaceMultipleWords(sentence, toReplace)
    print("The resulting string is:\n" + replacedSentence)


if __name__ == '__main__':
    main()