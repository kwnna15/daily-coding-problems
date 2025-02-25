def remove(s: str) -> str:
    stack = []
    for c in s:
        if c != "*":
            stack.append(c)
        else:
            stack.pop()
    return "".join(stack)
