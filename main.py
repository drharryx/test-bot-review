# Este es un programa para calcular el promedio de notas

def calcular_promedio(notas):
    suma = 0
    for i in range(0, len(notas)):
        suma += notas[i]
    promedio = suma / len(notas)
    return promedio

def imprimir_resultado(promedio):
    if promedio >= 6:
        print("Aprobado")
    elif promedio >= 4:
        print("Recuperación")
    else:
        print("Reprobado")

notas = []
while True:
    nota = input("Ingrese una nota (o 'q' para terminar): ")
    if nota == 'q':
        break
    notas.append(float(nota))

promedio = calcular_promedio(notas)
print("El promedio es: " + str(promedio))
imprimir_resultado(promedio)

a = 10
b = "20"
c = a + b
