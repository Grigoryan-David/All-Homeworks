def Split(arr):
  arr_length = len(arr)
  if arr_length > 1:
    mid = arr_length // 2
    L = arr[:mid]
    R = arr[mid:]
  
    Split(L)
    Split(R)

    print(arr)
    l_m = Majority(L)
    r_m = Majority(R)

    if len(L) + len(R) == len(arr):
      if l_m == -1:
        return r_m
      elif r_m == -1:
        return l_m
      else:
        return "No"

def Majority(arr):
  major = len(arr) // 2
  for i in set(arr):
    if arr.count(i) > major:
      return i
  else:
    return -1
    
    

a = [1, 2, 7, 2, 2, 7, 2, 7, 3, 3, 7, 7, 3, 7, 7, 7]

#print(len(a), a.count(7))
print(Split(a))
