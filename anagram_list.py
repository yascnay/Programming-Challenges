# Determine if two words are anagrams using lists
import string

def isanagram(word1,word2):
    # Convert words to lowercase
    word1= word1.lower()
    word2= word2.lower()

    # Check that the words are the same length
    if len(word1)!=len(word2):
        return False
    
    # Create lists to count the letters in each word
    count1 = []
    count2 = []
    
    for letter in word1:
        count1.append(letter)
    
  
    for letter in word2:
        count2.append(letter)
 
    return sorted(count1)==sorted(count2)


# Example of use
word1 = "Listen"
word2 = "Silent"
if isanagram(word1, word2):
    print(f"'{word1}' y '{word2}' son anagramas.")
else:
    print(f"'{word1}' y '{word2}' no son anagramas.")