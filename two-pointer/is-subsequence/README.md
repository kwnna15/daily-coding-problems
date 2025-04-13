# 392. Is Subsequence

## Description
See https://leetcode.com/problems/string-compression/description/

## Problem
Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

## Example 1

```
Input: s = "abc", t = "ahbgdc"
Output: true
```

## Example 2

```
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
```

## Example 3

```
Input: s = "axc", t = "ahbgdc"
Output: false
```

## Constraints

```
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
```

**Follow up:** Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?