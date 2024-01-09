# O(m * (n+m)) time | O(1) space
def generateDocument(characters, document):
    for character in document:
        documentFrequency = countCharacterFrequency(character, document)
        charactersFrequency = countCharacterFrequency(character, characters)
        if documentFrequency > charactersFrequency:
            return False

    return True


def countCharacterFrequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1

    return frequency



characters = "eripxe uoy erofeb eripsnI"
document = "Inspire before you expire"
print(generateDocument(characters, document))