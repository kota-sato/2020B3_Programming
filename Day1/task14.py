import numpy as np
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
        print("idf(" + str(term[i]) + ")="+ str(idf))


docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

idf(terms, docs)