def clean_it(l):
  print(id(l))
  l=[]
  print(id(l))

my_list=[1,2,3,4]
clean_it(my_list)
print(id(my_list))
print(my_list)