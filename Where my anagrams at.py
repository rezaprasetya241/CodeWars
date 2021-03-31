def anagrams(word, words):
    sortedWord = sorted(word)
    list = []
    for i in words:
        x = sorted(i)
        if x == sortedWord:
            list.append(i)
    return list 
'''def anagrams(word, words):
    return [w for w in words if is_match == sorted(w)]'''




print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])) # ['aabb', 'bbaa']