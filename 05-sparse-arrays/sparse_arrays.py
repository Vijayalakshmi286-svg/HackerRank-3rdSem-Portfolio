# HackerRank: Sparse Arrays
# Language: Python

def matchingStrings(stringList, queries):
    freq = {}

    for s in stringList:
        freq[s] = freq.get(s, 0) + 1

    result = []

    for q in queries:
        result.append(freq.get(q, 0))

    return result
