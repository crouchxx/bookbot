def word_counter(file_contents):
    counter = 0
    words = file_contents.split()
    for word in words:
        counter += 1
    print(f"Found {counter} total words")
        
def character_counter(file_contents):
    lowercase_text = file_contents.lower()
    character_dictionary = {}
    for character in lowercase_text:
        if character not in character_dictionary:
            character_dictionary[character] = 1
        elif character in character_dictionary:
            character_dictionary[character] += 1
    return character_dictionary

def sort_on(item):
    return item["num"]

def dictionary_sort(character_dictionary):
    dictionary_list = []
    for ch, count in character_dictionary.items():
        dictionary_list.append({"char" : ch, "num" : count})
    dictionary_list.sort(reverse = True, key = sort_on)
    return dictionary_list