import pandas as pd
import string

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
#Loop through rows of a data frame
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def if_alpha():
    user_input = input("Enter any word: ").upper()
    try:
        spelled = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Only letters please!")
        if_alpha()
    else:
        print(spelled)

if_alpha()#nato_dict


# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# for (index, row) in nato_df.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)