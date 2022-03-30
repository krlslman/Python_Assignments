
def is_valid_parantheses(text_str):
  #self.text = text
  text = list(text_str)  # iterasyon işlemlerini daha rahat yapmak için list'e çevirelim
  temp = text  # kopyasını oluşturalım
  flag = True
  i = 0
  if text.count("(")!=text.count(")") or text.count("[")!=text.count("]") or text.count("{")!=text.count("}") :  # parantez sayıları valid değilse;
    flag = False

  else:  # parantez adetleri doğru ise sıraya bakarız;
    while i < len(text):  # her kapanış açılışıyla eşleşip silinir
      if text[i] == "]":
        if temp[temp.index("]")-1]== "[" :
          temp.pop(i)
          temp.pop(i-1)
          i=0
      elif text[i] == "}":
        if temp[temp.index("}")-1]== "{" :
          temp.pop(i)
          temp.pop(i-1)
          i=0
      elif text[i] == ")":
        if temp[temp.index(")")-1] == "(" :
          temp.pop(i)
          temp.pop(i-1)
          i=0
      i += 1 
      if len(temp) == 0  : # çıkış koşulu : eğer item kalmadıysa : eğer sorun yoksa
        break
      #print(temp)  #  print test ************
    if len(temp)>0:  # hatalı parantez(ler) kaldıysa;
      flag = False
  return flag

is_valid_parantheses("({{}}([])[()])" )
