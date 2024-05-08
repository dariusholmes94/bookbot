def main():
    with open("books/frankenstein.txt") as f:
    # opens book directory
        file_contents = f.read()
    # reads the book
    print(file_contents)
    # prints the text to the console

main()