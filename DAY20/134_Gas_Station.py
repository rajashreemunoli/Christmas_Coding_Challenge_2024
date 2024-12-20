#134 Gas station
#There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station
# to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
#Given two integer arrays gas and cost, return the starting gas station's index
# if you can travel around the circuit once in the clockwise direction, otherwise return -1.
# If there exists a solution, it is guaranteed to be unique.

def canCompleteCircuit(gas, cost):
    if sum(gas)<sum(cost):
            return -1
        
    tank=0
    start_index=0
    for i in range(len(gas)):
        tank=tank+gas[i]-cost[i]
        if tank<0:
            tank=0
            start_index=i+1
    return start_index

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
if canCompleteCircuit(gas,cost)==-1:
     print(f'Cannot travel around the circuit')
else:
     print(f'Can travel around the circuit with starting index {canCompleteCircuit(gas,cost)}')