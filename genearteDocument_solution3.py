# O(n+m) time | O(c) space
def generateDocument(characters, document):
    characterCounts = {}

    for character in characters:
        if character not in characterCounts:
            characterCounts[character] = 0

        characterCounts[character] += 1

    for character in document:
        if character not in characterCounts or characterCounts[character] == 0:
            return False

        characterCounts[character] -= 1

    return True


characters = "eripxe uoy erofeb eripsnI"
document = "Inspire before you expire"
print(generateDocument(characters, document))