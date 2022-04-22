'''******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

******************************************************************************'''

#Write a program to print the reverse of the given string.

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
    
s = "abcdefghijklmnopqrstuvwxyz"
print("The original string is : ", end="")
print(s)

print("The reversed string (using loops) is :", end="")
print(reverse(s))
    