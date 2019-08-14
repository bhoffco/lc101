

def rotate():

    letter = "Z"

    rot = 10

    adjust = 97 if letter.islower() else 65

    return chr((ord(letter) + rot - adjust) % 26 + adjust)


print(rotate())

index = 2

key_length = 4

index = (index + 1) % key_length

print(index)
