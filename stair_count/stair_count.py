import pprint

memo={1:1,2:2}
def stair_count(n):
    ways=0
    if n<1:
        raise ValueError("n must be positive")
    if n not in memo:
        ways=memo.get(n-1,stair_count(n-1))+memo.get(n-2,stair_count(n-2))
        memo[n]=ways
    return ways

print(stair_count(50))
pprint.pprint(memo)
