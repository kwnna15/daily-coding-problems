import sys


def move_zeroes(nums: list[int]) -> None:
    left = 0
    for right in range(0, len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
    return nums


if __name__ == "__main__":
    nums = list(map(int, sys.argv[1].split(",")))
    print(move_zeroes(nums))
