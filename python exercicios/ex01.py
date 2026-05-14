import random
numeros=[random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)]
print("os numeros sortedos foram:",end=" ")
for c in numeros:
    print(c,end=" ")
print(" ")
print(f" maior:{max(numeros)}")
print(f" menor :{min(numeros)}")