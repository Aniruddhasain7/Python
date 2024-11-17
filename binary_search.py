def binary_search(arr,a,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==a:
            return mid
        elif arr[mid]<a:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[7,9,10,4,11,30,8]
a=int(input("Enter item to be searched:"))
print("The given array is:",arr)
print("Element to be found is:",a)
index=binary_search(arr,a,0,len(arr)-1)
if index != -1:
    print("The index of the element is:"+str(index))
else:
    print("Element Not Found")
