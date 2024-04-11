n1 = [4, 8, 8, 12, 24, 48]

n2 = {}

for item in n1:
    if item in n2:
        print("Повторяющийся элемент:", item)
    else:
        n2[item] = 1
