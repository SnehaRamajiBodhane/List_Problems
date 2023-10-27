#2)book name
def create_list():
    print("========================")
    print("Creating the List")
    print("========================")
    global listsofbooks
    listsofbooks=[ ]
    print("Created List is:",listsofbooks)
def generate_elements():
    print("=======================================")
    print("Assigning the List Elements Manually:")
    print("=======================================")
    listsofbooks.append('A Suitable Boy')
    listsofbooks.append('Amitav Ghosh')
    listsofbooks.append('The God of Small Things')
    listsofbooks.append('The White Tiger')
    listsofbooks.append('The Inheritance of Loss')
    listsofbooks.append('A Fine Balance')
    print("Generated List is:",listsofbooks)
def add_new_elements():
    listsofbooks.append('Khushwant Singh')
    print("Add new elements in the List is:",listsofbooks)

def update_elements():
    print("========================")
    print("Updating the List Elements")
    print("========================") 
      
    listsofbooks[0]='A Suitable Boy'
    listsofbooks[1]='Amitav Ghosh'
    listsofbooks[2]='The God of Small Things'
    listsofbooks[3]='The White Tiger'
    listsofbooks[4]='The Inheritance of Loss'
    listsofbooks[5]='Bhagatavgita'
    listsofbooks[6]='A Fine Balance'
    listsofbooks[2]='Train to Pakistan'
    print("Check the updated Elemensts in list",listsofbooks) 
    
def insert_new_elements():
    print("========================")
    print("Inserting the List Elements")
    print("========================") 
    listsofbooks.insert(4,'Mahabharat')
    print("check the inserting elements in the list is:",listsofbooks)   
def delete_elements():
    print("========================")
    print("Deleting the List Elements")
    print("========================") 
    listsofbooks.remove('A Fine Balance')
    print("check the deleting elements in the list is:",listsofbooks)
def pop_elements():
    print("========================")
    print("Pop the List Elements")
    print("========================") 
    listsofbooks.pop(2)
    print("check the pop elements in the list is:",listsofbooks)
def access_list():  
    print("========================")
    print("Accessing the List Elements")
    print("========================")    
    print("Accessing the List elements by using Indexing")
    print("In Authors List Index 0 : ", listsofbooks[0], end = "\n")
    print("In Authors List Index 1 : ", listsofbooks[1], end = "\n")
    print("In Authors List Index 2 : ", listsofbooks[2], end = "\n")
    print("In Authors List Index 3 : ", listsofbooks[3], end = "\n")
    print("In Authors List Index 4 : ", listsofbooks[4], end = "\n")
    print("In Authors List Index 5 : ", listsofbooks[5], end = "\n")
    print("In Authors List Index 6 : ", listsofbooks[6], end = "\n")
    print(" ")
    print("Accessing the List elements by using Indexing-For Loop ")
    i=0
    for index in listsofbooks:
        print("Authors  name in the List Position",i,"is",index,end="\n")
        i=i+1
    print("Accessing the List elements by using Indexing-While Loop ")
    y=0
    while y<len(listsofbooks):
        print("Authors  name in the List Position",y,"is",listsofbooks[y],end="\n")
        y=y+1
     
def main():
    create_list()
    generate_elements()
    add_new_elements()
    access_list()
    update_elements()
    insert_new_elements()
    delete_elements()
    pop_elements()
    
if __name__ == "__main__":
    main()