#create a window
from tkinter import *
from tkinter.messagebox import *
from space_vector_model import vector_calculation_call,query_processing
from query_result import print_links,print_cmd_links,print_cmd_page_links
from rocchio_expansion import get_rocchio_words




print("\n Press '1' to start the GUI and check for Page Rank+Cosine Similarity and Rocchio query expansion and have option to check for more than 10 results \n Press '2' to start the Command Line UI where you check top 10 links with different similarity measures")
choice = input("Enter choice: ")

if choice == '1':
    page_no = 0
    def show_results():
        #you call the vector space model python
        global page_no
        page_no = 0
        query_processing(queryInput.get(),'CosSim')
        result_list = print_links(page_no)
        result = ""
        for val in result_list:
            result += val + "\n"

        LabelResult['text'] = result

    def show_results_next():
        #you call the vector space model python
        query_processing(queryInput.get(),'CosSim')
        result_list = print_links(page_no)
        result = ""
        for val in result_list:
            result += val + "\n"

        LabelResult['text'] = result

    def next_page():
        global page_no
        page_no = page_no + 1
        show_results_next()

    def previous_page():
        global page_no
        if page_no == 0:
            page_no = 0
        else:
            page_no = page_no - 1
        show_results_next()





    def createNewWindow():

        def get_rocchio():
            label["text"] = "please wait"
            rocchio_list = get_rocchio_words()
            result_rocchio = ""
            for val_rocchio in rocchio_list:
                result_rocchio += val_rocchio + "\n"
            result_rocchio += "Add any of the above suggested words to get relevant search results"
            label["text"] = result_rocchio

        newWindow = Toplevel(searchbox)
        label = Label(newWindow, text = "Please wait till the suggested words appear from Rocchio Query Expansion")
        button = Button(newWindow, text = "Click here-Stem Word Suggestion",command=get_rocchio)
        button1 = Button(newWindow, text='Quit', command=newWindow.destroy)

        label.grid(row=5, column=1, sticky=W, pady=4)
        label.pack()
        button.pack()
        button1.pack()


    searchbox = Tk()
    searchbox.title('Search Engine User Interface')
    Label(searchbox, text = "Enter Search Query:").grid(row=0)
    LabelResult = Label(searchbox)
    LabelResult.grid(row=5, columnspan=5, rowspan=10)


    queryInput = Entry(searchbox)


    queryInput.grid(row=0, column=1)

    Button(searchbox, text='Search', command=show_results).grid(row=15, column=0, sticky=W)
    Button(searchbox, text='Query Expansion', command=createNewWindow).grid(row=15, column=1)
    Button(searchbox, text='<<Page', command=previous_page).grid(row=15, column=2, sticky=W,pady=4)
    Button(searchbox, text='Page>>', command=next_page).grid(row=15, column=3)
    Button(searchbox, text='Quit', command=searchbox.destroy).grid(row=15, column=4, sticky=E)

    searchbox.mainloop()

elif choice == '2':
    query = input("Enter search query: ")
    print("Enter similarity measure choice \n Press 1:Cosine Similarity \n Press 2:InnerProd \n Press 3:Dice Coefficient")
    measure_choice = input("Enter similarity choice: ")
    if measure_choice == '1':
        measure_sim = 'CosSim'
    elif measure_choice == '2':
        measure_sim = 'InnerProd'
    elif measure_choice == '3':
        measure_sim = 'DiceCof'

    query_processing(query,measure_sim)
    list = print_cmd_links()
    print("Links ranked according to the selected Similarity Measure")
    for link_output in list:
        print(link_output)
    print("-----------------------------------------------------------------")
    print("Links ranked according to the Page Rank Score")
    page_list = print_cmd_page_links()
    for page_link_output in page_list:
        print(page_link_output)
