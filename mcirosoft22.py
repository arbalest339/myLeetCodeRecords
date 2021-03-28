import heapq
import time
import random
def solution(A, K):
    time_start=time.time()
    min_q = A[K:]
    max_q = [-i for i in A[K:]]
    heapq.heapify(min_q)
    heapq.heapify(max_q)
    ans = -max_q[0] - min_q[0]
    for i in range(K, len(A)):
        heapq.heappush(max_q, -A[i - K])
        heapq.heappush(min_q, A[i - K])
        max_q.remove(-A[i])
        heapq.heapify(max_q)
        min_q.remove(A[i])
        heapq.heapify(min_q)
        ans = min(ans, -max_q[0] - min_q[0])
    time_end=time.time()
    print('time cost',time_end-time_start,'s')
    return ans

randomlst = [random.randint(1,100000) for _ in range(1000000)]
print(solution(randomlst, 2))
