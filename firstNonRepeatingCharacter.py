def firstNonRepeatingCharacter(string):
    seen_chars = set()

    for index, char in enumerate(string):
        if char not in seen_chars:
            if char not in string[index+1:]:
                return index
        seen_chars.add(char)

    return -1

string = "abcdcaf"
print(firstNonRepeatingCharacter(string))