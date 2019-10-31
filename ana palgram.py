print("Welcome to the anagram checker! It is so good to see you using our site!")
print("Thank you for giving us the opportunity to serve you!!")

first_word = input("Please type the first word that you want the computer to check for anagram (word must be a single word).........").lower()
print(f"The first word is {first_word}!")

second_word = input("Please type the second word that you want the computer to check for anagram (word must be a single word).........").lower()
print(f"The second_word is {second_word}!")

list(first_word)
first_word_list = list(first_word)
first_word_list.sort()
print(first_word_list)

list(second_word)
second_word_list = list(second_word)
second_word_list.sort()
print(second_word_list)

fs = first_word_list
sw = second_word_list

def areAnagram(fs, sw): 

    if (fs) == (sw): 
        return True 
    
    else:
        return False

def arePalindrome(first_word_list):

    if (first_word == first_word[::-1]):
        return True
    
    else:
        return False

def main():

    if(areAnagram(fs, sw)): 
        print("The two words are anagram of each other!") 
    else: 
        print("The two words are not anagram of each other!")

    if(arePalindrome(fs)):
        print("The first word is a palindrome!")
    else: 
        print("The first word is not a palindrome!") 

    if(arePalindrome(sw)):
        print("The second word is a palindrome and thank you for using our site!")
    else: 
        print("The second word is not a palindrome and thank you for using our site!")
    
main()

