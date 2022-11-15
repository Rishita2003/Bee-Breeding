from operator import sub

def spiral(a,n):
    if a != 0 or n != 0 and a and n <= 1000 and a != n:
        return shortest_distance(a,n)

def shortest_distance(a: int,n: int, spiral=[[0, 0, 0] * 2]):
    transforms = ((1, 0, -1), (1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1))

    for i in range(max(a,n)):
        for index, values in enumerate(transforms):
            for k in range(i - (1 == index) * 1):
                spiral.append(list(map(sum, list(zip(spiral[-1], values)))))

    return max(list(map(abs, list(map(sub, *[spiral[a], spiral[n]])))))

a = int(input("Enter the first num :"))
n = int(input("Enter the last num :"))

print(f"Shortest distance {spiral(a, n)-1}")
