print("Welcome to the anagram checker! It is so good to see you using our site!")
print("Thank you for giving us the opportunity to serve you!!")
first_word = input("Please type the first word that you want the computer to check for anagram (word must be a single word).........").lower()
print(f"The first word is {first_word}!")
second_word = input("Please type the second word that you want the computer to check for anagram (word must be a single word).........").lower()
print(f"The second_word is {second_word}!")
list(first_word)
first_word_list = list(first_word)
print(first_word_list)
list(second_word)
second_word_list = list(second_word)
print (second_word_list)
        
def areAnagram(str1, str2): 
      
    if (len(str1) != len(str2)): 
        return False; 
  
    value = 0; 
  
    for i in range(0,len(str1)): 
        value = value ^ ord(str1[i]); 
        value = value ^ ord(str2[i]); 
  
    return value == 0; 
  
str1 = first_word_list
str2 = second_word_list

if(areAnagram(str1, str2)): 
    print("The two strings are anagram of each other and thank you for using our site!"); 
else: 
    print("The two strings are not anagram of each other and thank you for using our site!"); 