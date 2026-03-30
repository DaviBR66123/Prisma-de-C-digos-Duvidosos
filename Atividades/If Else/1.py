print("Qual a temperatura atual?")
temp = float(input())

if temp < 10:
    print("Muito frio, né?")

elif temp > 10 and temp <= 24:
    print("Agradável")

elif temp > 24 and temp < 30:
    print("Quente")

else:
    print("Quente demais, estou derretendo...")
