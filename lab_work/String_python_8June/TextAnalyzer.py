# write a program to analyze Text Compression
# 1. Count occurrences of each character.  
# 2. Create a dictionary of character frequencies.  
# 3. Display unique characters.  
# 4. Find the most frequent character.  
# 5. Create a compressed output:  A3B3C3D3A3 
# 6. Calculate compression ratio.  
# --------------------------------------------------
#create a sample data
text = "AAABBBCCCDDDAAA"
# Count occurrences and create frequency dictionary
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("Original Text:", text)
print("\nCharacter Frequencies:")
for key, value in freq.items():
    print(key, "->", value)
# 3. Display unique characters
unique_chars = []
for ch in text:
    if ch not in unique_chars:
        unique_chars.append(ch)
print("\nUnique Characters:", unique_chars)
# 4. Find most frequent character
most_char = ""
max_count = 0
for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        most_char = key
print("Most Frequent Character:", most_char)
# 5. Create compressed output
compressed = ""
count = 1
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1
compressed += text[-1] + str(count)
print("Compressed Output:", compressed)
# 6. Calculate compression ratio
original_length = len(text)
compressed_length = len(compressed)
compression_ratio = (compressed_length / original_length) * 100
print("Original Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", round(compression_ratio, 2), "%")
