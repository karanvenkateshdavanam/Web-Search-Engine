#Name: Karan Venkatesh Davanam
#UIN: 673740735
#ID : kdavan2
#Term Project
#CS 582 Information Retrieval
#Spring 2020
from get_all_tokens import get_tokens,remove_punct,get_stopwords,get_stemwords
import re
import os
from bs4 import BeautifulSoup
import string
import math
import numpy as np
import operator
from collections import Counter
import pickle

#Using BeautifulSoup the title and text is extracted from the documents
def extract_title_text(contents):
    soup = BeautifulSoup(contents,'html.parser')
    title = str(soup.find("title"))
    text = str(soup.find("text"))
    extract = title +" "+text
    clean = re.compile('<.*?>')
    clean_content= re.sub(clean, '', extract)
    return clean_content

#contains all the functions required to prepocess the documents
def content_preprocess(title_text):
    clean_punc = remove_punct(title_text)
    translator = str.maketrans('', '', string.digits)
    clean_digit=clean_punc.translate(translator)
    clean_text = clean_digit.lower()
    return clean_text


#two dictionaries are created here one contains document frequency and the other frequency of term in each document
def inverted_index(path,entries):
    dict={}
    dict1 = {}
    i = 0
    for entry in entries:
        f = open(path+'\\'+entry,"r")
        if f.mode == "r":
            contents = f.read()
        #title_text = extract_title_text(contents)
        clean_text = content_preprocess(contents)
        token_text = get_tokens(clean_text)
        stop_words1 = get_stopwords()
        #i = i + 1
        #X = i
        X = entry
        for tokens in token_text:
            if tokens not in stop_words1 and len(tokens) > 2:
                token_stem = get_stemwords(tokens)
                if token_stem not in stop_words1 and len(token_stem) > 2:
                    if token_stem in dict1:
                        if X in dict1.get(token_stem):
                            dict1[token_stem][X] +=1
                        else:
                            dict1[token_stem][X] =1
                    else:
                       dict1[token_stem] = {}
                       dict1[token_stem][X] = 1

    for key,val in dict1.items():
        dict[key] = len(val)

    pickle_dict = open("dict.pickle","wb")
    pickle.dump(dict, pickle_dict)
    pickle_dict.close()

    pickle_dict1 = open("dict1.pickle","wb")
    pickle.dump(dict1, pickle_dict1)
    pickle_dict1.close()


    return dict,dict1

#The document length is calulated for each document
def document_length(dict, dict1,total_documents):
    dict2 = {}
    for k, doc1 in dict1.items():
        for doc in doc1:
            if doc in dict2:
                dict2[doc] = dict2[doc] + ((dict1[k][doc] * (math.log((total_documents/dict[k]),2)))**2)
            else:
                dict2[doc] = (dict1[k][doc] * (math.log((total_documents/dict[k]),2)))**2
    dict2.update({n: math.sqrt(dict2[n]) for n in dict2.keys()})

    pickle_dict2 = open("dict2.pickle","wb")
    pickle.dump(dict2, pickle_dict2)
    pickle_dict2.close()


#A dictionary is created here containing the cosine similarity between queries and documents
def query_processing(query,sim_measure):

    query_list = [query]

    pickle_in_dict = open("dict.pickle","rb")
    dict = pickle.load(pickle_in_dict)

    pickle_in_dict1 = open("dict1.pickle","rb")
    dict1 = pickle.load(pickle_in_dict1)

    pickle_in_dict2 = open("dict2.pickle","rb")
    dict2 = pickle.load(pickle_in_dict2)

    pickle_in_total_documents = open("total_documents.pickle","rb")
    total_documents = pickle.load(pickle_in_total_documents)

    dict_query={}
    stop_words1 = get_stopwords()
    #query_file = open(query_path,"r")
    number = 0
    query_vector={}
    for query in query_list:
        number = number + 1
        q_text = content_preprocess(query)
        q_tokens = get_tokens(q_text)
        for q_token in q_tokens:
            if q_token not in stop_words1 and len(q_token) > 2:
                q_token_stem = get_stemwords(q_token)
                if q_token_stem not in stop_words1 and len(q_token_stem) > 2 and q_token_stem in dict1.keys():
                    if q_token_stem in query_vector:
                        query_vector[q_token_stem] += 1
                    else:
                        query_vector[q_token_stem] = 1

                    docs = dict1.get(q_token_stem)
                    df = dict.get(q_token_stem)
                    for doc,tf in docs.items():
                        if number in dict_query:
                            if doc in dict_query.get(number):
                                dict_query[number][doc] += (dict1[q_token_stem][doc] * (math.log((total_documents/df),2)))*(math.log((total_documents/df),2))
                            else:
                                dict_query[number][doc] = (dict1[q_token_stem][doc] * (math.log((total_documents/df),2)))*(math.log((total_documents/df),2))
                        else:
                            dict_query[number] = {}
                            dict_query[number][doc] = (dict1[q_token_stem][doc] * (math.log((total_documents/df),2)))*(math.log((total_documents/df),2))

    for key,values in dict_query.items():
        for doc,value in values.items():
            if sim_measure == 'CosSim':
                dict_query[key][doc] = dict_query[key][doc] / dict2[doc]
            elif sim_measure == 'InnerProd':
                dict_query[key][doc] = dict_query[key][doc]
            elif sim_measure == 'DiceCof':
                dict_query[key][doc] = (2*dict_query[key][doc]) / (dict2[doc]**2)

    pickle_query = open("dict_query.pickle","wb")
    pickle.dump(dict_query, pickle_query)
    pickle_query.close()

    pickle_query_vector = open("query_vector.pickle","wb")
    pickle.dump(query_vector, pickle_query_vector)
    pickle_query_vector.close()




def vector_calculation_call():
    val = "htmlcontent"
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = dir_path +"\\"+str(val)
    entries = os.listdir(path)
    dict, dict1 = inverted_index(path,entries)
    total_documents = len(entries)
    pickle_documents = open("total_documents.pickle","wb")
    pickle.dump(total_documents, pickle_documents)
    pickle_documents.close()
    dict2 = document_length(dict, dict1,total_documents)


if __name__ == '__main__':
    main()
