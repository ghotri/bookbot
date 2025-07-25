import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book):
    with open(book) as f:
        return f.read()
    
def sort_on(items):
    return items["count"]

from stats import count_words
from stats import count_letters


def main():
    a= get_book_text(sys.argv[1])
    num_words = count_words(a)
    num_letters = count_letters(a)
    num_letters.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at '{sys.argv[1]}'...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in num_letters:
        print(f"{item['char']}: {item['count']}")

main()