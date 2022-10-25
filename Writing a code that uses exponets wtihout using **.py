b = int(input("input your base"))
e = int(input("input your exponent"))
def nevcov(e):
    if e < 0:
        abs(e)
    return e

def power(b,e): 
    res = 1 
    for i in range(e): 
        res *= b 
    return res

answer = power(b,e)

print(answer)