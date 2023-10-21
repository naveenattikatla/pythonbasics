# Sum of n number should not be exceed to ms 
# We need to maximize the value of mn^2 with respect to number os n values to be consider given by mt
t = int(input())
for _ in range(t):
    mt , mn , ms  = map(int , input().split())
    ans  = 0 
    while ms > 0  and mt  : 
        if(ms >= mn):
            ans += mn * mn 
        else:
            ans  += ms * ms
        ms  -= mn 
        mt -=1
    print(ans)

def outer():
    return lambda x : x
print(outer()(9))