'''
Question 2: “Exact Fare Machine”

Story:
A ticket machine accepts n types of coins, and it has an unlimited supply of each type. A passenger must pay exactly X rupees. To keep the machine from jamming, the passenger wants to use the fewest coins possible.

Find the minimum number of coins needed to pay exactly X. If it’s impossible, print -1.

Input Format:

Line 1: n X
Line 2: n integers, the coin values

Output Format:

One integer, the minimum number of coins, or -1.

Constraints:

1 ≤ n ≤ 50
1 ≤ X ≤ 10^4
1 ≤ coin value ≤ 10^4

Test Cases:

Input: 3 6 / 1 3 4 → Output: 2
Input: 1 3 / 2 → Output: -1
Input: 3 11 / 1 2 5 → Output: 3
Input: 1 7 / 7 → Output: 1
Input: 3 14 / 2 5 10 → Output: 3
Input: 2 11 / 3 7 → Output: -1
Input: 4 11 / 1 5 6 9 → Output: 2
'''


def func(idx,arr,val):

    if val == 0:
        return 0

    if val< 0:
        return float('inf')

    if idx < 0:
        return float('inf')

    

    take= 1 + func(idx,arr, val - arr[idx])
    notTake= 0 + func(idx-1,arr,val)

    return min(take,notTake)

n, x= input().split()
n=int(n)
x= int(x)
arr=list(map(int,input().split()))

res= func(n-1,arr,x)
if res == float('inf'):
    print(-1)
else:
    print(res)