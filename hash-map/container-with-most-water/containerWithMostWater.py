import sys

def maxArea(heights: list[int]) -> int:
    left = 0
    right = len(heights) - 1
    maxArea = 0
    while left <= right:
        height = min(heights[right], heights[left])
        length = right - left
        area = height * length 
        maxArea = max(maxArea, area)
        if heights[right] > heights[left]:
            left += 1
        else:
            right -= 1
    return maxArea

if __name__ == "__main__":
  list = numbers = [int(num) for num in sys.argv[1].split(',')]
  print(maxArea(list))