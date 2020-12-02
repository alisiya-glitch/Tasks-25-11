def my_sum(a,b):
  a+=1
  b-=1
  if b>0:
    return my_sum(a,b)
  else:
    return a

print ('Введите число A:')
A = int(input())
print ('Введите число B:')
B = int(input())
print (my_sum(A,B))