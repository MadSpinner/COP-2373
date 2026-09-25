
#Get the reduce command from functools
from functools import reduce


def max_func(a, b):
    """
    Returns the greater of two numbers. Used in conjuction with the reduce command.
    Paremeters:
        A (float): The first of two numbers
        B (float): The second of two numbers
    Variables:
        None
    Logic:
        1. Checks to see if A is greater than or equal to B
        2. If A is, return A
        3. Else, return B
    Return:
        float: The greater of two numbers
    """

    if a >= b:
        return a
    
    else:
        return b

#same as max func but less than or equal to instead of greater than or equal to
def min_func(a, b):
    """
    Returns the lesser of two numbers. Used in conjuction with the reduce command.
    Paremeters:
        A (float): The first of two numbers
        B (float): The second of two numbers
    Variables:
        None
    Logic:
        1. Checks to see if A is lesser than or equal to B
        2. If A is, return A
        3. Else, return B
    Return:
        float: The lesser of two numbers
    """

    if a <= b:
        return a
    
    else:
        return b

#run this function to get the main lists
def get_user_list():
    """
    Prompts the user into making a list
    Parameters:
        None
    Variables:
        user_expenses_list (list): Appends the type of expenses to this list
        expense_amnt_list (list): Appends the monetary value of the expenses to this list
        user_question (str): Asks the user a question. If they answer yes the program continues
        length_of_user_list (int): Asks the user how long the for loop should loop
        expense_type (str): Asks the user for a name of an expense, then its appended to user_expenses_list
        expense_amnt (str): Asks the user for the amount of an expense, then its appended as a float to expense_amnt_list
    Logic:
        1. initializes both lists
        2. Asks user a question
        3. If the answer is not yes, returns none, none
        4. If the answer contains yes, asks how long the list should be
        5. If an error occurs or the length is less than or equal to zero, return none, none
        6. loop in range of length_of_user_list
        7. Asks the user for the type of expense, and appends the answer
        8. Asks the user for the amount of the expense, and appends a float of it
        9. If an error occurs with step 8, returns none, none
        10. When loop ends, return the two lists
    Return:
        list: Both the type of expenses and their amounts are returned
    """

    #initialize the lists
    user_expenses_list = []

    expense_amnt_list = []

    #asks the user if they want to start the program
    user_question = input('Do you wish to enter in your monthly expenses? Type yes to confirm and type anything else to close:\t')

    if 'yes' in user_question.lower()  or user_question.lower() == 'y':
        #grabs how long the user is willing to make the list
        #if user makes an error, it gets caught
        try:
            length_of_user_list = int(input('Please enter how long the list should be:\t'))

        except ValueError:

            print('A ValueError has occured. Please run the program again to correct this.')
            return None, None
        
        except TypeError:

            print('A TypeError has occured. Please run the program again to correct this.')
            return None, None

        #if user enters a zero or a negative, returns None,None
        if length_of_user_list <= 0:
            return None, None

        #loop amount based on lenght_of_user_list variable
        # underscore used as placeholder
        for _ in range(length_of_user_list):

            #asks user which type of expense this is
            expense_type = input('Please enter the type of expense this is.\t')

            #adds user input to user_expenses_list
            user_expenses_list.append(expense_type)

            #asks user for the amount spent on expense
            expense_amnt = input('Please enter the amount spent.\t')

            #gets rid of dollar signs
            if '$' in expense_amnt:
                expense_amnt = expense_amnt.replace('$','')

            #appends expense_amnt's namesake
            try:
                expense_amnt_list.append(float(expense_amnt))

            except ValueError:

                print(
                    'A ValueError has occured when turning expense_amnt into a float.',
                    'Make sure you are strictly only using numbers when you type the expense amount'
                    )
                return None, None

        #ends the function by returning the two main lists
        return user_expenses_list, expense_amnt_list

    else: return None, None

#gets three different values of a list put through it
def list_reducer(number_list):
    """
    Runs the three main reductions on a list
    Parameters:
        number_list (list): A list that contains only numbers of the same type
    Variables:
        biggest_expense (float): Turns the parameter into its highest value
        smallest_expense (float): Turns the parameter into its lowest value
        total_expense (float): Adds up the sum of the entire list
    Logic:
        1. First, reduce the number_list through the max_func to get its highest number
        2. Second, reduce the number_list through the min_func to get its lowest number
        3. Third, reduce the number_list through a lamda function to get the total number
        4. Finally, returns all numbers gained
    Return:
        float: returns three different float values
    """

    #grabs the biggest number from number_list
    biggest_expense = reduce(max_func, number_list)

    #grabs smallest number from number_list
    smallest_expense = reduce(min_func, number_list)

    #I use lambda here to demonstrate that I can actually use it,
    # normally I wouldn't though as I prefer the neatness of functions
    #grabs total of number_list
    total_expense = reduce(lambda a, b: a + b, number_list)

    #returns the three expenses
    return total_expense, biggest_expense, smallest_expense

#Runs the functions, then displays them
if __name__ == '__main__':

    user_list, user_list_amnt = get_user_list()

    #provides a respose for the user if they decide to shutdown the program or made an error
    if user_list == None or user_list_amnt == None:
    
        print('You have ended the program!')
    elif user_list != None or user_list_amnt != None:
        total_expenses, maximum_expenses, minimum_expenses = list_reducer(user_list_amnt)

        #If there are multiple occurrences of the maximum/minimum, only the first will be labeled, not an error though
        print(f'Your highest expense was {user_list[user_list_amnt.index(maximum_expenses)]}, being ${maximum_expenses:.2f} dollars',
              f'Your lowest expense was {user_list[user_list_amnt.index(minimum_expenses)]}, being ${minimum_expenses:.2f} dollars.',
              f'Your total amount sums up to ${total_expenses:.2f} dollars',
              sep='\n'
              )


    