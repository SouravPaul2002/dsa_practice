"""
Question: "Gate Log Analysis"

Story:
A company's main gate has a sensor that records one value every minute for n minutes: 
1 if a person entered during that minute, and 0 if a person exited. 
The security head wants to find the longest continuous period (consecutive minutes) 
in which the number of entries was exactly equal to the number of exits.

Find the length of that longest period. If no such period exists, print 0.

Input Format:

Line 1: n
Line 2: n integers (each either 0 or 1)

Output Format:

One integer, the length of the longest valid period.

Constraints:

1 ≤ n ≤ 10^5
Each value is 0 or 1

Test Cases:

Input:
   6
   1 0 1 1 0 0

Output: 6

Input:
   5
   1 1 1 0 0

Output: 4

Input:
   4
   1 1 1 1

Output: 0

Input:
   1
   0

Output: 0

Input:
   8
   0 0 1 0 1 1 0 0

Output: 6

Input:
   7
   1 0 0 0 1 1 1

Output: 6

"""

n= int(input())
arr= list(map(int,input().split()))

seen={0: -1}

prefix_sum= 0
max_len=0

for i in range(n):
    if arr[i] == 0:
        prefix_sum+= -1
    else:
        prefix_sum+= 1

    if prefix_sum not in seen:
        seen[prefix_sum] = i
    else:
        max_len= max(max_len,(i- seen[prefix_sum]))
print(max_len) 