def decode(s: str) -> str:
    stack, num, temp = [], 0, ""
    for c in s:
        if c in "0123456789":
            num = num * 10 + int(c)
        elif c == "[":
            stack.append((temp, num))
            num = 0
            temp = ""
        elif c == "]":
            string, n = stack.pop()
            temp = string + temp * n
        else:
            temp += c
    return temp
