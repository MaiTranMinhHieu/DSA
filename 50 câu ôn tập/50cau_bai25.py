def largestRectangleArea(heights) -> int:
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, val = stack.pop()
            max_area = max(max_area, val * (i - idx))
            start = idx
        stack.append((start, h))
    return max_area

print(largestRectangleArea([2, 1, 5, 6, 2, 3]))