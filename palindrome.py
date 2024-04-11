# Determine if a word is a palindrome

# A function that writes the word in reverse
def reverse_word(word):
    reversed_word = ""
    # This command is particular to Python which is shorter to reverse the word
    #reversed_word = word [::-1]
    # This bucle reverse the word
    for letter in word:
        reversed_word = letter + reversed_word
    print(reversed_word)

    return reversed_word

# A function that determines if a word is palindrome
def is_palindrome(word):
    return word == reverse_word(word)

# A function that checks each word in a list to determine 
# if a word is palindrome, if all words inside the list return True else return False.
def check_all_palindromes(arr):
    for word in arr:
        if not is_palindrome(word):
            return False
    return True

# Example of use
words = ["radar", "level","comprar"]
print(check_all_palindromes(words))