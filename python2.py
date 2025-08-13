text="world is beautiful"
def print_longest_text(text):
    words= text.split()
    longest_word = max(words, key=len)
    return longest_word

print(print_longest_text(text))


def replace_with_stars(text):
    words = text.split()
    result = []
    for word in words:
        if len(word) > 2:
            new_word = word[0] + '*' * (len(word) - 2) + word[-1]
        else:
            new_word = word  # leave short words unchanged
        result.append(new_word)
    return ' '.join(result)

# Example usage
text = "python is powerful"
print(replace_with_stars(text))

def reverse_words(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words[::-1]]
    return ' '.join(reversed_words)

print(reverse_words(text))

def is_isogram(text):
    unique_chars = set(text)
    return len(unique_chars)

word="letter"
if is_isogram(word)==len(word):
    print(True)
else:
    print(False)

