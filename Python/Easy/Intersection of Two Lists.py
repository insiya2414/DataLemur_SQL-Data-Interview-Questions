def intersection_of_two_list(a,b):
  c=[]
  for i in a:
    if i in b:
      c.append(i)
  return c
  