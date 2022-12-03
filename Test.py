def avg(l):
  avg = sum(l)/len(l) if (len(l) != 0) else 0
  print("the average of your numbers is: " +str(avg)+ ".")
  # or
  if (len(l) !=0):
    avg = sum(l)/len(l)
  else:
    avg = 0
  print("the average of your numbers is: " +str(avg)+ ".")
