import sys
from stats import get_word_count



def main():
    book_path = sys.argv[1]
    check_args()
    
    text = get_text(book_path)
    word_count = get_word_count(text)
    letter_count = count_letters(text)
    letters_sorted_only_alpha = get_only_alpha_list_sorted(letter_count)
    output(word_count, letters_sorted_only_alpha, book_path)

def check_args():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_text(path):
    with open(path) as f:
        return f.read()

def output(word_count, letters, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for record in letters:
        print(f"{record["name"]}: {record["value"]}")
    print("============= END ===============")

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
