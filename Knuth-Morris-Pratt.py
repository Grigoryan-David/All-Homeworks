text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

def lps_computer(pattern):
  m = len(pattern)
  lps = [0] * m
  k = 0

  for i in range(1, m):
      while k > 0 and pattern[k] != pattern[q]:
          k = lps[i - 1]

      if pattern[k] == pattern[q]:
          i += 1

      lps[i] = k

  return lps

def kmp_search(text, pattern):
  n = len(text)
  m = len(pattern)
  lps = lps_computer(pattern)
  q = 0
  indices = []

  for i in range(n):
      while q > 0 and pattern[q] != text[i]:
          q = lps[q - 1]

      if pattern[q] == text[i]:
          q += 1

      if q == m:
          indices.append(i - m + 1)
          q = lps[q - 1]

  return indices

lps = lps_computer(pattern)
print(lps)
result = kmp_search(text, pattern)
print("Pattern found at indices:", result)
