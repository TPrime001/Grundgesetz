import nltk.stem.snowball as snow
import nltk



def token (text):
    new_text = nltk.word_tokenize(text)

    stemmer = snow.EnglishStemmer()
    new_list=[]
    for elements in new_text:

        new_list.append(stemmer.stem(elements))

    return new_list

