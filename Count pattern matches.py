text = "abbababacacacabacab"
p = "acabhpt"

def is_prefix(text, p):
  return all(p[i] == text[i] for i in range(len(p)))

def is_suffix(text, p):
  len_text = len(text)
  len_p = len(p)
  return all(p[i] == text[len_text - len_p + i] for i in range(len(p)))

def sigma(text, p):
  print(p)
  if is_suffix(text, p):
    return len(p)
  else:
    return sigma(text, p[:-1])


print(sigma(text, p))
