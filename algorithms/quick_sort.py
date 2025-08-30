def r_quick_sort(data_lst, left, right):
    loc = left
    right_most = right

    if right - left < 1:
        return

    while True:
        while data_lst[loc] < data_lst[right]:
            right -=1

        if right == loc:
            break

        data_lst[loc], data_lst[right] = data_lst[right], data_lst[loc]
        loc = right
        right -= 1
        
        

        while data_lst[loc]>data_lst[left]:
            left +=1

        if left == loc:
            break

        data_lst[loc], data_lst[left] = data_lst[left], data_lst[loc]
        loc = left
        left += 1



    r_quick_sort(data_lst, 0, loc-1)
    r_quick_sort(data_lst, loc+1, right_most)


def quick_sort(data_lst, l, r):
    lst = [(l, r)]

    while lst != []:
        left, right = lst.pop(0)
        right_most = right
        loc = left
        
        while True:
            while data_lst[loc] < data_lst[right]:
                right -=1

            if right == loc:
                break

            data_lst[loc], data_lst[right] = data_lst[right], data_lst[loc]
            loc = right
            right -= 1
            
            while data_lst[loc]>data_lst[left]:
                left +=1

            if left == loc:
                break

            data_lst[loc], data_lst[left] = data_lst[left], data_lst[loc]
            loc = left
            left += 1

        if loc-1 >= 1:
            lst.append((0, loc-1))

        if loc+1 < right_most:
            lst.append((loc+1, right_most))





data = [58, 62, 91, 43, 29, 37, 88, 72, 16, 30]

r_quick_sort(data, 0, 9)

print(data)