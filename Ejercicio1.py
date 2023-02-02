hora_de_llegada  = 8
hora_salida = 10
precio_por_hora = 5000
horas_parqueo = hora_salida-hora_de_llegada
precio_a_pagar = horas_parqueo*precio_por_hora   
print("usted estuvo", horas_parqueo, "horas parqueado y el valor a pagar es:", precio_a_pagar)

hora_de_llegada= int(input("Ingrese la hora de llegada: "))
hora_salida= int(input("Ingrese la hora de salida: "))
Nombre = input("Escriba su nombre: ")
precio_por_hora= 5000
horas_parqueo= hora_salida-hora_de_llegada
print(Nombre, "usted estuvo parqueado", horas_parqueo, "hrs", "debe pagar: ", (horas_parqueo*precio_por_hora))
 