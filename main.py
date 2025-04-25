from stats import wordcount
from stats import allchars
from stats import numchars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    booktext = get_book_text("/Users/srados/workspace/github.com/c0deslug/bookbot/books/frankenstein.txt")
    #print (booktext)
    num_words = wordcount(booktext)
    print (f"{num_words} words found in the document")
    unique_chars = allchars(booktext)
    #print (unique_chars)
    char_count = numchars(booktext, unique_chars)
    print (char_count)

main()

