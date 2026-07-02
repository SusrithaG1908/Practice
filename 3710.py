class Solution:
    def clearStars(self, s: str) -> str:
        h = []
        for i,c in enumerate(s):
            c=='*' and heappop(h) or heappush(h,(c,-i))
        
        return ''.join(c for c,_ in sorted(h,key=lambda p:-p[1]))
        