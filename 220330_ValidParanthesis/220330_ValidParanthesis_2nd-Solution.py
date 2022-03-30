word = "{}{[()[]]}([])" 
while True :
  if "()" in word or "[]" in word or "{}" in word :
    word = "".join(word.split("[]"))
    word = "".join(word.split("()"))
    word = "".join(word.split("{}"))
  else : 
    break
print(not word)
