text = "a pattern matching almithm"
pattern =               "mithm"

def BoyerMoore(text, pattern):
    m = len(pattern)
    n = len(text)
    skip = {}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1
    if pattern[-1] in pattern[:-1]:
      skip.update([("*", m)])
    else:
      skip.update([(pattern[-1], m), ("*", m)])
    i = 0
    while i <= n - m:
      j = m - 1
      while j >= 0:
        print(text[i+j], pattern[j])
        if text[i + j] not in skip.keys():
          i += skip["*"] - (m-1-j)
          break
        elif text[i + j] != pattern[j]:
          i += skip[text[i + j]]
          break
        j -= 1
      if j == -1:
        return i
    return -1

print(BoyerMoore(text, pattern))
