v = float(input())
if 2000 < v <= 3000: r = (v - 2000) * 8/100
elif 3000 < v <= 4500: r = 1000 * 8/100 + (v - 3000) * 18/100
else: r = 1000 * 8/100 + 1500 * 18/100 + (v - 4500) * 28/100
print('Isento') if v <= 2000 else print(f'R$ {r:.2f}')
