import pickle
from collections import Counter
import operator

#provide the Links
def print_links(page_no):
    index = page_no * 10
    pickle_in = open("file_link.pickle","rb")
    link_dict = pickle.load(pickle_in)

    pickle_page_in = open("page_rank.pickle","rb")
    page_dict = pickle.load(pickle_page_in)

    pickle_query_in = pickle_page_in = open("dict_query.pickle","rb")
    dict_query = pickle.load(pickle_query_in)

    print_list = {}
    document_id_list = {}
    for key,values in dict_query.items():
        for file,value in values.items():
            value1 = page_dict[link_dict[file]]
            print_list[link_dict[file]] = (0.65*value) + (0.35*value1)
            document_id_list[file] = (0.65*value) + (0.35*value1)


    sorted_dict = dict( sorted(print_list.items(), key=operator.itemgetter(1),reverse=True))
    sorted_doc_dict = dict( sorted(document_id_list.items(), key=operator.itemgetter(1),reverse=True))
    sorted_list = list(sorted_dict)
    pickle_dict_in = open("sorted_doc_list.pickle","wb")
    pickle.dump(sorted_doc_dict, pickle_dict_in)
    pickle_dict_in.close()

    return sorted_list[index:index+10]

def print_cmd_links():
    index = 10
    pickle_in = open("file_link.pickle","rb")
    link_dict = pickle.load(pickle_in)

    pickle_page_in = open("page_rank.pickle","rb")
    page_dict = pickle.load(pickle_page_in)

    pickle_query_in = pickle_page_in = open("dict_query.pickle","rb")
    dict_query = pickle.load(pickle_query_in)

    print_list = {}
    for key,values in dict_query.items():
        for file,value in values.items():
            value1 = page_dict[link_dict[file]]
            #print(str(link_dict[file])+"  "+str(value)+"  "+str(page_dict[link_dict[file]])+" "+ str((2*value1*value)/(value1+value)))
            #print_list[link_dict[file]] = str((2*value1*value)/(value1+value))
            print_list[link_dict[file]] = value


    sorted_dict = dict( sorted(print_list.items(), key=operator.itemgetter(1),reverse=True))
    #print(sorted_dict)
    sorted_list = list(sorted_dict)

    return sorted_list[0:10]

def print_cmd_page_links():
    index = 10
    pickle_in = open("file_link.pickle","rb")
    link_dict = pickle.load(pickle_in)

    pickle_page_in = open("page_rank.pickle","rb")
    page_dict = pickle.load(pickle_page_in)

    pickle_query_in = pickle_page_in = open("dict_query.pickle","rb")
    dict_query = pickle.load(pickle_query_in)

    print_list = {}
    for key,values in dict_query.items():
        for file,value in values.items():
            value1 = page_dict[link_dict[file]]
            #print(str(link_dict[file])+"  "+str(value)+"  "+str(page_dict[link_dict[file]])+" "+ str((2*value1*value)/(value1+value)))
            #print_list[link_dict[file]] = str((2*value1*value)/(value1+value))
            print_list[link_dict[file]] = value1


    sorted_dict = dict( sorted(print_list.items(), key=operator.itemgetter(1),reverse=True))
    #print(sorted_dict)
    sorted_list = list(sorted_dict)

    return sorted_list[0:10]
