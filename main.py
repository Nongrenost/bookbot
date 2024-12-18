def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = get_word_count(text)
    letter_count = count_letters(text)
    letters_sorted_only_alpha = get_only_alpha_list_sorted(letter_count)
    output(word_count, letters_sorted_only_alpha, book_path)


def get_text(path):
    with open(path) as f:
        return f.read()

def output(word_count, letters, path):
    print(f"--- Begin report of {path} ---")
    print(f"Word count: {word_count}\n")
    
    for record in letters:
        print(f"Character {record["name"]} was found {record["value"]} times")
    print("--- End report ---")

def get_word_count(text):
    _word_count = len(text.split())
    return _word_count

def count_letters(text):
    counted_letters = {}   
    for char in text:
        lowered_char = char.lower()
        if lowered_char in counted_letters:
            counted_letters[lowered_char] += 1
        else:
            counted_letters[lowered_char] = 1
    return counted_letters



def sort_on(dict):
    return dict["value"]

def get_only_alpha_list_sorted(dict):
    only_alpha_list = []
    for record in dict:
        if record[0].isalpha():
            new_record = {"name":record, "value":dict[record]}
            only_alpha_list.append(new_record)
    only_alpha_list.sort(reverse=True, key=sort_on) 
    return only_alpha_list 

main()
