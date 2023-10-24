

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift, direction):
    alphabet_shifted = ""
    shift = (shift % 26)
    for alph in text:
        if alph not in alphabet:
            alphabet_shifted += alph
            continue
        alphabet_index = int(alphabet.index(alph))
        index = 0
        len = 26
        if direction == "encode":
            index = alphabet_index + shift - len
            
        elif direction == "decode":
            index = alphabet_index - shift

        alphabet_shifted += alphabet[index]

    # return "".join(alphabet_shifted)
    return alphabet_shifted

rerun = True
while rerun==True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    message = encrypt(text, shift, direction)
    print(message)
    should_continue = input("Do you want to continue playing? (y/n): ")
    if should_continue == 'y':
        continue
    else:
        rerun = False

print("GoodBye")



    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

# print(alphabet.index('z'))

