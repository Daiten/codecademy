# Write your make_spoonerism function here:

def make_spoonerism(word1, word2):
    word1_new = word2[0] + word1[1:]
    word2_new = word1[0] + word2[1:]

    return word1_new + " " + word2_new


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
