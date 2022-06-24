v = input().split(' ')
a, b = int(v[0]), int(v[1])
print('Sao multiplos') if a%b == 0 or b%a == 0 else print('Nao sao multiplos')
