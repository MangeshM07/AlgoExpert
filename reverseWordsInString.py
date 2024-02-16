def reverseWordsInString(string):
    output = []

    left = right = len(string)-1

    while left >= 0 and right >= 0:
        if string[left] != ' ':
            left = left - 1
        else:
            output.append(string[left + 1:right + 1])
            left = right = left - 1
    output.append(string[left+1:right+1])
    return " ".join(output)


input = "Algoexpert  is the best!!"

print(reverseWordsInString(input))