text = "a pattern matching algorithm"
pattern = "rithm"

def BoyerMoore(text, pattern):
    m = len(pattern)
    n = len(text)
    skip = {}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1
    skip.update([(pattern[-1], m), ("*", m)])
    i = 0
    while i <= n - m:
      j = m - 1
      while j >= 0:
        if text[i + j] not in skip.keys():
          i += skip["*"]
          break
        elif text[i + j] != pattern[j]:
          i += skip[text[i + j]]
          break
        j -= 1
      if j == -1:
        return i
    return -1

print(BoyerMoore(text, pattern))