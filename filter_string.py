def filter_string(words, char):
    words = words.title()
    new_word = []
    for word in words:
        new_word.append(word)
        if char in new_word: 
            new_word.remove(char)
    print(''.join(new_word))
   
    
# code test :) 
filter_string("Hello", 'l')
