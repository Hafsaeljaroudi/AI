import random


n = int(input("Enter the number of nodes: "))


matrice = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(0)
        else:
            row.append(random.randint(1, 100))
    matrice.append(row)


with open("matrice.txt", "w") as file:
    file.write(str(n) + "\n")
    for row in matrice:
        file.write(" ".join(str(num) for num in row) + "\n")


with open("matrice.txt", "r") as file:
    lines = file.readlines()

n = int(lines[0])
cout = []
for line in lines[1:]:
    cout.append(list(map(int, line.strip().split())))


a = random.randint(0, n - 1)
used = [False] * n
used[a] = True
final_edges = []
cout_sum = 0
edges_done = 0


while edges_done < n - 1:
    smallest_cout = None
    node_from = None
    node_to = None

    for i in range(n):
        if used[i]:
            for j in range(n):
                if not used[j] and cout[i][j] != 0:
                    if smallest_cout is None or cout[i][j] < smallest_cout:
                        smallest_cout = cout[i][j]
                        node_from = i
                        node_to = j

    if node_from is not None and node_to is not None:
        used[node_to] = True
        cout_sum += cout[node_from][node_to]
        final_edges.append((node_from, node_to))
        edges_done += 1


for edge in final_edges:
    print(f"({edge[0]}, {edge[1]})", end=" ")
print()
print("cout:", cout_sum)
