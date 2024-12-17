#135 Candy
#There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
#You are giving candies to these children subjected to the following requirements:
#Each child must have at least one candy.
#Children with a higher rating get more candies than their neighbors.
#Return the minimum number of candies you need to have to distribute the candies to the children.

def candy(ratings):
        num_children=len(ratings)
        candies_l2r=[1]*num_children
        candies_r2l=[1]*num_children

        for i in range(1,num_children):
            if ratings[i]>ratings[i-1]:
                candies_l2r[i]=candies_l2r[i-1]+1

        for i in range(num_children-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candies_r2l[i]=candies_r2l[i+1]+1
        
        candies=[max(candies_l2r[i],candies_r2l[i]) for i in range(len(ratings))]
        return sum(candies)

min_candies=candy(ratings=[1,0,2])
print(f'Minimum no. of candies to be distributed: {min_candies}')