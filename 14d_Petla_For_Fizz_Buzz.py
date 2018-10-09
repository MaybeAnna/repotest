# wypisz liczby  od 1 do 100
# jezeli liczba jest podzielna przez 3, wpisz Fizz
# jezeli liczba jest podzielna przez 5, wpisz Buzz
# jezeli liczba jest podzielna przez 3 i 5, wpisz FizzBuzz


for i in range (0,100):
   if i % 3 == 0:
       print (i, "Fizz")
   elif i % 5 == 0:
       print (i, "Buzz")
   elif i % 3 == 0 and i % 5 == 0:
       print (i, "FizzBuzz")
   else:
       print (i)