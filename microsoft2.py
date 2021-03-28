import time
import random
def solution(A, K):
    # write your code in Python 3.6
    time_start=time.time()
    hashmap = {}
    smallest = A[0]
    biggest = A[0]
    for n in A:
        if n in hashmap:
            hashmap[n] += 1
        else:
            hashmap[n] = 1
        smallest = min(smallest, n)
        biggest = max(biggest, n)
    
    for i in range(K):
        hashmap[A[i]] -= 1
        if A[i] == biggest:
            if hashmap[A[i]] < 1:
                j = A[i]
                while j not in hashmap or hashmap[j] <1:
                    j -= 1
                biggest = j 
        if A[i] == smallest:
            if hashmap[A[i]] < 1:
                j = A[i]
                while j not in hashmap or hashmap[j] <1:
                    j += 1
                smallest = j
    
    cur_best = biggest - smallest
    for i in range(K, len(A)):
        hashmap[A[i]] -= 1
        if A[i] == biggest:
            if hashmap[A[i]] < 1:
                j = A[i]
                while j not in hashmap or hashmap[j] <1:
                    j -= 1
                biggest = j 
        if A[i] == smallest:
            if hashmap[A[i]] < 1:
                j = A[i]
                while j not in hashmap or hashmap[j] <1:
                    j += 1
                smallest = j
        
        hashmap[A[i-K]] += 1
        if A[i-K] < smallest:
            smallest = A[i-K]
        if A[i-K] > biggest:
            biggest = A[i-K]
        
        cur_best = min(biggest - smallest, cur_best)
    
    time_end=time.time()
    print('time cost',time_end-time_start,'s')
    return cur_best

randomlst = [random.randint(1,100000) for _ in range(1000000)]
print(solution(randomlst, 2))