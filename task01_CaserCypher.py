import string

# Function to encrypt text using the Caesar cipher
def caesercypher_encrypt(text, shift):

    # Get lowercase and uppercase alphabets
    alphabets_lower = string.ascii_lowercase
    alphabets_upper = string.ascii_uppercase
    encrypt_text = ""

    # Iterate through each character in the text
    for alphabet in text:

        # If the character is a lowercase alphabet
        if alphabet in alphabets_lower:

            # Get the index of the current alphabet in the lowercase alphabet string
            current_index = alphabets_lower.index(alphabet)

            # Calculate the new index after applying the shift and wrap around if needed
            encrypt_index = (current_index + shift) % 26

            # Append the encrypted alphabet to the result string
            encrypt_text += alphabets_lower[encrypt_index]

        # If the character is an uppercase alphabet
        elif alphabet in alphabets_upper:

            # Get the index of the current alphabet in the uppercase alphabet string
            current_index = alphabets_upper.index(alphabet)

            # Calculate the new index after applying the shift and wrap around if needed
            encrypt_index = (current_index + shift) % 26

            # Append the encrypted alphabet to the result string
            encrypt_text += alphabets_upper[encrypt_index]
        else:

            # If the character is not an alphabet, simply append it to the result string
            encrypt_text += alphabet
    return encrypt_text

# Function to decrypt text using the Caesar cipher
def caesercypher_decrypt(text, shift):

    # Get lowercase and uppercase alphabets
    alphabets_lower = string.ascii_lowercase
    alphabets_upper = string.ascii_uppercase
    decrypt_text = ""

    # Iterate through each character in the text
    for alphabet in text:

        # If the character is a lowercase alphabet
        if alphabet in alphabets_lower:

            # Get the index of the current alphabet in the lowercase alphabet string
            current_index = alphabets_lower.index(alphabet)

            # Calculate the new index after applying the shift and wrap around if needed
            decrypt_index = (current_index - shift) % 26

            # Append the decrypted alphabet to the result string
            decrypt_text += alphabets_lower[decrypt_index]

        # If the character is an uppercase alphabet
        elif alphabet in alphabets_upper:

            # Get the index of the current alphabet in the uppercase alphabet string
            current_index = alphabets_upper.index(alphabet)

            # Calculate the new index after applying the shift and wrap around if needed
            decrypt_index = (current_index - shift) % 26

            # Append the decrypted alphabet to the result string
            decrypt_text += alphabets_upper[decrypt_index]
        else:
            # If the character is not an alphabet, simply append it to the result string
            decrypt_text += alphabet
    return decrypt_text

# Function to get user selection (encrypt or decrypt)
def user_selection():

    # Ask the user to input their selection (Encrypt or Decrypt)
    select = input("Enter E If You Want To Encrypt The Text\nEnter D if You Want To Decrypt The Text\n==").upper()
    return select

# Function to handle user input and output
def output():

    # Get the user's selection (Encrypt or Decrypt)
    selection = user_selection()

    # If the selection is Encrypt
    if selection == "E":

        # Get the text to encrypt from the user
        text = input("Enter The Text To Encrypt==")

        # Get the shift value for encryption from the user
        shift = int(input("Enter The Shift Value For The Encryption=="))

        # Encrypt the text using the Caesar cipher and print the result
        print("The Encrypted Text Is==", caesercypher_encrypt(text, shift))

    # If the selection is Decrypt
    elif selection == "D":

        # Get the text to decrypt from the user
        text = input("Enter The Text To Decrypt==")

        # Get the shift value for decryption from the user
        shift = int(input("Enter The Shift Value For The Decryption=="))

        # Decrypt the text using the Caesar cipher and print the result
        print("Decrypted Text Is ==", caesercypher_decrypt(text, shift))

    # If the selection is neither Encrypt nor Decrypt
    else:
        # Inform the user to enter the correct selection

        print("Please Enter The correct Selection!!")
        
        # Ask for the user's selection again
        output()

# Call the output function to start the program
output()
