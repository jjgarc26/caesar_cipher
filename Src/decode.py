from alphabet import alphabet, alph_key

def decode(message, shift):
    for letter in message:
        index = alph_key.get(letter)
        sum = int(index) + shift

    # alphabet.rotate(-shift)
    # encrypted_message = []
    #
    # for letter in message:
    #     if letter == ' ':
    #         encrypted_message.append(' ')
    #     else:
    #         index = alph_key.get(letter)
    #         encrypted_message.append(alphabet[int(index)])
    #
    # return "".join(encrypted_message)
