import sys


def max_area(heights: list[int]) -> int:
    left = 0
    right = len(heights) - 1
    max_area = 0
    while left <= right:
        height = min(heights[right], heights[left])
        length = right - left
        area = height * length
        max_area = max(max_area, area)
        if heights[right] > heights[left]:
            left += 1
        else:
            right -= 1
    return max_area


if __name__ == "__main__":
    list = numbers = [int(num) for num in sys.argv[1].split(",")]
    print(max_area(list))
