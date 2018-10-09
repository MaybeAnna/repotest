# oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze 2 lata, kazdy psi rok to 10,5 ludzkiego roku
# przez kolejne lata, psi rok to 4 ludzkie lata
# np. 15 lat ludzkich to 73 psie lata




a = int(input('Podaj wiek psa'))
if a <= 2:
    print('wiek psa w ludzkich latach wynosi', a * 10.5)

else:
      print('wiek psa w ludzkich latach wynosi', (a-2) * 4 + 21)



