n, t = [int(i) for i in input().split()]

floors = [int(i) for i in input().split()]

leave = int(input())

if t >= floors[leave - 1] or t >= floors[-1] - floors[leave - 1]:
    print(floors[-1] - 1)
elif floors[-1] > 2 * floors[leave - 1]:
    print(floors[leave - 1] + floors[-1] - 2)
elif floors[-1] < 2 * floors[leave - 1]:
    print(2 * floors[-1] - floors[leave - 1] - floors[0] - 2)

