temperatura = float(input("Qual a temperatura atual? "))

if temperatura > 30:
    print("Muito quente")
elif temperatura < 15:
    print("Muito frio")
else:
    print("Temperatura agradável")