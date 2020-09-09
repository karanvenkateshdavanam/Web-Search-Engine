#Name: Karan Venkatesh Davanam
#UIN: 673740735
#ID : kdavan2
#Final Term Project
#CS 582 Information Retrieval
#Spring 2020
import os
import string
from nltk.tokenize import word_tokenize
from collections import Counter
import operator
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

#This function is used to remove punctuations as part of prepocessing the collection
def remove_punct(contents):
    translator = str.maketrans('', '', string.punctuation)
    clean_text=contents.translate(translator)
    return clean_text

#nltk work_tokenize is used to tokenize each documnets in collection based on space
def get_tokens(clean_text):
    tokens = word_tokenize(clean_text)
    return tokens

#get_stopwords function returns a a list of stopwords.
#stopwords.txt file is used as the stopword corpus
def get_stopwords():
    #dir_path_stopwords = os.path.dirname(os.path.realpath(__file__))
    #path_stopwords = dir_path_stopwords +"\\"+"stopwords.txt"
    #stop_words = open(path_stopwords,'r').read().split('\n')
    stop_words = set(stopwords.words('english'))
    return stop_words

#This function uses PorterStemmer to perform stemming on each token and returns the stemmed token.
def get_stemwords(token_val):
    ps = PorterStemmer()
    token_stem = ps.stem(token_val)
    return token_stem
