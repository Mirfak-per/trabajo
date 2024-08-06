list_trabajo= []
operatoria= []
# para que son estas listas? lo veras mas adelante en "guardar datos"
def add(num1,num2):
    print(f"{num1} + {num2} = {num1+num2}")
    list_trabajo.append(num1+num2)
    operatoria.append(f"{num1} + {num2}")
    #print(f"{num1}+{num2}"), es igual a poner print(num1,"+",num2)
    
def subtract(num1,num2):
    print(f"{num1} - {num2} = {num1-num2}")
    list_trabajo.append(num1-num2)
    operatoria.append(f"{num1} - {num2} =")

def multiply(num1,num2):
    print(f"{num1} * {num2} = {num1*num2}")
    list_trabajo.append(num1*num2)
    operatoria.append(f"{num1} * {num2}")

def divide(num1,num2):
    print(f"{num1} / {num2} = {num1/num2}")
    list_trabajo.append(num1/num2)
    operatoria.append(f"{num1} / {num2}")

def power(num1,num2):
    print(f"{num1} ^ {num2} = {num1**num2}")
    list_trabajo.append(num1**num2)
    operatoria.append(f"{num1} ^ {num2}")

def Logaritmo(num1,num2=10):
    import math
    print(f"log{num1},{num2}",math.log(num1,num2))
    list_trabajo.append(math.log(num1,num2))
    operatoria.append(f"log{num1},{num2}")
    #mat.log es logaritmos con "e" naturales, para hacerlo natural cambia la base a 10
    # el primer numero es num1 = el primer argumento y el num2 = base

def guardar_datos():
 import csv
 #este "guardar datos se ve mucho mejor que el otro no?"
 with open("Datos guardados completos.csv","+a",newline="") as archivo_csv:
    writer = csv.writer(archivo_csv)
    if archivo_csv.tell()==0:
        writer.writerow(["operaciones","Resultado"])
    for i in range(len(operatoria)):
        writer.writerow([operatoria[i],list_trabajo[i]])
    print("Datos guardados con exito")

def menu():
    #el print con tres """ """ a cada lado permite continuar para abajo
    print("""
        Select operation.
        1.Suma           : + 
        2.Resta          : - 
        3.Multiplicacion : * 
        4.Division       : / 
        5.Potencia       : ^ 
        6.Logaritmo      : $ 
        7.Clear Screen   :   
        8.Guardar datos  :   
        9.Cerrar         :   """)
    choice = input("Enter Choice : ")
    return choice

def choices(choice):
    if choice in ('1','2','3','4','5','6','7',"8","9"):
        if choice not in("7","8","9"):
            num1 = int(input("Enter First Number = "))
            num2 = int(input("Enter 2nd Number = "))
        if choice == '1':
            add(num1,num2)
        elif choice == '2':
            subtract(num1,num2)
        elif choice == '3':
            multiply(num1,num2)
        elif choice == '4':
            divide(num1,num2)
        elif choice == '5':
            power(num1,num2)
        elif choice == "6":
            Logaritmo(num1,num2)
        elif choice == "7":
            clearscreen()
        elif choice == "8":
            guardar_datos()
        elif choice == '9':
            #print("Closing te program...")
            wait() 
            exit("Closing te program...") #es como poner un break pero termina todo el codigo,
            # a partir de este punto al exit tambien se le puede poner texto.
        wait(2)
    else:
        print("Invalid input,please try a real option")
        wait()

def clearscreen():
    #clear screen borra todo lo que se encuentra antes de la definicion.
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(i=2):
    #wait espera 2 segundos antes de continuar con el codigo,
    #puedes ingresar un numero para darle el tiempo que quieras o dejarlo por defecto
    import time
    time.sleep(i)

clearscreen()
#este seria el codigo llamando a las funciones mas compacto no?
while True:
    choice = menu()
    choices(choice)
