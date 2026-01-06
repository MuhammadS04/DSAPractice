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


# class Solution:
#     def scoreOfString(self, s: str) -> int:
#         sScore = 0
#         for i in range(len(s) - 1):
#            char = s[i]
#            char2 = s[i+1]
#            sScore += (abs(ord(char2)-ord(char)))

#         return sScore
    


# ===============================================
# Contains Duplicate
# ===============================================

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

#brute force: O(n^2) time complexity)
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i + 1,(len(nums))):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
    
    #optimal solution:

# Sorted solution (O(n log n) time complexity due to sorting) 
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 return True
#         return False

# Hash Set Optimal Solution (O(n) time complexity)
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for i in nums:
#             if i in seen: 
#                 return True
#             seen.add(i)
#         return False

# ===============================================
# Valid Anagram
# ==============================================
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         countedS = {}
#         countedT = {}
        
#         for i in range(len(s)):
#             countedS[s[i]] = 1 + countedS.get(s[i],0)
#             countedT[t[i]] = 1 + countedT.get(t[i],0)
#         return countedS == countedT
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            idx1 = ord(s[i]) - ord('a')
            idx2 = ord(t[i]) - ord('a')
            count[idx1] += 1
            count[idx2] -= 1

        for val in count:
            if val != 0:
                return False
        return True


    
if __name__ == "__main__":
    s = "racecar"
    t = "carrace"
    sol = Solution()
    print(sol.isAnagram(s,t))
    exit