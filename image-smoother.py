class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        result = [[0] * len(img[0]) for _ in range(len(img))]
        def smooth(m, n):
            average = []
            for i in range(m-1, m+2):
                if 0 <= i < len(img):
                    for j in range(n-1, n+2):
                        if 0 <= j < len(img[0]):
                            average.append(img[i][j])
            return sum(average) // len(average)

        for row in range(len(img)):
            for col in range(len(img[0])):
                result[row][col] = smooth(row, col)
        return result


img = [[100,200,100],[200,50,200],[100,200,100]]

a = Solution()
print(a.imageSmoother(img))
print([[137,141,137],[141,138,141],[137,141,137]], 'correct')