def min4(a,b,c,d):
  min1=min(a,b)
  min2=min(c,d)
  min3=min(min1,min2) 
  return min3

print ('Введите число A:')
A = int(input())
print ('Введите число B:')
B = int(input())
print ('Введите число C:')
C = int(input())
print ('Введите число D:')
D = int(input())
print (min4(A,B,C,D))