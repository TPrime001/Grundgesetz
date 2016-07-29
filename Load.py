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
    for doc in docs:
        stemmend.append(process(doc))
    preindeex=defaultdict(dict)
    for id,doc in enumerate (stemmend):

        for wort in doc:
            if len(preindeex[wort]["list"])==0:

                preindeex[wort]["list"]=[id+1]
            else:
                preindeex[wort]["list"].append(id+1)
    for key in preindeex :
        integer=0
        for doc in preindeex[key]["list"]:
            integer+=1
        preindeex[key]["ntd"]= integer
        preindeex[key]["idf"] = math.log(integer/N,10)
    for key in preindeex:
        new_dict=defaultdict(int)
        for docid in preindeex[key]["list"]:

                new_dict[docid]+=1
        preindeex[key]["list"]= new_dict


class saved (object):
    def __init__(self,index,tf):
        self.index= index
        self.tf

loadAndStem("enmarveldatabase_pages_current.json.gz")