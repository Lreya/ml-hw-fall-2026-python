n = int

n = int(input("Enter input N: "))

array = []
for i in range(n):
  m = int(input(f"Enter numbers[{i+1}] of {n}: "))
  array.append(m)

x = int
x = int(input("Enter input X: "))


if x in array:
  print(array.index(x)+1)
else:
  print(-1)