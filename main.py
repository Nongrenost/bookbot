def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = get_word_count(text)
    letter_count = count_letters(text)
    output(word_count, letter_count)

def get_text(path):
    with open(path) as f:
        return f.read()

def output(word_count, letter_count):
    print(f"Word count: {word_count}")
    print(letter_count)

# remove if?
def get_word_count(text):
    if text is None:
        return None
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

main()
