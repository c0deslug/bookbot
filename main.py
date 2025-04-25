from stats import wordcount
from stats import allchars
from stats import numchars
from stats import sortchars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    booktext = get_book_text(sys.argv[1])
    #print (booktext)
    num_words = wordcount(booktext) # gets wordcount
 
    unique_chars = allchars(booktext) # gets all the unique characters

    char_count = numchars(booktext, unique_chars) # counts the occurence of all unique characters
    sorted_characters = sortchars(char_count)

    #print (char_count)
    print(f'''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------''') 
    for character in sorted_characters:
        #temp_char = character["char"]
        #temp_num = character["num"]
        if character["char"].isalpha():
           print(f'{character["char"]}: {character["num"]}') # use single quotes otherwise you'll get f-string: unmatched
    print("============= END ===============")

main()

