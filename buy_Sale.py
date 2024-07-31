#importing all the needed modules
import datetime
import Read_function
import Write_function

time = datetime.datetime.now()

# Create empty list to store the laptop sold and the price
laptopsold = []
price_list = []

def laptops_sold():
    while True:
        # getting the laptop ID from user
        Laptop_id = input(" Please! , Enter the id of the laptop you want to sell: ")

        #Find the laptop in the database.
        for each in Read_function.laptop:
            if Laptop_id == each[0]:  # checks if the provided ID matches with any laptop in stock
                while True:
                    try:
                        #getting the quantity from the user
                        quantity = int(input(" Please! , Enter the required quantity: "))
                        if 0<quantity<=int(each[4]): # the quantity should be greater than 0 and less then the quantity in stock
                            break
                        else: # if the quantity is less than 0 or higher tha the stock quantity this message will be printed
                            print("Sorry, invalid input found please enter either positive value or quantity shouldnot exceed the available laptop.")
                    except ValueError:
                        print("Please only enter numbers")
                #check if the quantity is available.
                if quantity < int(each[4]):
                    #update the quantity in database.
                    each[4] = str(int(each[4])-int(quantity))
                    Write_function.write_to_file(1)
                    #calculate the price of sold laptops.
                    price = str(int(each[3] )* int(quantity))
                    price_list.append(price)
                    #adds the sold laptop in the empty list of laptopsold
                    laptopsold.append([each[1], each[2], each[3],quantity])
                    while True:
                        # verifies the user to either buy more laptops by typing 'yes' or generate the bill by typing 'no'
                        sell_again = input("Enter 'yes' to sell more laptoops and enter 'no' to return for bill generation('yes' OR 'no')").lower()
                        if sell_again == "yes": # user types yes
                            laptops_sold() # the code runs from the star again
                            break
                        elif sell_again == "no": # user types no
                            print("Thank you for shopping with us.")# prints the message and calculates the total price with VAT
                            total_price= 0 
                            for price in price_list:
                                total_price += int(price) # calculate of total price without vat
                            total_pricevat = str(total_price +(total_price *0.13)) # total price after vat
                            while True:
                                
                                while True:
                                    shipping = input("Enter 'yes' to add shipping charge and 'no' to generate bill without shipping('yes' OR 'no')").lower()
                                    transport_cost= 0
                                    if shipping == "yes": # if the user types 'yes' then the value of transport_cost will be 10 and will be added to bill
                                        transport_cost = 10
                                        total_price = 0
                                        break
                                    #Grand_total = str(total_pricevat + transport_cost)
                                    elif shipping == "no": # If the user types 'no; then the transport_cost will be set to 0
                                        print("shipping charge is not included")
                                        break
                                        #Grand_total = total_pricevat
                                    else: # if user doesnt type yes or no then this messagae will show
                                        print("Sorry please type only yes or no")
                                    
                                for each in Read_function.laptop:
                                    total_price += int(each[3]) # calculates the total price of all the laptops
                                Grand_total =str(float(total_pricevat) + transport_cost)# Grandtotal cost by adding total price with vat and transport cost 
                                today_date_and_time = datetime.datetime.now() # Writes the current date and tme
                                print("Enter your details to continue")
                                Costumer_name = input("Enter your name: ")
                                Costumer_address = input("Enter your address: ")
                                Costumer_number = input("Enter your phone number: ")

                                #write the bill to a file
                                bill_file = open(str(time.hour)+ str(time.minute)+" "+Costumer_name+".txt","w")
                                bill_file.write("\n")
                                print("\n")
                                bill_file.write("\t\tYour bill is: \n")
                                print("\t\tYour bill is: ")
                                bill_file.write("Durbar Marga, Kathmandu \tPhone: 000-555-2222 \n")
                                print("\t\tDurbar Marga, Kathmandu \tPhone: 000-555-2222")
                                bill_file.write("--------------------------------------------------------------------\n")
                                print("--------------------------------------------------------------------")
                                bill_file.write("Name of the Customer: "+str(Costumer_name)+"\n")
                                print("Name of the Customer: "+str(Costumer_name))
                                bill_file.write("Address of the Customer: "+str(Costumer_address)+"\n")
                                print("Address of the Customer: "+str(Costumer_address))
                                bill_file.write("Phone Number of the Customer: "+str(Costumer_number)+"\n")
                                print("Phone Number of the Customer: "+str(Costumer_number))
                                bill_file.write("Date and Time of purchase: "+str(today_date_and_time)+"\n")
                                print("Date and Time of purchase: "+str(today_date_and_time))
                                bill_file.write("--------------------------------------------------------------------\n")
                                print("-------------------------------------------------------------------------")
                                for each in laptopsold:
                                    bill_file.write("Laptop ID: "+str(each[0])+"\n")
                                    print("Laptop ID: "+str(each[0]))
                                    bill_file.write("Laptop Name: "+str(each[1])+"\n")
                                    print("Laptop Name: "+str(each[1]))
                                    bill_file.write("Laptop Price: "+str(each[2])+"\n")
                                    print("Laptop Price: "+str(each[2]))
                                    bill_file.write("Laptop Quantity: "+str(each[3])+"\n")
                                    print("Laptop Quantity: "+str(each[3]))
                                    print("--------------------------------------------------------------------")
                                bill_file.write("--------------------------------------------------------------------\n")
                                print("--------------------------------------------------------------------")
                                bill_file.write("Shipping cost is: $"+str(transport_cost)+"\n")
                                print("Shipping cost is: $"+str(transport_cost))
                                bill_file.write("Grand Total is: $" +str(Grand_total)+"\n")
                                print("Grand Total is: $"+str(Grand_total))
                                bill_file.write("P.S: Shipping cosdt has already been added to the grand total  \n")
                                print("P.S: Shipping cosdt has already been added to the grand total")
                                bill_file.close()

                                return 
                                
                            
                        else:
                            print("please write yes or no only ")
                    
                            

                        

                elif int(quantity)== int(each[4]):
                    (Read_function.laptop).remove(each)
                    price = str(int(each[3] )* int(quantity))
                    price_list.append(price)
                    laptopsold.append([each[1], each[2], each[3],quantity])
                    Write_function.write_to_file(Read_function.laptop)
                    #calculate the price.
                    
                    while True:
                        sell_again = input("Enter 'yes' to sell more laptoops and enter 'no' to return for bill generation('yes' OR 'no')").lower()
                        if sell_again == "yes":
                            laptops_sold()
                            break
                        elif sell_again == "no":
                            print("Thank you for shopping with us.")
                            total_price= 0
                            for price in price_list:
                                total_price += int(price)
                            total_pricevat = str(total_price +(total_price *0.13))

                            while True:
                                
                                shipping = input("Enter 'yes' to add shipping charge and 'no' to generate bill without shipping('yes' OR 'no')").lower()
                                
                                if shipping == "yes":
                                    transport_cost = 10
                                    total_price = 0
                                #Grand_total = str(total_pricevat + transport_cost)
                                elif shipping == "no":
                                    print("shipping charge is not included")
                                    transport_cost =  0
                                    #Grand_total = total_pricevat
                                else:
                                    print("Sorry please type only yes or no")
                                    
                                for each in Read_function.laptop:
                                    total_price += int(each[3])
                                Grand_total =str(float(total_pricevat) + transport_cost)
                                today_date_and_time = datetime.datetime.now()
                                print("Enter your details to continue")
                                Costumer_name = input("Enter your name: ")
                                Costumer_address = input("Enter your address: ")
                                Costumer_number = input("Enter your phone number: ")

                                #write the bill to a file
                                bill_file = open(str(time.hour)+ str(time.minute)+" "+Costumer_name+".txt","w")
                                bill_file.write("\n")
                                print("\n")
                                bill_file.write("\t\tYour bill is: \n")
                                print("\t\tYour bill is: ")
                                bill_file.write("Durbar Marga, Kathmandu \tPhone: 000-555-2222 \n")
                                print("\t\tDurbar Marga, Kathmandu \tPhone: 000-555-2222")
                                bill_file.write("--------------------------------------------------------------------\n")
                                print("--------------------------------------------------------------------")
                                bill_file.write("Name of the Customer: "+str(Costumer_name)+"\n")
                                print("Name of the Customer: "+str(Costumer_name))
                                bill_file.write("Address of the Customer: "+str(Costumer_address)+"\n")
                                print("Address of the Customer: "+str(Costumer_address))
                                bill_file.write("Phone Number of the Customer: "+str(Costumer_number)+"\n")
                                print("Phone Number of the Customer: "+str(Costumer_number))
                                bill_file.write("Date and Time of purchase: "+str(today_date_and_time)+"\n")
                                print("Date and Time of purchase: "+str(today_date_and_time))
                                bill_file.write("--------------------------------------------------------------------\n")
                                print("-------------------------------------------------------------------------")
                                for each in laptopsold:
                                    bill_file.write("Laptop Name: "+str(each[0])+"\n")
                                    print("Laptop Name: "+str(each[0]))
                                    bill_file.write("Laptop Brand: "+str(each[1])+"\n")
                                    print("Laptop Brand: "+str(each[1]))
                                    bill_file.write("Laptop Price: "+str(each[2])+"\n")
                                    print("Laptop Price: "+str(each[3]))
                                    bill_file.write("Laptop Quantity: "+str(each[3])+"\n")
                                    print("Laptop Quantity: "+str(each[3]))
                                    print("--------------------------------------------------------------------")
                                bill_file.write("--------------------------------------------------------------------\n")
                                print("--------------------------------------------------------------------")
                                bill_file.write("Shipping cost is: $"+str(transport_cost)+"\n")
                                print("Shipping cost is: $"+str(transport_cost))
                                bill_file.write("Grand Total is: $" +str(Grand_total)+"\n")
                                print("Grand Total is: $"+str(Grand_total))
                                bill_file.write("P.S: Shipping cosdt has already been added to the grand total  \n")
                                print("P.S: Shipping cosdt has already been added to the grand total")
                                bill_file.close()

                                return 
                        else:
                            print("Please enter yes or no only")
                            
                else:
                    print("Quantity is not enough")
                    
                break
        else:
            print("sorry wrong laptop ID please try again")
            



