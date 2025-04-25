import sys
from stats import *

def get_book_text_from(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text_from(book_path)
    num_words = count_words(book_text)
    sorted = sort_chars(count_chars(book_text))

    # print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()