from helpers import alphabet_position, rotate_character
 
def encrypt(letters, rot):
    encrypted = ""
    for i in letters:
        if i.isalpha():
            encrypted = encrypted + rotate_character(i, rot)
        else:
            encrypted = encrypted + i
    return encrypted


def main():
    letters = input("What would you like to encrpt? ")
    rot = int(input("What is the rotation? "))

    print(encrypt(letters, rot))


if __name__ == "__main__":
    main()
