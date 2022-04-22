#Given an array of numbers, find the maximum and minimum element in the array.


def getMin(arr,n):
    return min(arr)
    
def getMax(arr,n):
    return max(arr)
    
if __name__=='__main__':
    arr = [54, 546, 548, 60]
    n = len(arr)
    print('minimum element of array : ' , getMin(arr,n))
    
    print('maximum element of array : ', getMax(arr,n))
    