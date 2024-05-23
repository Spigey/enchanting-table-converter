substitution_map = {
    'a': 'ᔑ', 'b': 'ʖ', 'c': 'ᓵ', 'd': '↸', 'e': 'ᒷ', 'f': '⎓', 'g': '⊣',
    'h': '⍑', 'i': '╎', 'j': '⋮', 'k': 'ꖌ', 'l': 'ꖎ', 'm': 'ᒲ', 'n': 'リ',
    'o': '𝙹', 'p': '!', 'q': '¡', 'r': 'ᑑ', 's': '∷', 't': 'ᓭ', 'u': 'ℸ',
    'v': ' ', 'w': '̣', 'x': ' ', 'y': '⚍', 'z': '⍊'
}
text = input("Enter your text: ").lower()

result = ""
for char in text:
    result += substitution_map.get(char, char)  # Use original char if not found

print("Substituted text:", result)