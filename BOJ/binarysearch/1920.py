import sys

def searchn(k,nums,s,e):
   
    if s>e:
        return 0

    mid = (s+e)//2

    if nums[mid]==k:
        return 1
    elif nums[mid]>k:
        e = mid -1
        
    elif nums[mid]<k:
        s=mid+1

    return searchn(k,nums,s,e)




n=int(sys.stdin.readline())
nums=[int(k) for k in sys.stdin.readline().split(" ")]
n2=int(sys.stdin.readline())
check=[int(k) for k in sys.stdin.readline().split(" ")]
nums.sort()



for k in check:
   print(searchn(k,nums,0,len(nums)-1))

