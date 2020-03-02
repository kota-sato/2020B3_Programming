import numpy as np
docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]
x = np.zeros((len(docs),len(terms)))

def idf(term, docs):

    N = len(docs)
    df = 0
    for i in range(0, len(term)):
        df = 0
        for j in range(0, len(docs)):
            n = docs[j].count(term[i])
            if n != 0:
                df += 1
        idf = np.log10(N/df) + 1
        for k in range(0, len(docs)):
            x[i, k] = idf



def tf(term, docs):
    n = 0
    for i in range (0, len(docs)):
        for j in range (0, len(term)):
           n = docs[i].count(term[j])
           n = n/len(docs[i])
           x[i, j] *= n

idf(terms, docs)
tf(terms, docs)

#print(x)