# lista_duplikaty = [1,1,"Ala", "Ala", 3, 4, 3]
#  Z listy pozbyc sie duplikatow


lista_duplikaty = [1,1,"Ala", "Ala", 3, 4, 3]
lista_unikaty = []

for element in lista_duplikaty:
    if element not in lista_unikaty:
        lista_unikaty.append(element)
        print (lista_unikaty)

