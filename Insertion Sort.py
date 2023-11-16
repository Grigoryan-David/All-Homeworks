def insertion_sort(l):

    for i in range(1, len(l)):
        curr_step = l[i]
        j = i - 1
                
        while j >= 0 and curr_step < l[j]:
            l[j + 1] = l[j]
            j = j - 1
        
        l[j + 1] = curr_step

    return data

data = [10, 25, 34, 74, 5, 1, 3, 12]

print(f'Sorted Array in Asc Order: {insertion_sort(data)}')

def insertion_sort_reverse(l):

    for i in range(1, len(l)):
        curr_step = l[i]
        j = i - 1
                
        while j >= 0 and curr_step > l[j]:
            l[j + 1] = l[j]
            j = j - 1
        
        l[j + 1] = curr_step

    return data

data = [10, 25, 34, 74, 5, 1, 3, 12]

print(f'Sorted Array in Desc Order: {insertion_sort_reverse(data)}')