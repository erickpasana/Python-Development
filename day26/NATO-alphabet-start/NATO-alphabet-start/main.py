import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
#Loop through rows of a data frame
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter any word: ").upper()
# user_input_list = [i for i in user_input]
spelled = [nato_dict[letter] for letter in user_input]
# for u in user_input_list:
#     # val = [value for key, value in nato_dict.items() if u == key]
#     for key, value in nato_dict.items():
#         if u == key:
#             spelled.append(value)
#             break
    # spelled.append(val)


# print(user_input_list)
print(spelled)




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