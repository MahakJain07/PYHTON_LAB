with open('abc.txt') as f:
    text = f.read().splitlines() # list of lines
print(text)
lines = len(text)
words = sum(len(line.split()) for line in text)
characters = sum(len(line) for line in text)
file_size_in_bytes = characters + (lines) + 2
print(lines)
print(words)
print(characters)
print(file_size_in_bytes)

import os
file_size = os.path.getsize('abc.txt')
print("file size is :", file_size, "bytes")