from alphabet import alphabet, alph_key

# encode function will encode message using the rotate method from the collection library
# rotate method moves list items to the right depending on spaces.
def encode(message, shift):
    alphabet.rotate(shift)
    encrypted_message = []

    for letter in message:
        if letter == ' ':
            encrypted_message.append(' ')
        else:
            index = alph_key.get(letter)
            encrypted_message.append(alphabet[int(index)])

    return "".join(encrypted_message)
