from stats import word_counter
from stats import character_counter
from stats import dictionary_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    print("Usage: python3 main.py <path_to_book>")
    book_text = get_book_text(sys.argv[1])
    counted_character = character_counter(book_text)
    sorted_dictionary = dictionary_sort(counted_character)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_counter(book_text)
    print("--------- Character Count -------")
    for i in sorted_dictionary:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
main()