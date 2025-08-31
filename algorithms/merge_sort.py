def merge_sort(data_lst):
    if len(data_lst) > 1:
        right = len(data_lst) - 1
        left = 0

        mid = (left + right) // 2

        left_sub_list = data_lst[left : mid + 1]
        right_sub_list = data_lst[mid + 1 : right + 1]

        sorted_left_sub = merge_sort(left_sub_list)
        sorted_right_sub = merge_sort(right_sub_list)
        

    
        for i in sorted_right_sub:
            j = len(sorted_left_sub) - 1

            sorted_left_sub.append(0)

            while j>=0 and sorted_left_sub[j]>i:
                sorted_left_sub[j+1] = sorted_left_sub[j]

                j -= 1

            sorted_left_sub[j+1] = i

        return sorted_left_sub
        

    return data_lst


#better merge sort
def better_merge_sort(data_lst):
    if len(data_lst) > 1:
        mid = len(data_lst) // 2

        left = data_lst[: mid]
        right = data_lst[mid :]

        better_merge_sort(left)
        better_merge_sort(right)

        i=j=k= 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data_lst[k] = left[i]
                i += 1

            else:
                data_lst[k] = right[j]
                j += 1
        
            k += 1

        while i < len(left):
            data_lst[k] = left[i]
            i += 1
            k += 1
    
        while j < len(right):
            data_lst[k] = right[j]
            j += 1
            k += 1
                    



data = [75, 29, 83, 42, 16, 90, 56, 34, 20, 71, 88, 92, 7]

# data = merge_sort(data)

better_merge_sort(data)

print(data)