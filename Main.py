#importing the modules
import buy_Sale 
import Welcome
import Read_function

Welcome.welcomeMessage()#calling the welcome message function from the intro module

#defining a function to handle user input
def check_input():
    # this loop will run indefinitely until the user chooses to exit the program
    while True:
        # print a menu of options for the user
        print("-------------------------------------------------------------------------------------------")
        print("Below are the options for you to carry out the necessary operations in the system")
        print("-------------------------------------------------------------------------------------------")
        print("\n")
        print("Press 1 to sell laptops to customers.")
        print("Press 2 to purchase laptops from manufacturers.")
        print("Press 3 to exit the system.")
        print("\n")
        print("--------------------------------------------------------------------------------------------")
        print("\n")
        # input value for the user
        input_ = input("\nEnter your choice: ")

        if input_ == "1":
            Read_function.readLaptop()# calling the readLaptop function from the Read_function module
            buy_Sale.laptops_sold()# calling the laptops_sold function from the buy_sale module1
            
        elif input_ == "2":
            buy_Sale.buy_laptops()

        elif input_ == "3":
            print("Thank you for using the Laptop Sales Management System. Goodbye!")
            print("\n")
            break

        else:
            print("\nInvalid input. Please try again.\n")

check_input()

        
