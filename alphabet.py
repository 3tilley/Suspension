from __future__ import print_function

vowels = ["A", "E", "I", "O", "U"]

def count_vowels(letters):
    count_vowels = 0
    for letter in letters:
        if letter in vowels:
            count_vowels = count_vowels + 1
    
    return count_vowels

def charlotte(letters):
    name = "CHARLOTTE"
    matching_letters = 0
    non_dupicles = set()
    for letter in letters:
        for charlotte_letter in name:
            if letter == charlotte_letter:
                non_dupicles.add(letter)
    
    return len(non_dupicles)