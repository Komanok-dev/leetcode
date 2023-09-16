class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def check(heights, x):
            lookup = [[False]*len(heights[0]) for _ in range(len(heights))]
            stk = [(0, 0)]
            while stk:
                r, c = stk.pop()
                if (r, c) == (len(heights) - 1, len(heights[0]) - 1):
                    return True
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < len(heights) and
                                0 <= nc < len(heights[0]) and
                                abs(heights[nr][nc]-heights[r][c]) <= x and
                                not lookup[nr][nc]):
                            continue
                    lookup[nr][nc] = True
                    stk.append((nr, nc))
            return False            
        
        left, right = 0, 10 ** 6
        while left <= right:
            mid = left + (right-left) // 2
            if check(heights, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
