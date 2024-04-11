# Determine if two words are anagrams using dictionary
import string

def isanagram(word1,word2):
    # Convert words to lowercase
    word1= word1.lower()
    word2= word2.lower()

    # Check that the words are the same length
    if len(word1)!=len(word2):
        return False
    
    # Create dictionaries to count the letters in each word
    count1 = {}
    count2 = {}
    
    for letter in word1:
        count1[letter] = count1.get(letter, 0) + 1
    
   
    for letter in word2:
        count2[letter] = count2.get(letter, 0) + 1

    return count1==count2


# Example of use
word1 = "Secure"
word2 = "Rescue"
if isanagram(word1, word2):
    print(f"'{word1}' y '{word2}' son anagramas.")
else:
    print(f"'{word1}' y '{word2}' no son anagramas.")