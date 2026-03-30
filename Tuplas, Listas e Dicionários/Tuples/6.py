n = int(input("Insira um número: "))
n1 = int(input("Insira outro número: "))
n2 = int(input("Insira mais outro número: "))

nl = (n, n1, n2)

media = nl[0] + nl[1] + nl[2]
media /= 3

print(f"A média é {media:.1f}")