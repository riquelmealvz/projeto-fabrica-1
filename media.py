n1 = float(input("Digite a 1° nota:"))
n2 = float(input("Digite a 2° nota:"))
n3 = float(input("Digite a 3° nota:"))
n4 = float(input("Digite a 4° nota:"))

media = (n1 + n2 + n3 + n4) / 4 

if media >= 7.0:
    situacao = "Aprovado✅"
elif media >= 5.0:
    situacao = "Recuperacao⚠️"
else:
    situacao = "Reprovado❌"

print(f"\nMedia: {media: .2f} | Situacao: {situacao}")