#Creating an empty list to store the laptops
laptop = []  #empty list
#Defining a function to read the laptop data from a file
def readLaptop():
    laptop.clear()
    #opening the file in read mode 
    file = open("laptops.txt" , "r")
    #message that shows that the file is being read
    print("\t  Please wait laptops.txt file is currently being read .......")
    # it loops through each line in the file
    for i in file:
        #it splits the line into individual fields and adds commas between each space
        data = (i.strip()).split(", ")
        #appends to the laptop list as a new elements
        laptop.append(data)
    print("\t  Congratulation, The 'laptops.txt' file has been successfully read.")
    print("\t Please wait while the laptop data is being printed...")
    # header for the laptop data table
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("S.no  Laptop Name         Company Name    Price   Quantity   Generation      Graphics")
    print("----------------------------------------------------------------------------------------------------------------------------")
    #loops through each laptop in the list and print its data in tabular format
    for each in laptop:
            print(f"{each[0]:<6} {each[1]:<20} {each[2]:<15} ${each[3]:<6} {each[4]:<10} {each[5]:<15} {each[6]}")
    print("----------------------------------------------------------------------------------------------------------------------------")