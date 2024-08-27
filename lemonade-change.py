class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        hand = {'5': 0, '10': 0, '20': 0}
        for bill in bills:
            print(hand)
            if bill == 5:
                hand[str(bill)] += 1
            elif bill == 10 and hand['5'] > 0:
                hand['10'] += 1
                hand['5'] -= 1
            elif bill == 20:
                if hand['5'] > 0 and hand['10'] > 0:
                    hand['20'] += 1
                    hand['10'] -= 1
                    hand['5'] -= 1
                elif hand['5'] >= 3:
                    hand['20'] += 1
                    hand['5'] -= 3
                else:
                    return False
            else:
                return False
        return True
