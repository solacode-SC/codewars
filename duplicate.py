def duplicate_encode(word):
    encoded = ""
    for char in word:
        if word.lower().count(char.lower()) > 1:
            encoded += ")"
        else:
            encoded += "("
    return encoded