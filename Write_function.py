import Read_function
def write_to_file(laptop):
    # opens a new file to write
    file = open("laptops.txt" , "w")
    #loop through each laptop in the list
    for each in Read_function.laptop:
        #Write each field of the laptop to the file, separated by commas
        file.write(str(each[0])+", "+each[1]+", "+each[2]+", "+str(each[3])+", "+str(each[4])+", "+each[5]+", "+each[6]+"\n")
    # Close the file    
    file.close()
    #Print a message to indicate that the file has been written successfully
    print(" Laptop information has been written to file.")