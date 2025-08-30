def selection_sort(data_lst):
    # for i in range(len(data_lst)-1):

    #     for j in range(i+1, len(data_lst)):
    #         if data_lst[i] > data_lst[j]:
    #             data_lst[i], data_lst[j] = data_lst[j], data_lst[i]

    # OR

    # Without doing multiple swapping per loop

    for i in range(len(data_lst)-1):
        min = i

        for j in range(i+1, len(data_lst)):
            if data_lst[min] > data_lst[j]:
                min = j

        data_lst[i], data_lst[min] = data_lst[min], data_lst[i]




data = [64, 35, 89, 21, 72, 13]

selection_sort(data)

print(data)