# https://www.codechef.com/wiki/tutorial-dynamic-programming


def get_min_steps(n):
    def get_steps(n, memo):
        if n == 1:
            return 0
        if memo[n] != -1:
            return memo[n]
        steps = 1 +  get_steps(n-1, memo)
        if n % 2 ==0:
            steps = min(steps, 1 + get_steps(n // 2, memo))
        if n % 3 == 0:
            steps = min(steps, 1 +  get_steps(n //3, memo))
        memo[n] = steps
        return steps
    memo = [-1] * (n+1)
    return get_steps(n, memo)

from queue import Queue
def get_min_steps_bm(n):
    steps_dp = [0] * (n+1) #[0,0,1,1,2,3,2,3]
    steps_dp[2] = 1
    steps_dp[3] = 1

    for curr in range(4, n +1): # 4
        steps = 1 +  steps_dp[curr-1] # 2
        if curr % 2 ==0:
            steps = min(steps, 1 +  steps_dp[curr//2])#2
        if curr % 3 == 0:
            steps = min(steps, 1 + steps_dp[curr//3])
        steps_dp[curr] = steps
    return steps_dp[n]

# for i in range(1, 100):
print(get_min_steps_bm(10000000))
    # rec =  get_min_steps(i)
    # if  dp!=rec:
    #     print(f"you fucked up {i}: dp {dp} rec {rec}")
