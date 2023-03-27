class Solution:
    def minJumps(self, arr: List[int]) -> int:

        # set pos[x][0] = True as unvisited indicator
        pos = collections.defaultdict(lambda: [True])

        # Store positions i based on value x=arr[i]
        # reverse is essential as we are finding shortest path backward
        for i, x in reversed(list(enumerate(arr))):
            pos[x].append(i)

        # res = result table, q = BFS queue
        n = len(arr)
        res = list(range(n-1, -1, -1))
        q = collections.deque()

        # start the search backward
        for k in range(n-1, -1, -1):
            q.append(k)
            while q:
                i = q.popleft()
                if pos[arr[i]][0]: # if unvisited
                    pos[arr[i]][0] = False

                    # create jump portal for all positions with same value
                    for j in pos[arr[i]][1:]:
                        res[j] = min(res[j], res[i]+1)
                        q.append(j)

                    # add adjcent posisitons to queue
                    for j in pos[arr[i]][1:]:
                        if j > 0:
                            res[j-1] = min(res[j-1], res[j]+1)
                            q.append(j-1)
                        if j < n-1:
                            res[j+1] = min(res[j+1], res[j]+1)
                            q.append(j+1)
        return res[0]
        