from pathlib import Path
from collections import Counter
import re
path = Path('text.txt')
with open(path, 'r', encoding='utf-8') as f:
    data = f.read()
num_lines = len(data.splitlines())
print(f"Рядків : {num_lines}")
num_chars = len(data)
print(f"Символів : {num_chars}")
words = data.split()
num_words = len(words)
print(f"Слів : {num_words}\n\n")

print("Топ 10 найуживаніших слів")
clean = re.sub(r'[^\w\s]', '', data)
words = clean.split()
for word , count in Counter(words).most_common(10):
    print(f"{word}: {count}")