def binary_search(A, key, high, low):
  if low >= high:
    return False
  mid = (low + high) // 2
  if key == A[mid]:
    return True
  elif key > A[mid]:
    return binary_search(A, key, high, mid)
  else:
    return binary_search(A, key, mid, low)

my_list = [15, 5, 62, 45, 82, 76, 94, 51]

print(binary_search(my_list, 1, len(my_list), 0))

def merge_sort(A):
  print(A)
  length = len(A)
  if length > 1:
    mid = length // 2
    L = A[:mid]
    R = A[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0
    print("dzax aj", L, R, sep = " ")
    while i < len(L) and j < len(R):
      if L[i] <= R[j]:
        A[k] = L[i]
        i += 1
      else:
        A[k] = R[j]
        j += 1
      k += 1

    while i < len(L):
      A[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      A[k] = R[j]
      j += 1
      k += 1

    print("havaqac", A)



#merge_sort(l)    


  
