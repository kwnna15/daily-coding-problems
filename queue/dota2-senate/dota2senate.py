from collections import deque


def predict(senate: str) -> str:
    radiant = deque()
    dire = deque()
    n = len(senate)
    for i in range(n):
        if senate[i] == "R":
            radiant.append(i)
        else:
            dire.append(i)
    while len(radiant) != 0 and len(dire) != 0:
        r = radiant.popleft()
        d = dire.popleft()
        n += 1
        if r < d:
            radiant.append(n)
        else:
            dire.append(n)
    if len(radiant) > 0:
        return "Radiant"
    return "Dire"
