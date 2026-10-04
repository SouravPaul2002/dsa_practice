'''
Question: "Range Sum Query — Prefix Sum"

Story:

A system stores a list of integer values.

You are given two indices, left and right, and need to calculate the total sum of all elements between these two indices, including both left and right.

Since the system may need to answer range-sum queries efficiently, use a Prefix Sum Array to preprocess the values.

Find the sum of elements from index left to index right.

Input Format:

Line 1: n

Line 2: n integers representing the array

Line 3: left — starting index of the range

Line 4: right — ending index of the range

Output Format:

One integer representing the sum of elements from index left to right (inclusive).

Constraints:

1 ≤ n ≤ 10^5

-10^9 ≤ array element ≤ 10^9

0 ≤ left ≤ right < n

Test Cases:

Input:

7
2 1 4 3 2 8 11
2
5

Output:
17


Input:

5
10 20 30 40 50
0
2

Output:
60


Input:

6
5 8 2 10 3 7
1
4

Output:
23


Input:

1
42
0
0

Output:
42


Input:

8
1 2 3 4 5 6 7 8
3
7

Output:
30


Input:

5
-5 10 -3 7 2
1
3

Output:
14


Expected Approach:

Build a prefix sum array where:

prefix[i] = sum of elements from index 0 to i

Then calculate the range sum in O(1) using:

prefix[right] - prefix[left - 1]

If left = 0, the range sum is simply prefix[right].

Overall Time Complexity: O(n)

Range Query Time Complexity: O(1)

Space Complexity: O(n)
'''



arr= list(map(int,input().split())) # 2 1 4 3 2 8 11
left=int(input()) # index: 2 -> 4
right=int(input()) # index: 5 -> 8
pre_sum=[0] # 2 3 7 10 12 20 31

temp=0
for num in arr:
    temp+=num
    pre_sum.append(temp)
print(pre_sum[right]- pre_sum[left-1])