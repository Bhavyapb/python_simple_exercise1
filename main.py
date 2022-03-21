num =1
while(num<51):
  if(num%3==0):
    print("Divisible by 3")
  elif(num%7==0):
    print("Divisible by 7")
  elif(num%3==0 and num%7==0):
    print("Divisible by both 3 and 7")
  else:
    print(num)
  num+=1