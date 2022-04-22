#Given an array of numbers, arrange them in a way that it forms the largest value.

for itertools import permutations
def largest(1):
    lst = []
    for i in permutations(1,len(1)):
        lst.append(''.join(map(str,i)))
    return max(lst)
    
print(largest([54, 546, 548, 60]))    
