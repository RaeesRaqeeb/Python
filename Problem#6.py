def print_big(letter):
    alphabet = {
        'a': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
        'b': ['**** ', '*   *', '**** ', '*   *', '**** '],
        # Add representations for other letters as needed
    }

    # Convert the input letter to lowercase to handle both uppercase and lowercase letters
    letter = letter.lower()

    # Check if the input letter is in the alphabet dictionary
    if letter in alphabet:
        # Print each line of the representation
        for line in alphabet[letter]:
            print(line)
    else:
        print(f"Letter '{letter}' not supported.")

# Example usage:
print_big('c')
