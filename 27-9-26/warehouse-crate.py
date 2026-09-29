"""
Question: "Warehouse Crate Stacking"

Story:
A warehouse has n crates arranged in a row, each with a certain weight. 
A forklift operator wants to select some crates to load onto a truck to maximize total weight, 
but there's a rule: he can never select more than 2 crates in a row, 
AND additionally, the very first and very last crate in the row are considered adjacent 
to each other (the row is arranged in a circular loop inside the warehouse, 
since it wraps around a support pillar).
Find the maximum total weight the operator can load.

Input Format:

Line 1: n
Line 2: n integers — weight of each crate

Output Format:

Maximum total weight that can be loaded.

Constraints:

1 ≤ n ≤ 1000
0 ≤ weight[i] ≤ 10^4

Test Cases:

Input:
   4
   3 3 3 3

Output: 6

Input:
   5
   1 2 3 4 5

Output: 11

Input:
   1
   7

Output: 7

Input:
   2
   10 20

Output: 30

Input:
   6
   5 1 1 5 1 1

Output: 12

Input:
   3
   4 4 4

Output: 8

"""

def func(arr,n):
    if n==1:
        return arr[0]
    if n==2:
        return arr[0] + arr[1]


    def mainFunc(arr):
        m= len(arr)
        dp=[-1]*m
        dp[0]= arr[0]
        dp[1]= arr[0]+ arr[1]
        for i in range(2,m):
            notTake= dp[i-1]
            takeOne= arr[i]+dp[i-2]
            if i > 2:
                takeTwo= arr[i] + arr[i-1] + dp[i-3]
            dp[i]=max(notTake,takeOne, takeTwo)
        return dp[m-1]

    notTakeFirst=mainFunc(arr[1:])
    notTakeLast=mainFunc(arr[:-1])

    return max(notTakeFirst,notTakeLast)


n= int(input())
arr= list(map(int,input().split()))

print(func(arr,n))