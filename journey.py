n,a,b,c = map(int , input().split())
s = n//(a+b+c)
x = n%(a+b+c)
y = s*3
if x > 0:
    x -= a
    y += 1
if x > 0:
    x -= b
    y += 1
if x > 0:
    x -= c
    y += 1

print (y)
