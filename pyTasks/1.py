import numpy as np
import re
from scipy.spatial.distance import cdist


file = open("sentences.txt")


lines = [x.lower()[:-1] for x in file.readlines()]
sentences = [[str(y) for y in re.split('[^a-z]', x) if y != ""] for x in lines]
text = " ".join(lines)
words = list(set([str(x) for x in re.split('[^a-z]', text) if x != ""]))

n, d = len(sentences), len(words)

A = np.array([[sentences[y].count(words[x]) for x in range(d)] for y in range(n)])
print(A.shape)

res = []

for i in range(1, n):
    dist = cdist(A[0][np.newaxis, :], A[i][np.newaxis, :], metric='cosine')[0]
    res.append(dist[0])

print(res.index(min(res))+1)
res1 = res[:]
res1.pop(res.index(min(res)))
print(res.index(min(res1))+1)
