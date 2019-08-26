from helpers import alphabet_position, rotate_character

def encrypt(letters, key):

    encrypted = ""
    index = 0
    key_length = len(key)
    for i in letters:
        if i.isalpha():
            encrypted = encrypted + rotate_character(i, alphabet_position(key[index]))
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
