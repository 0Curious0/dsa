def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    
    else:
        pivot = lst[0]

        lesser = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i>= pivot]

        return quick_sort(lesser) + [pivot] + quick_sort(greater)
    



data = [53, 11, 72, 68, 41, 25, 18, 37, 44, 80]

data = quick_sort(data)

print(data)