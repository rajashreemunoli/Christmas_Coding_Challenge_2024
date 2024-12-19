#Sort Array by Increasing Frequency

from collections import Counter

def frequencySort(nums):
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))

arr=[2,2,4,5,6,2,3,5,5,6,6,6,8]
print(f'soreted array: {frequencySort(arr)}')