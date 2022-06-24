n = input().split(' ')
n1, n2, n3, n4 = float(n[0]), float(n[1]), float(n[2]), float(n[3])
m = (n1*2+n2*3+n3*4+n4*1)/10
print(f'Media: {m:.1f}')
if m >= 7: print('Aluno aprovado.')
elif m < 5: print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    e = float(input())
    print(f'Nota do exame: {e:.1f}')
    mf = (m+e)/2
    print('Aluno aprovado.') if mf > 5 else print('Aluno reprovado.')
    print(f'Media final: {mf:.1f}')


