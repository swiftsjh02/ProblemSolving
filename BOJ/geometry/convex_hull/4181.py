import math

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def polar_angle(a,b):
    return math.atan2(b[1]-a[1],b[0]-a[0])

def dist(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def convex_hull(points):
    points.sort(key=lambda x: (x[0],x[1]))
    p0=points[0]
    points=points[1:]
    tmp=[]
    points.sort(key=lambda p: (polar_angle(p0,p),dist(p0,p)))
    tmp.append(p0)
    for i in points:
        tmp.append(i)

    return tmp

n=int(input())
points=[]
for i in range(n):
    tmp=list(input().split())
    if tmp[2]=="Y":
        temp=[int(tmp[0]),int(tmp[1])]
        points.append(temp)


points=convex_hull(points)
print(len(points))
for i in points:
    print(i[0],i[1])
