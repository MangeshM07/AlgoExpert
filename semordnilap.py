def semordnilap(words):
    wordsSet = set(words)
    semiordnilapPairs = []

    for word in words:
        reverse = word[::-1]
        if reverse in wordsSet and reverse != word:
            semiordnilapPairs.append([word, reverse])
            wordsSet.remove(word)
            wordsSet.remove(reverse)

    return semiordnilapPairs


words = ['diaper', 'abs', 'sba', 'test', 'repaid']
print(semordnilap(words))