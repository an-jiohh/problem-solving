s = "A man, a plan, a canal: Panama"
strs = []
for char in s:
  if char.isalnum():
      strs.append(char.lower())

while len(strs) > 1:
    if strs.pop(0) != strs.pop():
        return False

return True