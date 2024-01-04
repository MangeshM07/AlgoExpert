def palindrome(str):
    low = 0
    high = len(str)-1


    while low < high:
        if str[low].lower() != str[high].lower():
            return "not a palidrome"
        else:
            low += 1
            high -= 1
    return "Is a palindrome"

print(palindrome("Malayalam"))