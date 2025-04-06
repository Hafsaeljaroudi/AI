import random

n = int(input("Enter the number of nodes: "))

cout_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0 if i == j else random.randint(1, 100))
    cout_matrix.append(row)


with open("matrice.txt", "w") as f:
    f.write(f"{n}\n")
    for row in cout_matrix:
        f.write(" ".join(map(str, row)) + "\n")

startNode = random.randint(0, n-1)
used = [False] * n
used[startNode] = True
edges = []
total_cout = 0  

for _ in range(n-1):
    min_cout = float('inf')
    u, v = -1, -1
    
    
    for i in range(n):
        if used[i]:
            for j in range(n):
                if not used[j] and cout_matrix[i][j] < min_cout:
                    min_cout = cout_matrix[i][j]
                    u, v = i, j
    
    
    if u != -1:
        used[v] = True
        total_cout += min_cout  
        edges.append((u, v))

print("Edges:", ' '.join(f"({u},{v})" for u, v in edges))
print("Total cout:", total_cout)