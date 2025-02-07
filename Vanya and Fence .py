n,h=map ( int, input().split())
m= list (map(int, input().split()))
print (sum(2 if x > h else 1 for x in m))
