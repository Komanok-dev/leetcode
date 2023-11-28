class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        ans, cnt, left = 1, 0, -1
        for curr in range(len(corridor)):
            if corridor[curr] == 'S':
                cnt += 1
                if cnt >= 3 and cnt % 2:
                    ans = ans * (curr - left) % MOD
                left = curr
        return ans if cnt and cnt % 2 == 0 else 0


    def numberOfWays2(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seats = []
        idx = 0
        while True:
            idx = corridor.find('S', idx)
            if idx == -1:
                break
            seats.append(idx)
            idx += 1
        print(seats)
        if len(seats) < 2:
            return 0
        length = len(seats) - len(seats) % 2
        ans = 1
        i = 2
        while i < length:
            ans = ans * (seats[i] - seats[i-1]) % MOD
            i += 2
        print(len(seats))
        return ans if len(seats) % 2 == 0 else 0


corridor = "SSPPSPSPPSSPPSS"
corridor = "SSPPSPS"
corridor = "SPPPPPPPSPPPSPSSSPPPPPPPPPPPPPPPPPSPPPPPPPPPPPPPPPPSPPPPPSPSPPPPPPSPSPPSPSPPPSPSPPSSPPPPPSPPSSPP"
corridor = "PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS" # 919999993
a = Solution()
print(a.numberOfWays(corridor))