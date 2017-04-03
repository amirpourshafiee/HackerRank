def ransom_note(magazine, ransom):

    d = {}
    for word in magazine:
        d.setdefault(word, 0)
        d[word] += 1

    for word in ransom:
        if word in d:
            d[word] -= 1
        else:
            return False

    return all([x >= 0 for x in d.values()])

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
