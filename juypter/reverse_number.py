#Given a number N, print reverse of number N.

n = 988
rev = 0

while(n>0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
print(rev)    
    