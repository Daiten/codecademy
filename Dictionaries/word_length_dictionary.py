# Write your word_length_dictionary function here:

def word_length_dictionary(words):
    allwords = []
    sizes = []
    for word in words:
        allwords.append(word)
        sizes.append(len(word))
    zipped = zip(allwords, sizes)

    return (dict(list(zipped)))


# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}