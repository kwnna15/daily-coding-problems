import sys

def findMaxAverage(nums: list[int], k: int) -> float:
    currSum = sum(nums[:k])
    maxSum = currSum
    for i in range(k, len(nums)):
        currSum += nums[i] - nums[i - k]
        maxSum = max(maxSum, currSum)
    return maxSum / k

if __name__ == "__main__":
  nums = numbers = [int(num) for num in sys.argv[1].split(',')]
  k = int(sys.argv[2])
  print(findMaxAverage(nums, k))