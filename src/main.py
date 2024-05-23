import os
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
while True:
    substitution_map = {
        'a': 'ᔑ', 'b': 'ʖ', 'c': 'ᓵ', 'd': '↸', 'e': 'ᒷ', 'f': '⎓', 'g': '⊣',
        'h': '⍑', 'i': '╎', 'j': '⋮', 'k': 'ꖌ', 'l': 'ꖎ', 'm': 'ᒲ', 'n': 'リ',
        'o': '𝙹', 'p': '!', 'q': '¡', 'r': 'ᑑ', 's': '∷', 't': 'ᓭ', 'u': 'ℸ',
        'v': '⍊', 'w': '̣', 'x': '̇̇/', 'y': '⚍', 'z': '⍊', 'ä': 'ᔑᒷ', 'ö': '𝙹ᒷ',
        'ü': 'ℸᒷ', 'ß': '∷∷'
    }

    result = ""
    for char in input("> ").lower():
        result += substitution_map.get(char, char)

    print("\033[F\033[K" + result)