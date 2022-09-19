# contador = 0
#
# while contador < 10:
#     contador = contador + 1
#     if contador == 1:
#         print(contador, "item limpo")
#     else:
#         print(contador, "itens limpos")
#
# print("Fim da repetição")

contador = 0

while True:
    if contador < 10:
        contador = contador + 1
        if contador == 1:
            print (contador, "item limpo")
        else:
            print(contador, "itens limpos")
    else:
        break

print("Fim da repetição")
