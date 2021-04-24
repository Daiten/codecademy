# Write your every_other_letter function here:

def every_other_letter(word):
    counter = 2
    new_word = ""
    for letter in word:
        if counter % 2 == 0:
            new_word += letter
            counter += 1
        else:
            counter += 1
            continue
    return new_word


# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print