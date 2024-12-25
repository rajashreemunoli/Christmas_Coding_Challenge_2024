#26Remove Duplicates from Sorted Array

def removeDuplicates(nums):
    k=0
    for i in range(1, len(nums)):
        if nums[i]!=nums[k]:
            k+=1
            nums[k]=nums[i]
    return k+1

nums =[1,1,2,3,4,4,4,5]
print(removeDuplicates(nums))