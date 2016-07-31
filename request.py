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
print(new_index)
tf = index.tf
titels=index.titless
def search():
    x = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSuche Wort \n")
    x = filter(x)

    result_list = set()


    for i in x:

        if i not in new_index:
            x.remove(i)

        else:
            for doc_id in new_index[i]["list"]:
                result_list.add(doc_id)


    skalar = []
    for doc_id in result_list:
        ska=0
        leng=0
        prelen=0
        qqlen=0
        skalars=0
        for word in x:
            if new_index[word].get("idf",0):
                qqlen += new_index[word]["idf"] ** 2
                if new_index[word]["list"].get(doc_id,0):
                    ska += new_index[word]["list"][doc_id] * new_index[word]["idf"]**2 /tf[doc_id][0]*new_index[word]["list"][doc_id]
                    prelen+=(new_index[word]["list"][doc_id] * new_index[word]["idf"]/tf[doc_id][0]*new_index[word]["list"][doc_id])**2


            else:
                continue

        skalars=(ska/(prelen*qqlen)**0.5)
        skalar.append(skalars)
    dicte = {}
    if len(result_list) !=0:
        qqqlen=qqlen
        rating=skalar


        for inte in range(len(rating)):
             dicte[list(result_list)[inte]]= rating[inte]
        sort= sorted(dicte, key=dicte.get,reverse=True)
        integ=1
        sortedkeys=sorted(rating)
        for intege,item in enumerate(sort):
            print ("Position"+ str(integ))
            integ+=1
            print ("Doc id : "+str(item))
            print ("Title : "+ str(titels[item -1]))
            print ("Angle : "+str(math.acos(rating[intege])/math.pi*180)+"°")


search()



