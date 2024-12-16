def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = get_word_count(text)
    output(word_count)

def get_text(path):
    with open(path) as f:
        return f.read()

def output(word_count):
    print(f"Word count: {word_count}")

# remove if?
def get_word_count(text):
    if text is None:
        return None
    _word_count = len(text.split())
    return _word_count

main()
