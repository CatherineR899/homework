# my tries
def palindrome1(text):
    reverse = ""
    for i in range(len(text)-1, -1, -1):
        reverse += text[i]
    if reverse == text:
        return True
    return False

def palindrome2(text):
    i = 0
    j = len(text) - 1
    while i < len(text) and j > -1:
        if text[i] != text[j]:
            return False
            break
        else:
            i += 1
            j -= 1
    return True

# Mr Park's
def is_palindrome1(text):
    return text == text[::-1]

def is_palindrome2(text):
    if not text:
        return True 
    elif len(text) < 4:
        return text[0] == text[-1]
    else:
        midpoint = len(text) // 2
        for i in range(0, midpoint):
            left = text[i]
            right = text[(-1*i) - 1]
            if left != right:
                return False
        return True 