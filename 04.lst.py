def create_list():
    print("========================")
    print("Creating the List")
    print("========================")
    global listsofstate
    listsofstate=[ ]
    print("Created List is:",listsofstate)
def generate_elements():
    print("=======================================")
    print("Assigning the List Elements Manually:")
    print("=======================================")
    listsofstate.append('Andhra Pradesh')
    listsofstate.append('Assam')
    listsofstate.append('Bihar')
    listsofstate.append('Delhi ')
    listsofstate.append('Goa')
    listsofstate.append('Gujarat')
    print("Generated List is:",listsofstate)
def add_new_elements():
    listsofstate.append('Khushwant Singh')
    print("Add new elements in the List is:",listsofstate)

def update_elements():
    print("========================")
    print("Updating the List Elements")
    print("========================") 
      
    listsofstate[0]='Andhra Pradesh'
    listsofstate[1]='Assam'
    listsofstate[2]='Bihar'
    listsofstate[3]='Delhi '
    listsofstate[4]='Goa'
    listsofstate[5]='Gujarat'
    listsofstate[6]='Haryana'
    listsofstate[2]='Himachal Pradesh'
    print("Check the updated Elemensts in list",listsofstate) 
    
def insert_new_elements():
    print("========================")
    print("Inserting the List Elements")
    print("========================") 
    listsofstate.insert(4,'Goa')
    print("check the inserting elements in the list is:",listsofstate)   
def delete_elements():
    print("========================")
    print("Deleting the List Elements")
    print("========================") 
    listsofstate.remove('Haryana')
    print("check the deleting elements in the list is:",listsofstate)
def pop_elements():
    print("========================")
    print("Pop the List Elements")
    print("========================") 
    listsofstate.pop(5)
    print("check the pop elements in the list is:",listsofstate)
def access_list():  
    print("========================")
    print("Accessing the List Elements")
    print("========================")    
    print("Accessing the List elements by using Indexing")
    print("In Authors List Index 0 : ", listsofstate[0], end = "\n")
    print("In Authors List Index 1 : ", listsofstate[1], end = "\n")
    print("In Authors List Index 2 : ", listsofstate[2], end = "\n")
    print("In Authors List Index 3 : ", listsofstate[3], end = "\n")
    print("In Authors List Index 4 : ", listsofstate[4], end = "\n")
    print("In Authors List Index 5 : ", listsofstate[5], end = "\n")
    print("In Authors List Index 6 : ", listsofstate[6], end = "\n")
    print(" ")
    print("Accessing the List elements by using Indexing-For Loop ")
    i=0
    for index in listsofstate:
        print("Authors  name in the List Position",i,"is",index,end="\n")
        i=i+1
    print("Accessing the List elements by using Indexing-While Loop ")
    y=0
    while y<len(listsofstate):
        print("Authors  name in the List Position",y,"is",listsofstate[y],end="\n")
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
