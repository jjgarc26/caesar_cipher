from encode import encode
from decode import decode
caesar_cipher = "yes"

# we will use while loop to use cipher till user decides to stop
while caesar_cipher == "yes":

    user_choice = input('Would you like to encode or decode?: ')
    message = input(f"Message you'd like to {user_choice}?: ")
    shift = int(input('How many shifts would you like to use?: '))

    if user_choice == 'encode':
        # encode caesar cipher will go here
        message_encode = encode(message, shift)
        print(message_encode)
    else:
        # decode caesar cipher will go here
        message_decode =decode(message, shift)
        print(message_decode)

    # user can choose to continue cipher or not. This will determine while-loop condition
    continue_cipher = input("Would you like to continue?: ")

    if continue_cipher == "yes":
        continue
    else:
        caesar_cipher = 'no'
