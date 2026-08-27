#GLOBAL COMMENT: I don't know whether I should use end='\n\n' or just do \n at the end of a print statement

def ticket_sale_loop(tickets_in_stock, tickets_per_buyer):
    """
    Requests how many tickets a buyer wants, then displays how many tickets are left
    Loops until sold out
    
    Parameters:
        tickets_in_stock (int): The amount of tickets left in stock
        tickets_per_buyer (int): The amount of tickets a buyer is allowed to buy
    Variables:
        buyers (int): The number goes up every time a succesful sale is made
        tickets_bought (int): Asks for the amount of tickets bought
    Logic:
        1. Inits the two main variables
        2. Activates while loop that repeats until tickets_in_stock drops to 0
        3. Asks for amount of tickets bought and checks if its valid.
        4. If valid, then it subtracts from tickets_in_stock and +=1 to accumulator
        5. Loop closes upon reaching zero and returns the amount of buyers        
    Return:
        accumulator: The amount of buyers

    """
    #initializes the buyer amount
    buyers = 0

    #initializes the input variable
    tickets_bought = 0

    #Loops until all tickets are gone
    while tickets_in_stock > 0:

        #displays the amount of tickets left in stock
        print(f'The amount of tickets left in stock: {tickets_in_stock}', end='\n\n')

        #tries an input statement. If there is a ValueError it notifies the user and asks the input statement again.
        try:
            tickets_bought = int(input(f'Please input the amount of tickets being bought. Make sure not to exceed the limit of {tickets_per_buyer} tickets:\t'))
        except ValueError:

            #I added multiple \n for emphasis
            print('\nThere was a ValueError with the input. Please make sure to enter an integer next time.\n')
            continue

        #Checks to see if tickets_bought is invalid based on circumstances
        if tickets_bought > tickets_per_buyer or tickets_bought > tickets_in_stock:

            #similar to the exception, I added multiple \n for emphasis.
            #I also added a continue statement to return back to start of the loop
            print('\nThe buyer tried to buy an invalid amount. Please try again.\n')
            continue
        #Checks to see if the buyer actually bought something
        elif tickets_bought == 0:

            #displays to user what went wrong
            print('\nThe buyer did not buy anything. Please try again.', end='\n\n')
            continue
        else:
            #subtracts from total, then adds to accumulator
            tickets_in_stock -= tickets_bought
            buyers += 1

    #returns the accumulator
    return buyers

#abbreviated amount, should be fine
def display_amount_of_buyers(amnt_displayed):
    """
    Displays to user how many buyers bought tickets

    Parameters:
        amnt_displayed (int): amount of buyers that will be displayed in print statement
    Variables:
        none
    Logic:
        1. Formats the parameter into a print statement
    Return:
        none
    """
    print(f'\t{amnt_displayed} people bought tickets today.')



if __name__ == "__main__":

    #Creates a variable to return the amount of buyers to
    amount_of_buyers = ticket_sale_loop(20, 4)

    #Displays to user the amount of buyers
    display_amount_of_buyers(amount_of_buyers)