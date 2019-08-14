def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    fullname = fullname.upper()
    fullname = fullname.split()
    initials = ""

    for i in fullname:
        initials = initials + i[0][0]
    return initials


def main():
    fullname = input("What is your full name? ")
    print("The initials for {} are {}.".format(
        fullname, get_initials(fullname)))


if __name__ == "__main__":
    main()
