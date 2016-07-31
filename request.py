from Load import loadAndStem as load
from prepreprocess import preprocesss as filter
import pickle
import math
from Load import saved
try:
    with open("indexing.pickel","rb") as file:
        index=pickle.load(file)
except:
    load("enmarveldatabase_pages_current.json.gz")

new_index = index.index
tf = index.tf
def search():
    x = input("Suche Wort \n")
    x = filter(x)

    result_list = set()
    for i in x:
        if len(new_index[i])== 0:
            x.remove(i)
        else:
            for doc_id in new_index[i]["list"]:
                result_list.add(doc_id)
    skalar = []
    for doc_id in result_list:
        ska=0
        for word in x:
            if new_index[word]["list"].get(doc_id,0):
                ska += new_index[word]["list"][doc_id] * new_index[word]["idf"] /tf[doc_id][0]*new_index[word]["list"][doc_id]

            else:
                continue
        skalar.append(ska)
    print(skalar)
    print(result_list)
search()



