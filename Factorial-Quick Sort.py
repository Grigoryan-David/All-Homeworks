def factorial_loop(n):
  if n < 0:
    raise Exception("n must be positive number")
  elif n == 0:
    return 1
  fac = 1
  for i in range(1, n+1):
    fac *= i
  return fac

def factorial_recursion(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial_recursion(n-1)



def quick_sort(a):
  pivot = a[len(a)//2]
  i = 0
  l = a[i]
  j = len(a) - 1
  r = a[j]
  print(l, r, pivot)
  while l <= pivot:
    i += 1
    l = a[i]
  while r >= pivot:
    j -= 1
    r = a[j]
  a[i], a[j] = a[j], a[i]
  
  print(a)

quick_sort([0, 6, 5, 1, 4])
  
    
    