buylaptops = []
List_Of_Price =[]
def buy_laptops():
    Read_function.readLaptop()
    
    while True:
        #get the user's input.
        Laptop_name = input("Enter the name of laptop: ")
        Laptop_brand = input("Enter the brand of laptop: ")
        while True:
            try:
                Laptop_price = int(input("Enter the price of laptop: "))
                if 0< Laptop_price:
                    break  
                else:
                    print("Price cannot be negative or zero please enter a valid input\n-->")     
            except ValueError:
                print("Please enter valid number!!")
        while True:
            try:
                Laptop_quantity = input("Enter the quantity of laptop: ")
                if 0< int(Laptop_quantity):
                    break
                else:
                    print("Quantity cannot be negative or zero please enter a valid input\n-->")
            except ValueError:
                print("please enter a valid quantity")
        Laptop_processor = input("Enter the processor of laptop: ")
        Laptop_graphics = input("Enter the graphic of laptop: ")

        #Checking if the laptopp already exists
        laptop_exists = False
        for each in Read_function.laptop:
            if (Laptop_name == each[1] and
                Laptop_brand == each[2] and
                str(Laptop_price) == each[3] and
                Laptop_processor == each[5] and
                Laptop_graphics == each[6]):
                # if the laptop alresdy exists, so update the quantity.
                new_quantity = str(int(each[4])+int(Laptop_quantity))
                each[4] = new_quantity
                Write_function.write_to_file(Read_function.laptop)
                buylaptops.append((each[1], each[2], each[4], new_quantity))
                laptop_exists = True
                break
        
        #If the laptop doesn't exist, add it to the list
        if not laptop_exists:
            (Read_function.laptop).append([str(len(Read_function.laptop)+1), Laptop_name, Laptop_brand, Laptop_price, Laptop_quantity, Laptop_processor, Laptop_graphics])
            Write_function.write_to_file(Read_function.laptop)
            price = str(int(Laptop_price)* int(Laptop_quantity))
            List_Of_Price.append(price)
            buylaptops.append([Laptop_name, Laptop_brand, Laptop_price, Laptop_quantity])
        while True:
            sell_again = (input("Enter 'yes' to buy more laptoops and enter 'no' to return for bill generation('yes' OR 'no')")).lower()
            if sell_again == "yes":
                buy_laptops()
                break
            elif sell_again == "no":
                print("Bill is going to be generated please fill the below information.")
                while True:
                    shipping = input("Enter 'yes' to add shipping charge and 'no' to generate bill without shipping('yes' OR 'no')").lower()
                    transport_cost =  0
                    if shipping == "yes":
                        transport_cost = 10
                        total_price = 0
                        break
                        #Grand_total = str(total_pricevat + transport_cost)
                    elif shipping == "no":
                        print("Shipping charge is not included")
                        break
                        #Grand_total = total_pricevat
                    else:
                        print("Sorry please type only yes or no")
                total_price= 0
                for price in List_Of_Price:
                    price = str(int(each[3] )* int(Laptop_quantity))
                    total_price += int(price)
                total_pricevat = str(total_price +(total_price *0.13))
                total_price += int(each[3])
                Grand_total =str(float(total_pricevat) + transport_cost)
                today_date_and_time = datetime.datetime.now()
                print("Enter your details to continue")
                Costumer_name = input("Enter your name: ")
                Costumer_address = input("Enter your address: ")
                Costumer_number = input("Enter your phone number: ")

                #write the bill to a file
                bill_file = open(str(time.hour)+ str(time.minute)+" "+Costumer_name+".txt","w")
                bill_file.write("\n")
                print("\n")
                bill_file.write("\t\tYour bill  \n")
                print("\t\tYour bill is: ")
                bill_file.write("Durbar Marga, Kathmandu \tPhone: 000-555-2222 \n")
                print("\t\tDurbar Marga, Kathmandu \tPhone: 000-555-2222")
                bill_file.write("--------------------------------------------------------------------\n")
                print("-------------------------------------------------------------------")
                bill_file.write("Name of the Customer: "+str(Costumer_name)+"\n")
                print("Name of the Customer: "+str(Costumer_name))
                bill_file.write("Address of the Customer: "+str(Costumer_address)+"\n")
                print("Address of the Customer: "+str(Costumer_address))
                bill_file.write("Phone Number of the Customer: "+str(Costumer_number)+"\n")
                print("Phone Number of the Customer: "+str(Costumer_number))
                bill_file.write("Date and Time of purchase: "+str(today_date_and_time)+"\n")
                print("Date and Time of purchase: "+str(today_date_and_time))
                bill_file.write("--------------------------------------------------------------------\n")
                print("-------------------------------------------------------------------")
                for each in buylaptops:
                    bill_file.write("Laptop Name: "+str(each[0])+"\n")
                    print("Laptop Name: "+str(each[0]))
                    bill_file.write("Laptop Brand: "+str(each[1])+"\n")
                    print("Laptop Brand: "+str(each[1]))
                    bill_file.write("Laptop Price: "+str(each[2])+"\n")
                    print("Laptop Price: "+str(each[2]))
                    bill_file.write("Laptop Quantity: "+str(each[3])+"\n")
                    print("Laptop Quantity: "+str(each[3]))
                print("-------------------------------------------------------------------")
                bill_file.write("-------------------------------------------------------------------\n")
                print("-------------------------------------------------------------------")
                bill_file.write("Shipping cost is: $"+str(transport_cost)+"\n")
                print("Shipping cost is: $"+str(transport_cost))
                bill_file.write("Grand Total is: $" +str(Grand_total)+"\n")
                print("Grand Total is: $"+str(Grand_total))
                bill_file.write("P.S: Shipping cosdt has already been added to the grand total  \n")
                print("P.S: Shipping cosdt has already been added to the grand total")
                bill_file.close()

                return 
            else:
                print("Invalid input")
                
            



