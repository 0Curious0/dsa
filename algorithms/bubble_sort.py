def bubble_sort(data_lst):
    for i in range(len(data_lst)-1):
        for j in range(len(data_lst)-i-1):
            if data_lst[j] > data_lst[j+1]:
                data_lst[j], data_lst[j+1] = data_lst[j+1], data_lst[j]

def modified_bubble_sort(data_lst):
    # for i in range(len(data_lst)-1):
    #     temp = data_lst.copy()

    #     for j in range(len(data_lst)-i-1):
    #         if data_lst[j] > data_lst[j+1]:
    #             data_lst[j], data_lst[j+1] = data_lst[j+1], data_lst[j]

    #     if data_lst == temp:
    #         return

    # OR

    flag = False

    for i in range(len(data_lst)-1):
        flag = False

        for j in range(len(data_lst)-i-1):
            if data_lst[j] > data_lst[j+1]:
                data_lst[j], data_lst[j+1] = data_lst[j+1], data_lst[j]
                flag = True

        if not flag:
            return
    





# Testing

data = [34, 67, 12, 89, 25, 50]

modified_bubble_sort(data)

print(data)