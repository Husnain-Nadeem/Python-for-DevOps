import re

text = "The quick brown fox quick"
pattern = "quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
