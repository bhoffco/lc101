
def alphabet_position(letter):

    letter_dict = {'a': 0, 'A': 0, 'b': 1, 'B': 1, 'c': 2, 'C': 2, 'd': 3, 'D': 3, 'e': 4, 'E': 4, 'f': 5, 'F': 5, 'g': 6, 'G': 6, 'h': 7, 'H': 7, 'i': 8, 'I': 8, 'j': 9, 'J': 9, 'k': 10, 'K': 10, 'l': 11, 'L': 11, 'm': 12, 'M': 12, 'n': 13,
                   'N': 13, 'o': 14, 'O': 14, 'p': 15, 'P': 15, 'q': 16, 'Q': 16, 'r': 17, 'R': 17, 's': 18, 'S': 18, 't': 19, 'T': 19, 'u': 20, 'U': 20, 'v': 21, 'V': 21, 'w': 22, 'W': 22, 'x': 23, 'X': 23, 'y': 24, 'Y': 24, 'z': 25, 'Z': 25, }
    if letter in letter_dict:
        return (letter_dict[letter])


def pos_to_char(position_number, upper_case):
    character = chr(position_number + 65)
    if upper_case:
        return character
    else:
        return character.lower()


def rotate_character(char, rot):

    if not(char.isalpha()):
        return char

    new_position = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return pos_to_char(new_position, True)
    else:
        return pos_to_char(new_position, False)


def encrypt(letters, rot):
    encrypted = ""
    for i in list(letters):
        encrypted = encrypted + rotate_character(i, rot)
    return encrypted


def main():
    letters = input("What would you like to encrypt? ")
    rot = int(input("How much rotation would you like? "))
    print(encrypt(letters, rot))


if __name__ == "__main__":
    main()
