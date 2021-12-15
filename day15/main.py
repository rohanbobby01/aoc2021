import heapq
from collections import defaultdict

with open("data.txt") as file:
    my_list = file.read().split()
    plots = []
    for r in my_list:
        plots.append(list(map(lambda x: int(x), r)))
    x = len(plots[0])
    y = len(plots)


def big_plot(row, col):
    cost = plots[row % y][col % x] + int(row / y) + int(col / x)
    if cost > 9:
        return cost % 9
    else:
        return cost


def find(x, y):
    while True:
        c, row, col = heapq.heappop(pq)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        cost[(row, col)] = c
        if row == y - 1 and col == x - 1:
            break
        for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            rr, cc = row + a, col + b
            if 0 <= rr < y and 0 <= cc < x:
                heapq.heappush(pq, (big_plot(rr, cc) + c, rr, cc))
    return cost[(y - 1, x - 1)]


cost = defaultdict(int)
pq = [(0, 0, 0)]
heapq.heapify(pq)
visited = set()
ans1 = find(x, y)

cost = defaultdict(int)
pq = [(0, 0, 0)]
heapq.heapify(pq)
visited = set()
ans2 = find(5 * x, 5 * y)
print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:{ans2}')
