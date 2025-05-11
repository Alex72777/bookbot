from stats import *
import sys

def main(file_path: str):
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(file_path, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def get_book_text(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as book:
        content = book.read()
        return content

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])