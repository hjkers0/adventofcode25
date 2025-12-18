with open('input') as f:
    file = f.read()

signs = file.strip().split('\n')[-1].split()
width = len(signs)
numbers = file.strip().split()[:-width]
total = {x: int(numbers[x]) for x in range(width)}
numbers = numbers[width:]
for indx in range(len(numbers)):
    sign = signs[indx % width]
    if sign == '*':
        total[indx % width] *= int(numbers[indx])
    elif sign == '+':
        total[indx % width] += int(numbers[indx])
print('result operation:', sum(total.values()))

