from alphabet import alphabet, alph_key


# this function will decode messages based on the number of shifts
def decode(message, shift):
    alphabet.rotate(shift)
    decrypted_message = []

    # for loop will retrieve the index of the letter when rotated to find original letter
    for letter in message:
        if letter == ' ':
            decrypted_message.append(' ')
        else:
            index = alphabet.index(letter)
            # place keys in a list to be able to find using its index
            keys = list(alph_key.keys())
            real_letter = keys[int(index)]
            decrypted_message.append(real_letter)

    alphabet.rotate(-shift)

    return ''.join(decrypted_message)
