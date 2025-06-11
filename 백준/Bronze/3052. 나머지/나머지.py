
a = [] 
for i in range(10):
    b = int(input())
    a.append(b % 42) 


unique = []
for i in a:
    if i not in unique: 
        unique.append(i)
print(len(unique)) 