import math

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def polar_angle(a,b):
    return math.atan2(b[1]-a[1],b[0]-a[0])

def dist(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def convex_hull(points):
    p0=min(points,key=lambda p: (p[1],p[0]))
    points.sort(key=lambda p: (polar_angle(p0,p),dist(p0,p)))
    hull=[]
    for i in range(len(points)):
        while len(hull)>=2 and ccw(hull[-2],hull[-1],points[i])!=1:
            hull.pop()
        hull.append(points[i])
    return len(hull)

n=int(input())
points=[]
for i in range(n):
    x,y=map(int,input().split())
    temp=[x,y]
    points.append(temp)


print(convex_hull(points))
