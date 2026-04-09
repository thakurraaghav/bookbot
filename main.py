import sys
import json
from stats import (
    num_words,
    count_character,
    sort_characters,
    get_word_frequency,
    sort_words,
)


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book> [--top N] [--export]")
        sys.exit(1)

    book_path = sys.argv[1]
    top_n = None
    export = False

    # Parse optional arguments
    if "--top" in sys.argv:
        try:
            top_n = int(sys.argv[sys.argv.index("--top") + 1])
        except:
            print("Invalid value for --top")
            sys.exit(1)

    if "--export" in sys.argv:
        export = True

    book_text = get_book_text(book_path)

    word_count = num_words(book_text)
    character_counts = count_character(book_text)
    sorted_characters = sort_characters(character_counts)

    word_freq = get_word_frequency(book_text)
    sorted_words = sort_words(word_freq)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("\n----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("\n--------- Character Count -------")
    for item in sorted_characters:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("\n--------- Top Words -------")
    display_words = sorted_words[:top_n] if top_n else sorted_words[:10]

    for word, count in display_words:
        print(f"{word}: {count}")

    # Export to JSON
    if export:
        data = {
            "word_count": word_count,
            "top_words": display_words,
        }

        with open("report.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\n✅ Report exported to report.json")

    print("\n============= END ===============")


main()