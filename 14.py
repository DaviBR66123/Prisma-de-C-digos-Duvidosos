n = int(input("Insira minutos: "))

h = n // 60
h1 = n % 60

if h1 != 0 or n == 60:
	n -= (h * 60)
	
else:
	tapaburaco = "literalmente nada"

print(h,"h ", n, "minutos")