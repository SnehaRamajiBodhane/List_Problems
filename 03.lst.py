"""
1.Create a List Empty List.
2.Generate a Elements.
3.Access the Elements.
4.Update the Elemensts.
5.Check the updated Elemensts.
6.add new elements .
7.insert new elements at particular position.
8.Delete the element at particular position.
9.access the element at particular position.
10.pop the element.
"""
#1)
def create_list():
    print("========================")
    print("Creating the List")
    print("========================")
    global listsofauthors
    listsofauthors=[ ]
    print("Created List is:",listsofauthors)
def generate_elements():
    print("=======================================")
    print("Assigning the List Elements Manually:")
    print("=======================================")
    listsofauthors.append('Chetan Bhagat')
    listsofauthors.append('Jay Shetty')
    listsofauthors.append('R. K. Narayan')
    listsofauthors.append('Arundhati Roy')
    listsofauthors.append('Jhumpa Lahiri')
    listsofauthors.append('Sudha Murthy')
    print("Generated List is:",listsofauthors)
def add_new_elements():
    listsofauthors.append('Khushwant Singh')
    print("Add new elements in the List is:",listsofauthors)

def update_elements():
    print("========================")
    print("Updating the List Elements")
    print("========================") 
      
    listsofauthors[0]='Sneha Bodhane'
    listsofauthors[1]='GAurav Bodhane'
    listsofauthors[2]='R. K. Narayan'
    listsofauthors[3]='Arundhati Roy'
    listsofauthors[4]='Jhumpa Lahiri'
    listsofauthors[5]='Sudha Murthy'
    listsofauthors[6]='Khushwant Singh'
    listsofauthors[2]='sneha'
    print("Check the updated Elemensts in list",listsofauthors) 
    
def insert_new_elements():
    print("========================")
    print("Inserting the List Elements")
    print("========================") 
    listsofauthors.insert(3,'Gaurav')
    print("check the inserting elements in the list is:",listsofauthors)   
def delete_elements():
    print("========================")
    print("Deleting the List Elements")
    print("========================") 
    listsofauthors.remove('Sudha Murthy')
    print("check the deleting elements in the list is:",listsofauthors)
def pop_elements():
    print("========================")
    print("Pop the List Elements")
    print("========================") 
    listsofauthors.pop(3)
    print("check the pop elements in the list is:",listsofauthors)
def access_list():  
    print("========================")
    print("Accessing the List Elements")
    print("========================")    
    print("Accessing the List elements by using Indexing")
    print("In Authors List Index 0 : ", listsofauthors[0], end = "\n")
    print("In Authors List Index 1 : ", listsofauthors[1], end = "\n")
    print("In Authors List Index 2 : ", listsofauthors[2], end = "\n")
    print("In Authors List Index 3 : ", listsofauthors[3], end = "\n")
    print("In Authors List Index 4 : ", listsofauthors[4], end = "\n")
    print("In Authors List Index 5 : ", listsofauthors[5], end = "\n")
    print("In Authors List Index 6 : ", listsofauthors[6], end = "\n")
    print(" ")
    print("Accessing the List elements by using Indexing-For Loop ")
    i=0
    for index in listsofauthors:
        print("Authors  name in the List Position",i,"is",index,end="\n")
        i=i+1
    print("Accessing the List elements by using Indexing-While Loop ")
    y=0
    while y<len(listsofauthors):
        print("Authors  name in the List Position",y,"is",listsofauthors[y],end="\n")
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



