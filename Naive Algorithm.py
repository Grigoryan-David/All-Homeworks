text  = "aabacvderjeifjnfsgfjnvdbbxjhajxgfjncbnmb"
pattern = "fjn"

for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
        print(i)
    else:
        continue