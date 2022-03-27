def koralius_survivor(a,b):
  list_init = list(range(1,a+1))
  delete_index = b-1
  next_start = 0
  print("Initial list : {:>39}".format(str(list_init)))
  for i in range(a): 
    temp_list = list_init[next_start:]
    temp_list.extend(list_init)
    if i< len(list_init)-1: # to prevent range error at the last step
      next_start = list_init.index(temp_list[delete_index]) # starting index of next temporary list
    list_init.remove(temp_list[delete_index]) # drop it from main list
    print(temp_list[delete_index]," is counted out. New list is :",list_init,"\n")
    if len(list_init)==1: 
      print("---->>>>  ",list_init[0], " is the survivor!   <<<<----")
      break

koralius_survivor(7,3)
