from stats import word_counter
from stats import character_counter
from stats import dictionary_sort

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    counted_character = character_counter(book_text)
    sorted_dictionary = dictionary_sort(counted_character)

    # print(counted_character)
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