from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    gas_acquired, total = 0, 0
    index = 0
    for i in range(len(gas)):
        gas_acquired += gas[i] - cost[i]
        total += gas[i] - cost[i]
        if gas_acquired < 0:
            gas_acquired = 0
            index = i + 1
    print(total)
    return index if total >= 0 else -1


# print(canCompleteCircuit(gas=[1,2,3,4,5], cost=[3,4,5,1,2]))
print(canCompleteCircuit(gas=[3, 1, 1], cost=[1, 2, 2]))