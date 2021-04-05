import random

record = []
def randomPartition(start, finish):
    i = random.randint(start, finish-1)
    record.append(i)
    return i

def quiksort(nums):
    recSort(nums, 0, len(nums))
    return nums

def recSort(nums, start, finish):
    if finish-start<2:
        return
    elif finish-start==2:
        nums[start], nums[finish-1] = min(nums[start], nums[finish-1]), max(nums[start], nums[finish-1])
        return
    i = randomPartition(start, finish)
    nums[start], nums[i] = nums[i], nums[start]
    i = start
    j = finish-1
    movei = False
    while i<j:
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            movei = not movei
        if movei:
            i += 1
        else:
            j -= 1

    recSort(nums, start, i)
    recSort(nums, i+1, finish)

if __name__ == "__main__":
    nums = [5,6,3,4,2,1,8,7,12,10,11]
    quiksort(nums)
