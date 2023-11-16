x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0]
n = 0

def split(x, l, n):
    print(x, n)
    if x[0] == 0:
      print(n, l)
      n += l
      return n
    if x[l//2] == 0:
      if l % 2 == 0:
        n += l / 2
      else:
        n += l//2 + 1
      x = x[:(l//2)]
      return split(x, len(x), n)
    else:
      x = x[l//2 + 1:]
      print(x)
      return split(x, len(x), n)

print(split(x, len(x), n))   