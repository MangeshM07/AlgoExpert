# Time O(n) | Space O(1)
def palindrome(str):
    low = 0
    high = len(str) - 1

    while low < high:
        if str[low].lower() != str[high].lower():
            return "not a palidrome"
        else:
            low += 1
            high -= 1
    return "Is a palindrome"


# Time O(n*2) | Space O(n)
def isPalindrome_solution1(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString


# Time O(n) | Space O(n)
def isPalindrome_solution2(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)


# Recursive solution
# Time O(n) | Space O(n)
def isPalindrome_solution3(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome_solution3(string, i + 1)


# Tail recursion
# Time O(n) | Space O(1)
def isPalindrome_solution4(string, i=0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome_solution4(string, i + 1)


print(isPalindrome_solution3("malayalam"))
