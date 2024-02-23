def filter_string(words, char):
    words = words.title()
    new_word = [word for word in words]
    if char in new_word: new_word.remove(char)
    print(''.join(new_word))

# code test :)
filter_string("Prince", "r")
