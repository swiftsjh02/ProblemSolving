n,m=map(int,input().split())
n_heard=set()
n_seen=set()
for i in range(n):
    n_heard.add(input())
for i in range(m):
    n_seen.add(input())

n_heard_seen=list(n_heard&n_seen)
n_heard_seen.sort()
print(len(n_heard_seen))

for i in n_heard_seen:
    print(i)