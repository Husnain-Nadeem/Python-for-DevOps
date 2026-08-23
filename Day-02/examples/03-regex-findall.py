import re

text = "The quick brown fox"
pattern = "brown"
if pattern in text:
    print("Pattern found:", pattern)

    
search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
