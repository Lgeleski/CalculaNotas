import media

print("Programa de avaliação de notas ")
print()

n1 = float(input("Informe a 1° nota: "))
n2= float(input("Informe a 2° nota: "))
n3 = float(input("Informe a 3° nota: " ))

media = media.calcular_media(n1, n2, n3)

print(f"A média ponderada é {media:.2f} ")