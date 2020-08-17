'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

#SUDO CODE

# we are looking to see if the combination of "th" occurs in a word (i.e. within, this, that, the other)

# I NEED:
#     a) a base case wher ethe word is less than 2. In that case I would return 0 because you can only have 0 instances of a substring from a string shorter than 2 characters.
#     b) to check and see if an instance of "th" is at the start of the word. IF YES, I need to recurse and return a counter.
#     c) use a new recursive call starting at the next index of "word" to go trho the entire word to check it for additional instances of "th"

# K. I have 3 cases to deal with. Base case = 0. Simple Case is 1, PLUS the recursive call to check the rest of the word.


def count_th(word):
    target = "th"

    #base case - word is less than 2. return 0
    if len(word) < 2:
        return 0

    #check to see if the beginning of the word starts with "th".
    if word[:2] == target:
        return count_th(word[1:]) + 1

    #if the beginning of the word is NOT a "th", then we want to iterate to teh next letter in the word and repeat the process
    return count_th(word[1:])