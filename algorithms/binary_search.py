def binary_search(lst, item):
    mid = (0 + len(lst)-1)//2

    if len(lst) > 1:
        if lst[mid] == item:
            return mid
        
        elif lst[mid] > item:
            return binary_search(lst[0:mid], item)

        else:
            return binary_search(lst[mid+1:], item)

    return None




data = [35, 40, 29, 18, 90, 87, 62, 53, 61, 59]

data.sort()

print(data)

print(binary_search(data, 29))