def to_camel_case(text):
    newText = ""
    for i in range(len(text)):
        if text[i] == "-":
            newText += text[i+1].upper()
        else:
            newText += text[i]
    return newText