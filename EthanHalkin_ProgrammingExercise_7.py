#The entire program depends on this one line
import re 


#Global Constant that is the regular expression pattern for a sentence
#90% sure re.m means MULTILINE and re.s is DOTALL
#Comment that explains the re: Checks for capital or digit followed by nongreedy amount of anything that ends
# when a punctuation is used. However the punctuation only works when another capital or digit follows it, or if its the end of a sentence.
SENTENCE_PATTERN = re.compile(r'[A-Z\d].*?[.!?](?= [A-Z\d]|$)', flags=re.M | re.S)

#felt adverse to using Lorem Ipsum
'''
I will test the pattern using these sentences! At least 7 sentences will be used. 
2 cutoffs will 
happen before the period. Along with the number in the prior sentence. There will be 
1 abbreviation that means nothing. For example this a.b.b.r.e.v.i.a.t.i.o.n. Final sentence.
'''



def display_paragraph(list_of_sentences):
    '''
    Displays each sentence from a paragraph, then follows it with the amount of sentences.
    Parameters:
        list_of_sentences (list): A user's paragraph that was seperated into a list of sentences.
    Variables:
        None
    Logic:
        1. Initates a for loop that displays each sentence from the list.
        2. Displays the length of the list.
    Return:
        None
    '''

    #loops through the list and displays each sentence
    for index in list_of_sentences:

        #kinda regret naming the placeholder index, but I can't think of a better name
        #using the arrow to signify the start of a new sentence
        print('->', index)

    #displays how many sentences were in the list
    #I don't fully understand what's the difference between doing this or concatenation
    # when format strings accomplish the same thing
    #Sure you can use sep=, but that just makes concatenation feel purposeless.
    print('Your paragraph contained', len(list_of_sentences), 'sentences.')


def seperate_paragraph(user_paragraph):
    '''
    Seperates the parameter into a list based on if it matches the global constant
    Parameter:
        user_paragraph (string): A paragraph that the user wrote. It is assumed to be grammatically correct (capitalization-wise).
    Variables:
        seperated_paragraph_list (list): A list comprised of the matched sentences found in the parameter.
    Logic:
        1. Seperates the user paragraph based on its sentences.
        2. Returns the resulting list.
    Return:
        list: A list comprised of sentences.
    '''

    #Matches each sentence in user_paragraph to the global constant then assigns it to a list.
    #pretty sure I don't have to use flags here as the constant has the flags attached.
    seperated_paragraph_list = re.findall(SENTENCE_PATTERN, user_paragraph)

    return seperated_paragraph_list

if __name__ == '__main__':

    #Asks user to enter in a paragraph
    #I have no qualms with reusing the parameter from seperate_paragraph
    user_paragraph = input('Please enter in the paragraph you want checked:\t')

    #sends user input into seperate paragraph
    list_of_sentences = seperate_paragraph(user_paragraph)

    #Sends list of sentences into the display function
    display_paragraph(list_of_sentences)