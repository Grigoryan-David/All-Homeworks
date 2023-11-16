def hanoi_tower(n, start, end, alt):
  if n != 0:
    hanoi_tower(n-1, start, alt, end)
    print(n, start, end)
    hanoi_tower(n-1, alt, end, start)


hanoi_tower(5, "1", "3", "2")
