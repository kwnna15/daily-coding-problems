import sys


def max_average(nums: list[int], k: int) -> float:
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum / k


if __name__ == "__main__":
    nums = numbers = [int(num) for num in sys.argv[1].split(",")]
    k = int(sys.argv[2])
    print(max_average(nums, k))
