def ceasarCipherEncryptor_solution1(string, key):
    newString = ""
    for i in range(len(string)):
        nlc = ord(string[i]) + key
        if nlc > 122:
            newString += chr(96 + (nlc % 122))
        else:
            newString += chr(nlc)
    return newString


def ceasarCipherEncryptor_solution2(string, key):
    newLetters = []
    newKey = key % 26

    for letter in string:
        newLetters.append(getNewLetter_solution2(letter, newKey))
    return "".join(newLetters)


def getNewLetter_solution2(Letter, key):
    newLetterCode = ord(Letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


def ceasarCipherEncryptor_solution3(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter_solution3(letter, newKey, alphabet))
    return "".join(newLetters)


def getNewLetter_solution3(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode] if newLetterCode < 25 else alphabet[newLetterCode % 26]


print(ceasarCipherEncryptor_solution3('xyz', 2))
