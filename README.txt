Name: Karan Venkatesh Davanam
UIN: 673740735
ID : kdavan2
Web Search Engine Term Project
CS 582 Information Retrieval
Spring 2020
-------------------------------------------------------------------------------------------------------------------------------------------------
The libraries that needs to be installed
Prerequisites before running the code: Since this is python 3 based code make sure you have Ananconda(Python 3) installed.
NLTK package should be installed since I'm using some NLTK built in functions in the preprocessing stage:
You might encounter some error regarding sqlite3 for nltk: I have placed the necessary DLL files(Windows x64 machine) for sqlite3 in the folder:
Place the DLL files in inside the sqlite-dll-win64-x64-3310000(folder) to  Anaconda\DLLs directory(If necessary)
Since I'm using word_tokenize and string.punctuation for tokenizing the words based on space we need the following package to be installed:
Open your python prompt and do the following steps:
>>> import nltk
>>> nltk.download('punkt')
pip install networkx
Beautiful soup 
requests
nltk
sys
re
nltk
urllib
bs4
pickle
numpy
Counter from collections
operator
tkinter

-------------------------------------------------------------------------------------------------------------------------------------------------------
Steps in running the crawler:
Delete the folder htmlcontent before you run the crawler 
Warning running crawling from staring might take a lot time and make sure the htmlcontent(important!!!!!) folder is deleted from the location where crawler_web.py exists.
If you want to crawl the webpages from starting you need to run:(you find these files inside the kdavan2_Final_web_search_engine\Crawler)
python crawler_web.py    (if you run this step it will take 4 hours to complete the whole programs
after the crawler is successfully completed you can run.
python Ui.py
---------------------------------------------------------------------------------------------------------------------------------------------------------
Make sure the all the pickle files exists before running the below step
adj_link_list,dict, dict_query, dict1, dict2 , file_link , network,page_rank , query_vector, sorted_doc_list and total_documents
Steps in running the project directly by skipping the crawler phase:
Run the below command:
python Ui.py

Follow the instructions given in the command line

While using the GUI kindly click on search button for a given query after the results appear then only click on Query Expansion button.

query that can be used for- 'accc'