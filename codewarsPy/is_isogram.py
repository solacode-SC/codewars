def is_isogram(string):
    #your code here
    if (string == ""):
        return True
    result = False
    for char in string:
        if(string.lower().count(char.lower()) <= 1):
            result = True
        else:
            result = False
            break
    return result