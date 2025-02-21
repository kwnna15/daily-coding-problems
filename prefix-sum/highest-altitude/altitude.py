def max_altitude(gain: list[int]) -> int:
    max_alt, curr = 0, 0
    for i in gain:
        curr += i
        max_alt = max(max_alt, curr)
    return max_alt
