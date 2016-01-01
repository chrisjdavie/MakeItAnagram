'''
Solving the hackerrank Make It Anagram puzzle.

https://www.hackerrank.com/challenges/make-it-anagram

----------------------------

Problem Statement

Alice recently started learning about cryptography and found that anagrams are very useful. Two strings are anagrams of each other if they have same character set and same length. For example strings "bacdc" and "dcbac" are anagrams, while strings "bacdc" and "dcbad" are not.

Alice decides on an encryption scheme involving 2 large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. She need your help in finding out this number.

Given two strings (they can be of same or different length) help her in finding out the minimum number of character deletions required to make two strings anagrams. Any characters can be deleted from any of the strings.

Input Format 
Two lines each containing a string.

Constraints 
1 <= Length of A,B <= 10000 
A and B will only consist of lowercase latin letter.

Output Format 
A single integer which is the number of character deletions.

----------------------------

Created on 1 Jan 2016

@author: chris
'''

inputString1 = raw_input().strip()
inputString2 = raw_input().strip()

allChars = set(inputString1).union(inputString2)

deletions = 0
for char in allChars:
    deletions += abs(inputString1.count(char) - inputString2.count(char))

print deletions
