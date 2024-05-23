import os

while True:
    substitution_map = {
        'a': 'ᔑ', 'b': 'ʖ', 'c': 'ᓵ', 'd': '↸', 'e': 'ᒷ', 'f': '⎓', 'g': '⊣',
        'h': '⍑', 'i': '╎', 'j': '⋮', 'k': 'ꖌ', 'l': 'ꖎ', 'm': 'ᒲ', 'n': 'リ',
        'o': '𝙹', 'p': '!', 'q': '¡', 'r': 'ᑑ', 's': '∷', 't': 'ᓭ', 'u': 'ℸ',
        'v': ' ', 'w': '̣', 'x': ' ', 'y': '⚍', 'z': '⍊'
    }

    result = ""
    for char in input("> ").lower():
        result += substitution_map.get(char, char)

    print(result)