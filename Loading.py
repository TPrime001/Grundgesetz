from Testjgw import indexing
from collections import defaultdict
import pickle

pathss=["Grundgesetz"]
index={}
try:
    with open("index.pickel","rb") as file:
        index=pickle.load(file)
except:
    for x in pathss:

        index=indexing(x)
        print (index)

sa = input ("Geben sie eie Suchanfrage ein\n ")
sa = sa.split(" ")          #stemming
words= len(sa)
resultlist=[]
import nltk.stem.snowball as snow


for wort in sa:
    stemmer = snow.GermanStemmer()
    wortt=stemmer.stem(wort)
    for inte in index[wortt]:
        if inte!=0:

            resultlist.append(inte)
dicte= defaultdict(int)
for integ in sorted(resultlist):
    dicte[integ]+=1
print(dicte)
liste=list(sorted(dicte, key=dicte.get,reverse=True))
print (liste)
if len(liste)>0:
    print("Best article ist... Art. "+str(liste[0]))