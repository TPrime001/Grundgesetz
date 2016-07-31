import nltk
import nltk.stem.snowball as snow
from nltk.corpus import stopwords
import re

#tokenize creates list of words
def tokenize (text):
        print(text+"\n")
        new_text = nltk.word_tokenize(text)
        new_text1=[]
        for item in new_text:
            new_text1+=( re.findall('[\w]+', item))
        print("Tokenized:\n"+ str(new_text1)+"\n")
        return new_text1


#stemming
def stemming (new_text2):
        stemmer = snow.EnglishStemmer()
        new_list=[]
        for elements in new_text2:

            new_list.append(stemmer.stem(elements))
        print("Stemmed:\n" + str(new_list)+"\n")
        return new_list


#stopword removal
def stoppwords(new_list2):
        stop = stopwords.words('english')
        new_words = [word for word in new_list2 if word not in stop]
        print("Without Stopword:\n" + str(new_words)+"\n")
        return new_words

def preprocesss(data):
    tokens= tokenize(data)
    stemmed= stemming(tokens)

    finaltokens = stoppwords(stemmed)
    return finaltokens
preprocesss("Information retrieval is the activity of obtaining information resources relevant to an information need from a collection of information resources. Searches can be based on or on full-text (or other content-based) indexing. Automated information retrieval systems are used to reduce what has been called information overload. Many universities and public libraries use IR systems to provide access to books, journals and other documents. Web search engines are the most visible IR applications.")