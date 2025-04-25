def wordcount(booktext):
    words = [] # array
    words = booktext.split() #splits the word https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.split
    wordcount = len(words)
    return wordcount

def allchars(booktext):
    booktext = booktext.lower() # turns everything into lower case
    unique_chars = set()
    for char in booktext:
        unique_chars.add(char)
    unique_chars = sorted(unique_chars) # kind of alphabetizes them https://docs.python.org/3/library/functions.html#sorted
    return unique_chars
    
def numchars(booktext, unique_chars):
    char_table = {}
    booktext = booktext.lower()
    for char in unique_chars: # sets the initial value of each character to zero
        char_table[char] = 0
    for char in booktext: # go through each character in book text and if found in the dictionary increment value
        if char in char_table:
            char_table[char] += 1
    return char_table

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def sortchars(char_count):
    new_dict = {}
    list_of_dicts = []
    for char in char_count:
        new_dict = {
        "char": char,
        "num": char_count[char]
        }
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)        
    return list_of_dicts