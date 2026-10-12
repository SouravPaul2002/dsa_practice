"""
Question 1: “Conveyor Belt Scanner”

Story:
A factory conveyor belt carries n items in a row, 
and each item has a product code written as a lowercase letter. 
A quality inspector watches a continuous stretch of items and 
gets confused if the same code appears twice in his view.
Find the length of the longest continuous stretch of items in which no code repeats.

Input Format:

Line 1: n
Line 2: a string of n lowercase letters

Output Format:

One integer, the length of the longest stretch with no repeated code.

Constraints:

1 ≤ n ≤ 10^5

Test Cases:

Input: 8 / abcabcbb → Output: 3
Input: 5 / bbbbb → Output: 1
Input: 6 / pwwkew → Output: 3
Input: 1 / a → Output: 1
Input: 6 / abcdef → Output: 6
Input: 4 / dvdf → Output: 3
Input: 4 / abba → Output: 2

"""

def func(arr):
    n=len(arr)
    left=0
    right=0
    maxi=0
    seen={}

    while left < n and right < n:
        if arr[right] not in seen:
            seen[arr[right]]=right
        else:
            left=max(left, seen[arr[right]] +1)
            
            seen[arr[right]]=right
        maxi=max(maxi,right - left +1)
        right+=1
    return maxi

n = int(input())
strng=input()

if len(strng)!=n:
    print("Wrong Input!!")

arr=[]
for ch in strng:
    arr.append(ch)

print(func(arr))
