coded_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
coded_message2 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
hard_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
alphabet = "abcdefghijklmnopqrstuvwxyz"


def decoder(message, offset):
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
        elif letter == "'":
            decoded_string += "'"
        elif index_of_letter in range(0, 26 - offset):
            index_of_letter += offset
            decoded_string += alphabet[index_of_letter]
        else:
            index_of_letter = (index_of_letter + offset) % 26
            decoded_string += alphabet[index_of_letter]

    return decoded_string


print(decoder(coded_message, 10))
print(decoder(coded_message2, 14))

for i in range(0, 26):
    print(decoder(hard_message, i))

print(decoder(coded_message, 10))
print(decoder(coded_message2, 14))