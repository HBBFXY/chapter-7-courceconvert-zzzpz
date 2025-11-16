import keyword

with open('random_int.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

processed_lines = []
for line in lines:
    words = line.split()
    new_words = []
    for word in words:
        if keyword.iskeyword(word):
            new_words.append(word)
        else:
            new_words.append(word.upper())
    processed_line = ' '.join(new_words) + '\n'
    processed_lines.append(processed_line)

with open('random_int_converted.py', 'w', encoding='utf-8') as f:
    f.writelines(processed_lines)
