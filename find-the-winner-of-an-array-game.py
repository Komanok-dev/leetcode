from collections import deque


class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        winner = arr[0]
        count_wins = 0
        for i in range(1, len(arr)):
            if arr[i] > winner:
                winner = arr[i]
                count_wins = 0
            count_wins += 1
            if (count_wins == k):
                break
        return winner

    def getWinner2(self, arr: list[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        if k > len(arr):
            return max(arr)
        last_winner = None
        arr = deque(arr)
        count_wins = 0
        while count_wins < k:
            one, two = arr.popleft(), arr.popleft()
            winner = max(one, two)
            print(f'winner {winner}, one {one}, two {two}')
            if winner == last_winner or last_winner == None:
                count_wins += 1
            else:
                count_wins = 1
            print(count_wins)
            last_winner = winner
            arr.appendleft(winner)
            arr.append(min(one, two))
        return winner


arr = [2,1,3,5,4,6,7]
k = 2

arr = [1,11,22,33,44,55,66,77,88,99]
k = 1000000000

arr = [1,25,35,42,68,70]
k = 1 # 25

a = Solution()
print(a.getWinner(arr, k))
