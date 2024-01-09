# O(c * (n+m)) time | O(c) space
def generateDocument(characters, document):
    alreadyCounted = set()

    for character in document:
        if character in alreadyCounted:
            continue

        documentFrequency = countCharacterFrequency(character, document)
        charactersFrequency = countCharacterFrequency(character, characters)
        if documentFrequency > charactersFrequency:
            return False

        alreadyCounted.add(character)
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