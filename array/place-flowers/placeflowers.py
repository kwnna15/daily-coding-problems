def place_flowers(flowerbed: list[int], n: int) -> bool:
    count = 0
    ptr1 = -1
    ptr2 = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            ptr1 = i + 1
            ptr2 = i + 1
        elif (ptr2 - ptr1 == 2) or (len(flowerbed) - 1 == i and ptr2 - ptr1 == 1):
            count += 1
            ptr1 = i - 1
            ptr2 = i
        else:
            ptr2 += 1
    return count >= n
