# Time O(n^2) | space O(n)
def firstNonRepeatingCharacter(string):
    seen_chars = set()

    for index, char in enumerate(string):
        if char not in seen_chars:
            if char not in string[index + 1:]:
                return index
        seen_chars.add(char)

    return -1


def firstNonRepeatingCharacter_solution2(string):
    for idx in range(len(string)):
        foundDuplicate = False
        for idx2 in range(len(string)):
            if string[idx] == string[idx2] and idx != idx2:
                foundDuplicate = True

        if not foundDuplicate:
            return idx

    return -1


# O(n) time | O(1) space
def firstNonRepeatingCharacter_solution3(string):
    characterFrequencies = {}

    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1

    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx

    return -1


string = "abcdcaf"
print(firstNonRepeatingCharacter_solution3(string))
