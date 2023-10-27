def create_list():
     
    #created List
    global stationaryItems
    stationaryItems = ["Pencils", "Papers", "Ball Pens", "Erasers", "Glue Sticks", "Exam Pads"]
   

#Accessing the List Elements
def access_list():
    print("Accessing the List elements by using Indexing")
    print("In stationaryItems List Index 0 : ", stationaryItems[0], end = "\n")
    print("In stationaryItems List Index 1 : ", stationaryItems[1], end = "\n")
    print("In stationaryItems List Index 2 : ", stationaryItems[2], end = "\n")
    print("In stationaryItemsList Index  3 : ", stationaryItems[3], end = "\n")
    print("In stationaryItems List Index 4 : ", stationaryItems[4], end = "\n")
    print("In stationaryItems List Index 5 : ", stationaryItems[5], end = "\n")


    print("========================")
    print("Accessing the List Elements")
    print("========================") 
    print("Accessing the List elements by using Indexing-for Loop ")
    i=0
    for index in stationaryItems:
        print("StationaryItem in the List Position",i,"is",index,end="\n")
        i=i+1
    print("Accessing the List elements by using Indexing-While Loop ")
    y=0
    while y<len(stationaryItems):
        print("StationaryItem in the List Position",y,"is",stationaryItems[y],end="\n")
        y=y+1
def main():
    create_list()
    access_list()
if __name__ == "__main__":
    main()
