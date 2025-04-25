# Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each of the points in your 3-D space and store them in a list. The final output is a list with each consisting of a point and its nearest neighbour.

def dis(p1, p2):
    return (((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)**0.5)

def nearest(points):
    l = []
    for i, point in enumerate(points):
        min = float("inf")
        nearestpt = None
        for j, temp in enumerate(points):
            if i != j:
                distance = dis(point, temp)
                if distance < min:
                    min = distance
                    nearestpt = temp
        l.append((point, nearestpt))
    return l

l1 = []
print("Enter 10 3D points (x y z):")
for i in range(10):
    x, y, z = map(int, input(f"Point {i+1}: ").split())
    l1.append((x, y, z))

l = nearest(l1)

print()
print("Nearest Neighbors:")
for i, j in l:  # i=point and j=neighbour
    print(f"{i} Nearest -> {j}")
