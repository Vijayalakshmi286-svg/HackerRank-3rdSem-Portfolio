# HackerRank: Dynamic Array
# Language: Python

def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    result = []

    for query in queries:
        query_type, x, y = query
        idx = (x ^ lastAnswer) % n

        if query_type == 1:
            seqList[idx].append(y)

        elif query_type == 2:
            lastAnswer = seqList[idx][y % len(seqList[idx])]
            result.append(lastAnswer)

    return result
