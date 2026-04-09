import string
def num_words(book_text):
    words = book_text.split()
    return len(words)

def count_character(book_text):
    character_counts = {}

    for char in book_text:
        char = char.lower()

        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    
    return character_counts

def sort_on(items):
    return items["num"]


def sort_characters(character_counts):
    sorted_list = []

    for char, count in character_counts.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def clean_text(text):
    # Remove punctuation
    return text.translate(str.maketrans("", "", string.punctuation))


def get_word_frequency(book_text):
    cleaned_text = clean_text(book_text.lower())
    words = cleaned_text.split()

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


def sort_words(word_counts):
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
