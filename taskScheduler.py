'''Task Scheduler
Solved
You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

Example 1:

Input: tasks = ["X","X","Y","Y"], n = 2

Output: 5
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

Example 2:

Input: tasks = ["A","A","A","B","C"], n = 3

Output: 9
Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

Constraints:

1 <= tasks.length <= 1000
0 <= n <= 100'''

class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        cnt = Counter(tasks)
        maxHeap = [-i for i in cnt.values()]
        heapq.heapify(maxHeap)

        q = deque()
        t = 0

        while maxHeap or q:
            t += 1
            if maxHeap:
                tsk = 1 + heapq.heappop(maxHeap)
                if tsk:
                    q.append((tsk, t+n))
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        return t