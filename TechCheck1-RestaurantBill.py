#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    ### Introduce User to the Application
    print("Welcome to the Bill Calculator\n")

    ### Assign Variables
    BILL_HARDCODED = 85
    TAX_RATE = 0.15
    TIP_RATE = 0.2

    ### Ask User if they want to use the program normally or use hard-coded values
    mode = int(input("WOULD YOU LIKE TO RUN THIS PROGRAM NORMALLY OR WITH PRE-DETERMINED VALUES(TESTING)?\n 1 - Default \n 2 - Testing\n Input: "))
    print("")

    ### (OPTION 1 ONLY) - Enter bill amount
    if mode == 1:
        bill_amount = float(input("Please enter your original bill amount: "))

    ### Display bill amount
    bill_update = 0

    if mode == 1 or mode == 2:
        match mode:
            case 1:
                bill_update = bill_amount
            case 2:
                bill_update = BILL_HARDCODED
    else:
        print("Invalid answer, program ended.")
    print("Your original bill amount is: ${0:.2f}".format(bill_update))

    ### Display your tax amount
    tax_value = bill_update * TAX_RATE
    print("Your tax is: {0:.2f}%".format(tax_value))

    ### Display your tip amount
    tip_value = bill_update * TIP_RATE
    print("Your tip is: {0:.2f}%".format(tip_value))

    ### Display the bill total amount 
    total_bill = bill_update + tax_value + tip_value
    print("Your total is: ${0:.2f}".format(total_bill))
    print("")
    # YOUR CODE ENDS HERE

main()