from load_dataset import load_wikidata as load
from load_dataset import clean_wikidata as clean
from prepreprocess import preprocesss as process
import math
import pickle
from collections import defaultdict

def loadAndStem(path):
    data = load(path)
    docs=[]
    titels=[]
    for doc in data:
        docs.append(clean(doc["text"]))
        titels.append(doc["title"])
    stemmend=[]
    N= len(titels)
    loadlimit =N
    print ("5%")
    i=0
    for doc in docs:
        i+=1
        print("....")
        stemmend.append(process(doc))
        if i==loadlimit:
            break


    preindeex=defaultdict(dict)
    print("40%")
    for id,doc in enumerate (stemmend):
        print("....")
        for wort in doc:
            if "list" not in preindeex[wort]:

                preindeex[wort]["list"]=[id+1]
            else:
                preindeex[wort]["list"].append(id+1)

    print ("50%")
    for key in preindeex :

        m=len(preindeex[key]["list"])
        preindeex[key]["ntd"]= m
        preindeex[key]["idf"] = math.log(N/m,10)
    print ("60%")
    for keyss in preindeex:
        new_dict=defaultdict(int)
        for docid in preindeex[keyss]["list"]:

                new_dict[docid]+=1
        preindeex[keyss]["list"]= new_dict
    tfmax=defaultdict(list)
    for keys in preindeex:
        for doc_id in preindeex[keys]["list"]:
            if len(tfmax[doc_id])==0:
                tfmax[doc_id].append(preindeex[keys]["list"][doc_id])
                tfmax[doc_id].append(keys)
            elif  tfmax[doc_id][0] <preindeex[keys]["list"][doc_id]:
                tfmax[doc_id][0]=( preindeex[keys]["list"][doc_id])
                tfmax[doc_id][1]=( keys)
    print (tfmax)
    print ("90%")
    with open("indexing.pickel", "wb") as file:

        pickle.dump(saved(preindeex,tfmax,titels),file)

    print ("100%")
    print (preindeex)

class saved (object):
    def __init__(self,index,tf,titelss):
        self.index= index
        self.tf=tf
        self.titless=titelss

