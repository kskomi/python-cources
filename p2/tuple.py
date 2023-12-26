print(dir(tuple))
help(tuple.index)
help(tuple.count)
seq = (2,8,23,97,92,44,17,39,11,12)
print(seq.count(8))
print(seq.index(44))

listseq = list(seq)
print(type(listseq))

listseq.append(666)
listseq.insert(3, 111)
listseq.remove(23)
listseq.pop()

print(listseq)
