#Leetcode 1792. Maximum Average Pass Ratio
import heapq

def maxAverageRatio(classes,extraStudents):
    def ratio_increase(passed,total):
        return (passed+1)/(total+1)-passed/total
    
    max_heap=[]

    for passed,total in classes:
        increase=ratio_increase(passed,total)
        heapq.heappush(max_heap,(-increase,passed,total))
    
    for i in range(extraStudents):
        increase,passed,total=heapq.heappop(max_heap)
        passed,total=passed+1,total+1
        new_increase=ratio_increase(passed,total)
        heapq.heappush(max_heap,(-new_increase,passed,total))
    
    total_ratio=0

    for increase,passed,total in max_heap:
        total_ratio+=passed/total

    return total_ratio/len(classes)

# Example Usage
classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2
print(maxAverageRatio(classes, extraStudents))