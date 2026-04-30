class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            L = 0
            R = len(matrix[0]) - 1
            m = (l+r) // 2
            data = matrix[m]
            if data[R] < target: l = m + 1; continue
            elif data[R] > target and data[L] > target: r = m - 1; continue
            if data[L] <= target <= data[R]:
                while L <= R:
                    M = (L+R) // 2
                    if data[M] == target: return True
                    elif data[M] > target: R = M - 1
                    else : L = M + 1
                break
        return False