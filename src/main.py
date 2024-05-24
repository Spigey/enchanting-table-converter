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
    thingmap = {value: key for key, value in substitution_map.items()}

    result = ""
    content = input("> ").lower()
    if "--invert" in content:
        content = content.replace("--invert", "")
        for char in content:
            result += thingmap.get(char, char)
    else:
        for char in content:
            result += substitution_map.get(char, char)

    print("\033[F\033[K" + result)