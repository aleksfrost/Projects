n, m = [int(i) for i in input().split()]
topX = 0
topY = 0
bottomX = m - 1
bottomY = n - 1
k = 1
array = [[0 for i in range(m)] for j in range(n)]
while k <= n * m:
	x = topX
	y = topY
	for x in range(topX, bottomX + 1):
		array[y][x] = k
		k = k + 1
	topY = topY + 1
	if k <= n * m:
		for y in range(topY, bottomY + 1):
			array[y][x] = k
			k = k + 1
		bottomX = bottomX - 1
	if k <= n * m:
		for x in range(bottomX, topX - 1, -1):
			array[y][x] = k
			k = k + 1
		bottomY = bottomY - 1
	if k <= n * m:
		for y in range(bottomY, topY - 1, -1):
			array[y][x] = k
			k = k + 1
		topX = topX + 1

for row in array:
	for el in row:
		print(str(el).center(3), end=' ')
	print()
