with open("dataset/data.txt", "r", encoding = 'shift-jis') as f:

    docs_list = []
    terms_list = []
    mylist = []
    mylist2 = []

    for line in f:
        new_str = ''
        for i in range(0, len(line)):
            if line[i:i + 1] == 'と':
                new_str += ' '
            else:
                new_str += line[i:i + 1]
        mylist.append(new_str.split())
        mylist2 += new_str.split()
#    print("docs:", end = '')
#    print(mylist)
 #   print("terms:",end = '')
#    print(list(set(mylist2)))

    import sys
    def task17(ter, doc):
        import nlp.task16
        import nlp.task15
        nlp.task15.idf(ter, doc)
        nlp.task15.tf(ter, doc)
    #    nlp.task16.

    task17(mylist, mylist2)
