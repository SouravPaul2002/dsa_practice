"""
Question: "Festival Light Budget"

Story:
A town is decorating its streets for a festival. 
There are n types of light strings available, 
each with a cost and a "brightness" score. 
The town council has a total budget of B and wants to buy some combination of light strings — 
any type can be bought multiple times, without limit — 
to maximize total brightness without exceeding the budget.

Find the maximum total brightness achievable.

Input Format:

Line 1: n B
Line 2: n integers, cost of each light type
Line 3: n integers, brightness of each light type

Output Format:

One integer, the maximum total brightness achievable within the budget.

Constraints:

1 ≤ n ≤ 50
1 ≤ B ≤ 1000
1 ≤ cost[i] ≤ 1000
0 ≤ brightness[i] ≤ 1000

Test Cases:

Input:
   3 10
   2 3 5
   3 4 8

Output: 16

Input:
   2 7
   3 4
   4 5

Output: 9

Input:
   1 5
   2
   3

Output: 6

Input:
   2 6
   4 4
   5 5

Output: 5

Input:
   3 0
   1 2 3
   5 5 5

Output: 0

Input:
   2 10
   3 7
   4 10

Output: 14

"""

# brute force approach 

# def func(light_cost, brightness , idx, budget):

#     take= float('-inf')

#     if idx == 0:
#         if light_cost[0] <= budget:
#             return (budget // light_cost[0])* brightness[0]
#         else:
#             return 0

#     notTake= 0 + func( light_cost, brightness, idx -1, budget)

#     if light_cost[idx] <= budget:
#         take= brightness[idx] + func(light_cost, brightness, idx, budget - light_cost[idx])

#     return max(notTake, take)

# n , b = input().split()
# idx= int(n)
# b= int(b)
# light_cost= list(map(int,input().split()))
# brightness= list(map(int,input().split()))

# print(func(light_cost, brightness, idx -1 , b))


# memoization 

# def func(light_cost, brightness , idx, budget, dp):

#     if idx == 0:
#         if light_cost[0] <= budget:
#             return (budget // light_cost[0])* brightness[0]
#         else:
#             return 0

#     take= float('-inf')

#     if dp[idx][budget] != -1 :
#         return dp[idx][budget]

#     notTake= 0 + func( light_cost, brightness, idx -1, budget, dp)

#     if light_cost[idx] <= budget:
#         take= brightness[idx] + func(light_cost, brightness, idx, budget - light_cost[idx], dp)

#     dp[idx][budget]= max(notTake, take)
#     return dp[idx][budget]


# n , b = input().split()
# n=int(n)
# idx= n
# b= int(b)
# light_cost= list(map(int,input().split()))
# brightness= list(map(int,input().split()))
# dp=[[-1]*(b+1) for _ in range(n)]

# print(func(light_cost, brightness, idx -1 , b,dp))


# tabulation 

def func(light_cost, brightness , idx, budget, dp):

    if idx == 0:
        if light_cost[0] <= budget:
            dp[0][0]= (budget // light_cost[0])* brightness[0]
        else:
            dp[0][0]= 0

    take= float('-inf')

    if dp[idx][budget] != -1 :
        return dp[idx][budget]

    notTake= 0 + func( light_cost, brightness, idx -1, budget, dp)

    if light_cost[idx] <= budget:
        take= brightness[idx] + func(light_cost, brightness, idx, budget - light_cost[idx], dp)

    dp[idx][budget]= max(notTake, take)
    return dp[idx][budget]


n , b = input().split()
n=int(n)
idx= n
b= int(b)
light_cost= list(map(int,input().split()))
brightness= list(map(int,input().split()))
dp=[[-1]*(b+1) for _ in range(n)]

print(func(light_cost, brightness, idx -1 , b,dp))