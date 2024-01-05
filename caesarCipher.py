def ceasarCipher(string, key):
    newString = ""
    for i in range(len(string)):
        nlc = ord(string[i]) + key
        if nlc > 122:
            newString+=chr(96+(nlc%122))
        else:
            newString+=chr(nlc)
    return newString

print(ceasarCipher('xyz',2))