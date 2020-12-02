def my_div(n):
       a=0
       for i in range(2, n):
           while n % i == 0:
               a = i
               n //= i
       if n == 1:
               return a
       if n > 1:
           return n

print ('Введите число A:')
A = int(input())
print (my_div(A)) 