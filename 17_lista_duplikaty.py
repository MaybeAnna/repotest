# tworzymy liste [1,1,"Ala", "Ala"] i usuwamy za niej duplikaty
# uzyc petle in

lista = [1,1,"Ala", "Ala"]
lista1 = []
for element in lista:
    if element not in lista1:
        lista1.append(element)
        print (lista1)





