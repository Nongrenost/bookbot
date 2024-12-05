def main():
    book_path = "books/frankenstein.txt"
    text_output(book_path)
    

def get_text(path):
    with open(path) as f:
        return f.read()

def text_output(path):
    print(get_text(path))

def word_count(text):


main()  