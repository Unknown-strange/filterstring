def filterString(word, charToRemove):
    result = ''
    for char in word: 
        if char != charToRemove: # We only care about characters that are not to be filtered out
            result += char
    return result

print(filterString("HelloWorld", "l"))