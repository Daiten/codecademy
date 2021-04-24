coded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
alphabet = "abcdefghijklmnopqrstuvwxyz"


def decode(message):
    decoded_string = ""
    for letter in message:
        index_of_letter = alphabet.find(letter)
        if letter == " ":
            decoded_string += " "
        elif letter == "!":
            decoded_string += "!"
        elif letter == ".":
            decoded_string += "."
        elif letter == "?":
            decoded_string += "?"
        elif index_of_letter in range(0, 16):
            index_of_letter += 10
            decoded_string += alphabet[index_of_letter]
        else:
            index_of_letter = (index_of_letter + 10) % 26
            decoded_string += alphabet[index_of_letter]

    return decoded_string


decoded_message = decode(coded_message)
print(decoded_message)
