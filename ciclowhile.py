#CICLO WHILE (MIENTRAS)
#se ejecuta hastqa que la condicion sea falta
#sintaxis, while condicion: debajo instruccion, antes del while se
#deben inicializar las variables importantes

#programa que me muestre los numeros menores que 10 / V2 menor que 10
"""
x = 0
while x <=10:
    print(x)
    x+=1

x = 10
while x >0:
    x-=1
    print(x)"""

#While con if, break (rompre el ciclo), continue

#While con If

num = 0
while num <=8:
    num +=1
    print(num)    
    if num == 6:
        break   

num = 0
while num <=8:
    num +=1        
    if num == 6:
        continue 
    print(num)
     
    