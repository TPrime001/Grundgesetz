from load_dataset import load_wikidata as load
from load_dataset import clean_wikidata as clean
from prepreprocess import token as process
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
            if preindeex[wort].get("list",1):

                preindeex[wort]["list"]=[id+1]
            else:
                preindeex[wort]["list"].append(id+1)
    print ("50%")
    for key in preindeex :
        integer=0
        for doc in preindeex[key]["list"]:
            integer+=1
        preindeex[key]["ntd"]= [integer]
        preindeex[key]["idf"] = [math.log(N/integer,10)]
    print ("60%")
    for key in preindeex:
        new_dict=defaultdict(int)
        for docid in preindeex[key]["list"]:

                new_dict[docid]+=1
        preindeex[key]["list"]= new_dict
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

        pickle.dump(saved(preindeex,tfmax),file)
    print ("100%")
    print (preindeex)

class saved (object):
    def __init__(self,index,tf):
        self.index= index
        self.tf=tf

loadAndStem("enmarveldatabase_pages_current.json.gz")