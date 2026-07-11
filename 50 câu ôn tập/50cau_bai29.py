from collections import deque

def maxSlidingWindow(nums, k: int):
    q, res = deque(), []
    for i, num in enumerate(nums):
        while q and q[0] < i - k + 1: 
            q.popleft()
        while q and nums[q[-1]] < num: 
            q.pop()
        q.append(i)
        if i >= k - 1: 
            res.append(nums[q[0]])
    return res

print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))