def word_count(book_contents):
    # This functions takes a string containing the book contents and returns a word count.
    words = book_contents.split()
    word_count = len(words)
    return word_count

def main():
    # This function reads the book contents and prints the book and word count.
    book_contents = "books/frankenstein.txt"
    with open(book_contents) as f:
        file_contents = f.read()
    
    print(file_contents)
    
    count = word_count(file_contents)

    print(f"Word count: {count}")

    
main()