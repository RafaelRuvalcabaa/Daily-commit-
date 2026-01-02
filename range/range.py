# Range 

# nums = range(2,10)  # No crea esto [1,2,3,4,5]

for num in range(10): #Te genera una secuencia de numeros pero no una lista 
    print(num)

#Range(Inicio, final, de cuantos incrementa)

for num in range(0,100,3):
    print(num)

for num in range(100):
      if num % 2 == 1:
           print(num)

nums = range(0,10)
list_of_nums = list(nums) #Aqui con list() se genera una lista usando range()
print(list_of_nums)

contador = 0
while contador < 5: 
     print("Hacer 5 veces algo")
     contador += 1


for _ in range(5): print("hacer algo 4 veces")