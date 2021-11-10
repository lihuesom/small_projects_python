def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos "+tipo_pesos+ "tienes?: ")
    pesos = float(pesos)
    dolares = pesos /valor_dolar
    dolares = round(dolares, 2)
    dolares =str(dolares)
    print("Tienes $"+ dolares + " dólares")    



menu = """
Bienvenido al conversor de monedas 💵 💴 💶 💷 💰

1 - Pesos colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción:
"""
opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos",3462)
elif opcion == 2:
    conversor("Argentinos",85)
elif opcion == 3:
    conversor("Mexicanos",20)
else:
    print("Ingresa una opción valida")









# dolares1 = input("¿Cuántos dolares tienes?: ")
# dolares1 = float(dolares1)
# pesoc = valor_dolar * dolares1
# pesoc = round(pesoc, 2)
# pesoc = str(pesoc)
# print("Tienes $"+pesoc+ "pesos colombianos")



