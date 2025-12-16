#This file is used to practice neetcode problems 


#===============================================
# Score of a String
#===============================================


# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
# Return the score of s.

# Example 1:
# Input: s = "code"

# Output: 24
# Explanation: The ASCII values of the characters in the given string are: 'c' = 99, 'o' = 111, 'd' = 100, and 'e' = 101. The score of s will be: |111 - 99| + |100 - 111| + |101 - 100|.

# Example 2:
# Input: s = "neetcode"

# Output: 65
# Constraints:
# 2 <= s.length <= 100
# s is made up of lowercase English letters.

# Thought process: 
# brute force approach maybe: 
# first step would be figure out how to get the ascii value of the character 
# then iterate through the string and get its value nad the value of the character adjacent to it , then subract their values  
# store that value into a result int variable and print it 

# what is the optimal solution though ?

class Solution:
    def scoreOfString(self, s: str) -> int:
