#Given a number, check whether it is a prime number or not.

num = 3

if num > 1:
    for i in range(2,int(num/2)+1):
        if (num % i )== 0:
            print(num,'is not a prime number')
            break
    else:
        print(num,'is a prime number')
        
else:
    print(num,'is not a prime number')