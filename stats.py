
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = [{"char": k, "count": v} for k, v in char_count.items()]
    return result

