import os

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'
ORANGE = '\033[38;5;208m'

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print("Enchanting table language converter made by Spigg\n"
      "- Write any text to convert to minecraft enchanting table language\n"
      "- Write any enchaning table language to convert to text\n")
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
    content = input("").lower()
    if content == "--exit":
        os.system("py main.py")
    else:
        for char in content:
            result += substitution_map.get(char, thingmap.get(char, char))

        if not content == "": print(f"\033[F{content} {ORANGE} > {RESET} {result}")
