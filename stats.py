def wordcount(booktext):
    words = [] # array
    words = booktext.split() #splits the word https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.split
    wordcount = len(words)
    return wordcount

