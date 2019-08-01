x11,y11=map(int,input().split())
l=list(map(int,input().split()))
for p in range(x11):
	if l[p]==y11:
		o=p+1
print(o)
