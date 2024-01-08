# O(n * m) time | O(m) space
def commonCharacters(strings):
    characterCounts = {}
    for string in strings:
        uniqueStringCharacters = set(string)
        for character in uniqueStringCharacters:
            if character not in characterCounts:
                characterCounts[character] = 0
            characterCounts[character] += 1

    finalCharacters = []
    for character, count in characterCounts.items():
        if count == len(strings):
            finalCharacters.append(character)

    return finalCharacters

strings = ["abc", "bcd", "cbbaadd"]
print(commonCharacters(strings))