def count_words(text):
    return len(text.split())

def count_chars(text):
    counts = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in counts:
            counts[lower_char] = 1
        else:
            counts[lower_char] += 1
    return counts

def sort_chars(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({"char": char, "count": char_dict[char]})
    char_list.sort(key=lambda char: char["count"], reverse=True)
    return char_list