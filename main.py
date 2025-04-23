
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def wordcount(booktext):
    words = [] # array
    words = booktext.split() #splits the word https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.split
    wordcount = len(words)
    return wordcount
    

def main():
    booktext = get_book_text("/Users/srados/workspace/github.com/c0deslug/bookbot/books/frankenstein.txt")
    #print (booktext)
    num_words = wordcount(booktext)
    print (f"{num_words} words found in the document")

main()

