#x = "and i left yesterday"
#print (x.split(" "))
#numberofwords = len(x)
#print (numberofwords)


# from nltk import*
import re
import nltk.stem.snowball as snow

from collections import defaultdict
import pickle as pi
def Index(data):
    integer = 0
    indexdict = defaultdict(set)
    for wort in data:
        if re.search("xxx", wort):
            integer += 1
        else:
            indexdict[wort].add(integer)
    return indexdict

def indexing(path):
    boundry = 160

    file = open(path,"r+",encoding="UTF-8")
    satz= file.read()
    satz=re.split("Artikel [0-9]+\n",satz)
    satznew=[]
    for itt in satz:
        satznew.append(itt)
        satznew.append("xxx")
    satz=satznew
    satz=" ".join(satz)




    satz = re.findall('[\w-]+', satz)


    im = 1

    print(satz)



    stemmer = snow.GermanStemmer()
    satz = [ stemmer.stem(x) for x in satz]


    print(satz)
    counter = {}

    for token in satz:
        if token in counter:
            counter[token] = counter[token] + 1
        else:
            counter[token] = 1
    for w in sorted(counter, key=counter.get, reverse=True):
        print (w, counter[w])

    clearlist = []
    for k,v in counter.items():
        if v > boundry:
            clearlist.append(k)

    satz = [x for x in satz if x not in clearlist]
    print (satz)


    print(counter)
    with open("index.pickel","wb") as file:

        pi.dump (Index(satz),file)

    return (Index(satz))




