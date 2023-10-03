set = [r for r in range(21)]
print(set)
# print(len(set))
# print(set[len(set)-1])

inn = 5
out = 1

x = {}
y = {}
for i in range(0, len(set) - inn+1):
    # print(f"{i}, to {i+inn}")
    x[i] = [row for row in set[i : i+inn]]
    y[i] = [row for row in set[i+inn-out : i+inn]]

for key in y:
    print (f"x{key}: {x[key]}")
    print (f"y{key}: {y[key]}")
    print("")

