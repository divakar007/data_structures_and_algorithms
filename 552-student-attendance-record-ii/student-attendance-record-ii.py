class Solution:
    def checkRecord(self, n):
        MOD = 10**9 + 7
        # 1) build tribonacci P0 up to n
        if n == 0:
            return 1
        P0 = [0] * (n+1)
        P0[0] = 1
        if n >= 1:
            P0[1] = 2  # "P","L"
        if n >= 2:
            P0[2] = 4  # "PP","PL","LP","LL"
        for i in range(3, n+1):
            P0[i] = (P0[i-1] + P0[i-2] + P0[i-3]) % MOD
        
        # 2) count 0-A records
        ans = P0[n]
        
        # 3) count 1-A records by placing A at each position
        #    and multiplying the #ways before and after
        for i in range(n):
            ans = (ans + P0[i] * P0[n-1-i]) % MOD
        
        return ans
