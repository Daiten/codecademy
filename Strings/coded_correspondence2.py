alphabet = "abcdefghijklmnopqrstuvwxyz"
coded_message = "Great job! Now send Vishal back a message using the same offset. Your message can be anything you want!"


def encode(message):
    encoded_string = ""
    for letter in message:
        index_of_letter = alphabet.find(letter)
        if letter == " ":
            encoded_string += " "
        elif letter == "!":
            encoded_string += "!"
        elif letter == ".":
            encoded_string += "."
        elif letter == "?":
            encoded_string += "?"
        elif index_of_letter in range(11, 26):
            index_of_letter -= 10
            encoded_string += alphabet[index_of_letter]
        else:
            index_of_letter = (index_of_letter - 10) % 26
            encoded_string += alphabet[index_of_letter]

    return encoded_string


print(encode(coded_message))