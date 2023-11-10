letter_path = "\\Users\\flpas\\OneDrive - Connection Systems Development\\Python-Development\\day24Files\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt"
name_path = "C:\\Users\\flpas\\OneDrive - Connection Systems Development\\Python-Development\\day24Files\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Input\\Names\\invited_names.txt"
ready_to_send = "C:\\Users\\flpas\\OneDrive - Connection Systems Development\\Python-Development\\day24Files\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Output\\ReadyToSend"
for_process = "C:\\Users\\flpas\\OneDrive - Connection Systems Development\\Python-Development\\day24Files\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Output\\for_process"
letter = ''
names = []

with open(name_path, "r") as name_file:
    names = name_file.readlines()
    names = [name.strip() for name in names]

with open(letter_path, 'r') as file:
    letter = file.read()
    
# new_letter = letter.replace("Dear [name],\n", f"Dear {names[0]},\n")
for i in range(len(names)):
    with open(f"{ready_to_send}\\for_{names[i]}.txt", 'w') as filing:
        new_letter = letter.replace("Dear [name],\n", f"Dear {names[i]},\n")
        filing.write(new_letter)




#     for i in range(len(names)):
#         letter.replace("Dear [name],\n", "Dear {names[i]},\n")
#         with open(for_processf"for_{names[i]}.txt", 'w') as filing:
#             filing.write(letter)

# with open()
# print(names)
# print(letter)
# print(new_letter)



#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp