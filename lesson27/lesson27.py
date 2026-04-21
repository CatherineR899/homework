# my try 
def only_letters(word):
    letters = ""
    for character in word:
        if character.lower() in "abcdefghijklmnopqrstuvwxyz":
            letters += character
    return letters

# Mr. Park's 
def string_cleaner(text):
    result = ""
    for character in text:
        if character.isalpha():
            result += character
    return result