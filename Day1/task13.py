def tf(term, docs):
    n = 0
    for i in range (0, len(docs)):
        for j in range (0, len(term)):
           n = docs[i].count(term[j])
           print("tf("+ str(term[j])+ ", "+str(docs[i])+ ")="+ str(n/ len(docs[i])))

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

tf(terms, docs)