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
# then iterate through the string and get the first value (i) ascii and the ascii of the character (i + 1) adjacent to it 
# then get the absolute difference of those two values and put them in a sum variable
# now iterate to the next position and repeat this for i and the i + 1 character 
# store that value into a result int variable and print it 

# what is the optimal solution though ?

#brute force implementation 
class Solution:
    def scoreOfString(self, s: str) -> int:
        sScore = 0
        for i in range(len(s) - 1):
           char = s[i]
           char2 = s[i+1]
           sScore += (abs(ord(char2)-ord(char)))

        return sScore