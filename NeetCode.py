#This file is used to practice neetcode problems 

from typing import List
from collections import defaultdict

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
    
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         count = [0] * 26
#         for i in range(len(s)):
#             idx1 = ord(s[i]) - ord('a')
#             idx2 = ord(t[i]) - ord('a')
#             count[idx1] += 1
#             count[idx2] -= 1

#         for val in count:
#             if val != 0:
#                 return False
#         return True

# ===============================================
# Two Sum
# ===============================================

# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.


#two sum problem debuggig.    sorting method , learning enumerate and tuple usage
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         A = []
#         for i, val in enumerate(nums):
#             A.append([val, i])

#         A = sorted(A)
#         i = 0
#         j = len(A) - 1

#         while i < j:
#             currSum = A[i][0] + A[j][0]

#             if currSum == target:
#                 answer = [min(A[i][1],A[j][1]), max(A[i][1],A[j][1])]
#                 return answer
#             elif currSum < target:
#                 i += 1
#             else: 
#                 j -=1
#         return []     

#my answer without looking at the coded solution only the algorithm in english text
# not quite right missing some edge cases but very close to the actual solution ngl

#correct answer two pass O(n)
# class Solution1:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {} 
#         for index, val in enumerate(nums):
#             d[val] = index
        
#         #calculate the complement of curr value
#         for i, val in enumerate(nums):
#             complement = target - nums[i]

#             if complement in d and d[complement] != i:
#                 answer = [min(d[complement], i), max(d[complement], i)]
#                 return answer
#         return []
            
# class Solution2:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#         for i, val in enumerate(nums):
#             complement = target - nums[i]

#             if complement in d:
#                 return [d[complement], i]
#             d[val] = i
                
    
#------------------------------
#Group anagram
#------------------------------
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             sortedS = ''.join(sorted(s))
#             res[sortedS].append(s)
#         return list(res.values())
        
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord('a')] += 1
#             res[tuple(count)].append(s)
#         return list(res.values())
 
class topKSolution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        sorted_count = []
        for num,freq in count.items():
            sorted_count.append([freq,num]) #frequency, values
        sorted_count.sort()

        res = []
        while len(res) < k:
            res.append(sorted_count.pop()[1])
        return res

        

if __name__ == "__main__":
    nums = [1,2,2,2,3,3,3]
    sol = topKSolution1()
    print(sol.topKFrequent(nums,2))
    exit