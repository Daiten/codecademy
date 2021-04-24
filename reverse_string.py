# Write your reverse_string function here:

def reverse_string(word):
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print
