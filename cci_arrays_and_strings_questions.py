"""
1.1) Implement an algorithm to determine if a string has all unique characters.

"""
def is_unique(str):
    # Brute Force. Time Complexity = O(N^3), Space Complexity = O(1)
    for current_letter in range(0, len(str)):
        for next_letter in range(current_letter+1, len(str)):
            if str[current_letter] == str[next_letter]:
                return False
    return True
    
    
    # Optimal Algorithm. Time Complexity = O(N), Space Complexity = O(c)
    num_of_characters = 128
    
    #String cannot be unique if it is large than the character set.
    if len(str) > num_of_characters: 
        return False
    
    characters = [False] * num_of_characters
    
    for i in range(0, len(str)):
        current_char = ord(str[i])
        if characters[current_char]: #Already appeared in the string.
            return False
        else:
            characters[current_char] = True
    return True
   
         
"""
1.2) Given two strings, write a method to decide if one is a permutation of the
     other.
"""
def is_permutation(str1, str2):
    #Brute Force. Time Complexity = O(n^5), Space Complexity = O(N)
    used_letters = []
    for current_letter in range(0, len(str1)):
        for next_letter in range(0, len(str2)):
            if str1[current_letter] == str2[next_letter]:
                for i in range(0, len(used_letters)):
                    if used_letters[i] == next_letter:
                        return False
                used_letters.append(next_letter)
        break
    return True  
         
    #Optimal Algorithm. Time Complexity = O(N), Space Complexity = (N)
    if len(str1) != len(str2):
        return False
    
    str1 = sorted(str1)
    str2 = sorted(str2)
    
    for character in range(0, len(str1)):
        if str1[character] != str2[character]:
            return False
    return True
    

"""
1.3) Write a method to replace all spaces in a string with '%20'. You may 
     assume that the string has sufficient space at the end to hold the 
     additional characters, and that you are given the "true" length of the 
     string.  
     
     EXAMPLE
     Input:     "Mr John Smith    ", 13
     Output:    "Mr%20John%20Smith"
"""
def urlify(string, integer):
    # Time Complexity = O(N), Space Complexity = O(N)
    for character in range(0, integer):
        if string[character] == " ":
            string = string[:character] + "%20" + string[character+1: integer]
    return string
    

"""
1.4) Given a string, write a function to check if it is a permutation of a 
     palindrome. A palindrome is a word or phrase that is the same forwards and
     backwards. A permutation is a rearrangement of letters. The palindrome 
     does not need to be limited to just dictionary words.
"""
def is_palindrone_permutation(str):
    #Time Complexity = O(N), Space Complexity = O(N)
    
    str = str.lower()
    frequencies = {character: 0 for character in str}
    
    for character in str:
        if character == " ":    
            continue    #Ignore white space
        else:
            frequencies[character] += 1
    
    odd = False     #There can only be one letter whose frequency value is odd.
    
    for key in frequencies:
        if frequencies[key] % 2 == 1:
            if odd:
                return False
            else:
                odd = True
    return True       
        
     
"""
1.5) There are three types of edits that can be performed on strings: insert a 
     character, remove a character, or replace a character. Given two strings, 
     write a function to check if they are one edit (or zero edits) away.
     
     EXAMPLE
     pale, ple -> true
     pales, pale -> true
     pale, bale -> true
     pale, bake -> false  
"""
def one_away(str1, str2):
    #Time Complexity = O(N), Space Complexity = O(N)
    if len(str2) > len(str1):
        temp = str1
        str1 = str2
        str2 = temp
    
    string1 = build_frequency_dictionary(str1)
    string2 = build_frequency_dictionary(str2)
    
    difference = 0
    for key in string1:
        if not key in string2:
            difference += string1[key]
        else:
            difference += abs(string1[key] - string2[key])
        
        if difference > 1:
            return False
    return True

def build_frequency_dictionary(str):
    freq = {}
    for character in str:
        if character in freq:
            freq[character] += 1
        else:
            freq[character] = 1
    return freq

    
"""
1.6) Implement a method to perform basic string compression using the counts
     of repeated characters. For example, the string aabcccccaaa would become 
     a2blc5a3. If the "compressed" string would not become smaller than the 
     original string, your method should return the original string. You can 
     assume the string has only uppercase and lowercase letters (a - z).
"""
def string_compression(str1):
    #Time Complexity = O(N), Space Complexity = O(N) 
    #TODO -> fix aabbccccaaa should be a2b1c5a3 NOT a5b1c5
    frequencies = {}
    for character in str1:
        if character in frequencies:
            frequencies[character] += 1
        else:
            frequencies[character] = 1
           
    greater_than_3 = False
    compressed_string = ""
   
    for key in frequencies:
        if frequencies[key] >= 3:
            greater_than_3 = True
        compressed_string = compressed_string + str(key) + str(frequencies[key])
    
    if greater_than_3:
        return compressed_string
    else:
        return str1
        
    
"""
1.7) Given an image represented by an NxN matrix, where each pixel in the image
     is 4 bytes, write a method to rotate the image by 90 degrees. Can you do 
     this in place?
"""
def rotate_matrix(matrix):
    #Time Comlexity = O(N^2), Space Complexity = O(N)
    #TODO: This can be done in O(1) space.
    new_matrix = []
    for col in range(0, len(matrix)):
        new_row = []
        for row in range(len(matrix)-1, -1, -1):
            new_row.append(matrix[row][col])
        new_matrix.append(new_row)
    print(new_matrix)




"""
1.8) Write an algorithm such that if an element in an MxN matrix is 0, its 
     entire row and column are set to 0.
"""
def zero_matrix(matrix):
    #Time Complexity = O(NxM), Space Comlexity = O(N)
    #TODO: This can be done in O(1) space.
    zero_indices = []
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == 0:
                matrix[row] = [0] * len(matrix[row])
                zero_indices.append(col)
    
    for row in range(0, len(matrix)):
        for index in zero_indices:
            matrix[row][index] = 0
            
    print(matrix)





"""
1.9) Assume you have a method isSubstring which checks if one word is a substring
     of another. Given two strings, sl and s2, write code to check if s2 is a 
     rotation of sl using only one call to isSubstring (e.g., "waterbottle" is 
     a rotation of"erbottlewat").
"""
def is_rotation(s1, s2):
    #Time Complexity = O(N), Space Complexity = O(N)
    indices = []
    for i in range(0, len(s1)):
        if s1[i] == s2[0]:
            indices.append(i)
    
    for element in indices:
        j = 1
        
        for  i in range(element + 1, len(s1)):
            if s1[i] == s2[j]:
                j += 1
            else:
                return False
     
        if True:
            return True
        else: 
            return False