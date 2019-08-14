def alphabet_position(letter):

    letter_dict = {'a': 0, 'A': 0, 'b': 1, 'B': 1, 'c': 2, 'C': 2, 'd': 3, 'D': 3, 'e': 4, 'E': 4, 'f': 5, 'F': 5, 'g': 6, 'G': 6, 'h': 7, 'H': 7, 'i': 8, 'I': 8, 'j': 9, 'J': 9, 'k': 10, 'K': 10, 'l': 11, 'L': 11, 'm': 12, 'M': 12, 'n': 13,
                   'N': 13, 'o': 14, 'O': 14, 'p': 15, 'P': 15, 'q': 16, 'Q': 16, 'r': 17, 'R': 17, 's': 18, 'S': 18, 't': 19, 'T': 19, 'u': 20, 'U': 20, 'v': 21, 'V': 21, 'w': 22, 'W': 22, 'x': 23, 'X': 23, 'y': 24, 'Y': 24, 'z': 25, 'Z': 25, }
    if letter in letter_dict:
        return (letter_dict[letter])


def rotate_character(let, rot):

    position = (alphabet_position(let) + rot) % 26
    updated_char = chr(position + 65)
    if let.islower():
        updated_char = updated_char.lower()
    return updated_char


def encrypt(letters, key):
    encrypted = ""
    index = 0
    key_length = len(key)

    for i in letters:
        if i.isalpha():
            encrypted = encrypted + \
                rotate_character(i, alphabet_position(key[index]))
            index = (index + 1) % key_length
        else:
            encrypted = encrypted + i
    return encrypted


def main():
    letters = input("What would you like to encrypt? ")
    key = input("Enter your key: ")

    print(encrypt(letters, key))


if __name__ == "__main__":
    main()
