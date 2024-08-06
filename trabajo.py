list_trabajo_add= []
list_trabajo_substract =[]
list_trabajo_multiply =[]
list_trabajo_divide =[]
list_trabajo_power =[]
list_trabajo_Logaritmo =[]
# para que son estas listas? lo veras mas adelante en "guardar datos"
def add(num1,num2):
    print(f"{num1} + {num2} = {num1+num2}")
    list_trabajo_add.append(num1+num2)
    #print(f"{num1}+{num2}"), es igual a poner print(num1,"+",num2)
    
def subtract(num1,num2):
    print(f"{num1} - {num2} = {num1-num2}")
    list_trabajo_substract.append(num1-num2)

def multiply(num1,num2):
    print(f"{num1} * {num2} = {num1*num2}")
    list_trabajo_multiply.append(num1*num2)

def divide(num1,num2):
    print(f"{num1} / {num2} = {num1/num2}")
    list_trabajo_divide.append(num1/num2)

def power(num1,num2):
    print(f"{num1} ^ {num2} = {num1**num2}")
    list_trabajo_power.append(num1**num2)

def Logaritmo(num1,num2=10):
    import math
    print(math.log(num1,num2))
    list_trabajo_Logaritmo.append(math.log(num1,num2))
    #mat.log es logaritmos con "e" naturales, para hacerlo natural cambia la base a 10
    # el primer numero es num1 = el primer argumento y el num2 = base

def guardar_datos():
    #que hace esto? guarda los datos en un archivo tipo csv para usarlos o verlos mas tarde
    import csv
    #sin el import csv no funciona
    with open("Datos guardados suma.csv","+a", newline="") as archivo_csv_suma:
        #with open() abre un archivo la pimera parte en la esta el nombre del archivo en .csv
        #puede ser nombrada como sea, tambien se puede .txt, pero se me acomoda mas de esta forma a mi
        #el "a" es para agregar datos, si el archivo no exsite de antes, da un error
        #al ingreas un + antes del a "+a" crea el archivo si no existe
        # newline="", al crear una nueva linea en el archivo la crea sin espacios
        # as archivo_csv_suma, abre el archivo con el nombre de esa variable 
        writer = csv.writer(archivo_csv_suma)
        #writer es un objeto que permite escribir en el archivo csv
        if archivo_csv_suma.tell() == 0:
            #si el archivo esta vacio, es decir, no tiene datos, crea un titulo o como el programa lo
            #llama cabecera
            writer.writerow(["Suma"])
            #el writerow("suma"), es el titulo de la lista
        for i in range (len(list_trabajo_add)):
            #pasa por cada suma guardada y la agrega a el csv
            #nota, no le tengo puesto que guarde la operatoria, solo la suma y asi con el resto 
            writer.writerow([list_trabajo_add[i]])
            #el writerow es para agregar una fila a el csv, el i es para que agrege solo la suma

    with open("Datos guardados resta.csv", "+a", newline="") as archivo_csv_resta:
        writer = csv.writer(archivo_csv_resta)
        if archivo_csv_resta.tell() == 0:
            writer.writerow(["Resta"])
        for i in range (len(list_trabajo_substract)):
            writer.writerow([list_trabajo_substract[i]])

    with open("Datos guardados multiplicacion.csv", "+a", newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)
        if archivo_csv.tell() == 0:
            writer.writerow(["Multiplicacion"])
        for i in range (len(list_trabajo_multiply)):
            writer.writerow([list_trabajo_multiply[i]])

    with open("Datos guardados division.csv", "+a", newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)
        if archivo_csv.tell() == 0:
            writer.writerow(["Division"])
        for i in range (len(list_trabajo_divide)):
            writer.writerow([list_trabajo_divide[i]])

    with open("Datos guardados potencia.csv", "+a", newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)
        if archivo_csv.tell() == 0:
            writer.writerow(["Potencia"])
        for i in range (len(list_trabajo_power)):
            writer.writerow([list_trabajo_power[i]])

    with open("Datos guardados Logaritmo.csv", "+a",newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)
        if archivo_csv.tell() == 0:
            writer.writerow(["Logaritmo"])
        for i in range (len(list_trabajo_Logaritmo)):
            writer.writerow([list_trabajo_Logaritmo[i]])

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
        if choice not in ("7","8","9"):
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
            # a partir de este punto, al exit tambien se le puede poner texto.
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
