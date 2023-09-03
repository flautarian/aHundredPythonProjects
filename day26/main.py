
from random import randint

input_name = str(input("Tell me the word to dictionaryze!!"))

dictionary = {
    "a": ["Alabama"],
    "b": ["Boromir"],
    "c": ["Catalunya"],
    "d": ["Detonator"],
    "e": ["Estimatory"],
    "f": ["Flame"],
    "g": ["Grose"],
    "h": ["Hello"],
    "i": ["Italian"],
    "j": ["Joel"],
    "k": ["Kakarotto"],
    "l": ["Lion"],
    "m": ["Monster"],
    "n": ["Nigger"],
    "o": ["Ornitology"],
    "p": ["Peta"],
    "q": ["Quit"],
    "r": ["Romatory"],
    "s": ["Southern"],
    "t": ["Tivalt"],
    "u": ["Uganda"],
    "v": ["Vallery"],
    "w": ["Wakanda"],
    "x": ["Xaxophone"],
    "y": ["Yay"],
    "z": ["Ziggar"],
}

final_word_dictionarized = []

""" for word in input_name:
    new_word = dictionary[word.lower()][randint(0, len(dictionary[word.lower()]))]
    final_word_dictionarized.append(new_word) """
    
final_word_dictionarized = [dictionary[word.lower()][randint(0, len(dictionary[word.lower()])-1)] for word in input_name]
    
print(final_word_dictionarized)
    