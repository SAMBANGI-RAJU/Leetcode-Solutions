class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)

        arr.sort()

        if arr[0] != 1:
            arr[0] = 1

        for j in range(1, n):
            if arr[j] - arr[j - 1] <= 1:
                continue
            else:
                arr[j] = 1 + arr[j - 1]

        return max(arr)
