def insertion_sort(data_lst):
    """
    for i in range(1, len(data_lst)):

        while data_lst[i] < data_lst[i-1] and i-1>=0:
            data_lst[i], data_lst[i-1] = data_lst[i-1], data_lst[i]
            i -= 1
    """

    # Actual Insertion Sort

    for i in range(1, len(data_lst)):
        j = i-1
        temp = data_lst[i]

        while 0<=j and temp<data_lst[j]:
            data_lst[j+1] = data_lst[j]

            j-=1

        data_lst[j+1] = temp







    """
    Some new Reverse Sorting

    for i in range(1, len(data_lst)):

        while data_lst[i] < data_lst[i-1] and i-1>=0:
            data_lst[i], data_lst[i-1] = data_lst[i-1], data_lst[i]
            i -= 1
    """

        




# Testing
data = [25, 37, 11, 14, 60, 82, 18, 41]

insertion_sort(data)

print(data)