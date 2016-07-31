import nltk
import nltk.stem.snowball as snow
from nltk.corpus import stopwords


#tokenize creates list of words
def tokenize (text):
       new_text = nltk.word_tokenize(text)
       return new_text


#stemming
def stemming (new_text):
        stemmer = snow.EnglishStemmer()
        new_list=[]
        for elements in new_text:
            new_list.append(stemmer.stem(elements))
        return new_list


#stopword removal
def stoppwords(new_list):
        stop = stopwords.words('english')
        new_words = [word for word in new_list if word not in stop]
        return new_words

def preprocesss(data):
    tokens= tokenize(data)
    stemmed= stemming(tokens)
    finaltokens = stoppwords(stemmed)
    return finaltokens

print(preprocesss("Information retrieval is the activity of obtaining information resources relevant to an information need from a collection of information resources. Searches can be based on or on full-text (or other content-based) indexing. Automated information retrieval systems are used to reduce what has been called information overload. Many universities and public libraries use IR systems to provide access to books, journals and other documents. Web search engines are the most visible IR applications."))